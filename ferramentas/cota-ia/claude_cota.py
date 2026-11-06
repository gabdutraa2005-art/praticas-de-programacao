#!/usr/bin/env python3
"""Cota de IA: uso das janelas de 5h e da semana do Claude (plano Max) e do Codex (ChatGPT).

Lê os mesmos endpoints que o /usage de cada CLI usa, com o login que cada uma já guarda
(~/.claude/.credentials.json e ~/.codex/auth.json). Só lê o token; quem renova é a própria CLI.
Sem argumento imprime um resumo; com --json imprime o que a extensão da barra do GNOME mostra.
"""
import json, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def duracao(min_):
    min_ = max(0, int(min_))
    if min_ >= 48 * 60:
        return f"{min_ // 1440}d"
    return f"{min_ // 60}h{min_ % 60:02d}"


def janela(rotulo, pct, fim, total_min):
    """fim: datetime do reset; total_min: tamanho da janela."""
    agora = datetime.now(timezone.utc)
    falta = (fim - agora).total_seconds() / 60
    local = (fim + timedelta(seconds=30)).astimezone()
    hoje = datetime.now().astimezone().date()
    if local.date() == hoje:
        quando = f"hoje {local:%H:%M}"
    elif local.date() == hoje + timedelta(days=1):
        quando = f"amanhã {local:%H:%M}"
    else:
        quando = f"{DIAS[local.weekday()]} {local:%d/%m %H:%M}"

    # ritmo: no passo atual, a cota acaba antes de renovar?
    passado = total_min - falta
    ritmo = "ritmo tranquilo"
    if pct >= 100:
        ritmo = "estourou"
    elif passado > total_min * 0.05 and pct > 0:
        ate_100 = (100 - pct) / (pct / passado)
        if ate_100 < falta:
            ritmo = f"nesse ritmo acaba em ~{duracao(ate_100)}"
    nivel = "critico" if pct >= 90 else "alerta" if pct >= 70 else "ok"
    return {"rotulo": rotulo, "pct": round(pct), "nivel": nivel,
            "detalhe": f"renova {quando} · em {duracao(falta)} · {ritmo}"}


def pegar(url, headers):
    req = urllib.request.Request(url, headers=headers)
    return json.load(urllib.request.urlopen(req, timeout=15))


def erro_http(e, cli):
    if isinstance(e, urllib.error.HTTPError):
        return f"login vencido: abra o {cli}" if e.code in (401, 403) else f"erro {e.code}"
    return "sem conexão"


def claude():
    p = {"nome": "Claude", "plano": "", "url": "https://claude.ai/settings/usage", "janelas": [], "erro": None}
    try:
        o = json.loads((Path.home() / ".claude/.credentials.json").read_text())["claudeAiOauth"]
    except Exception:
        p["erro"] = "sem login"
        return p
    tier = o.get("rateLimitTier") or ""
    p["plano"] = (o.get("subscriptionType") or "").capitalize() + (" 5x" if "5x" in tier else " 20x" if "20x" in tier else "")
    try:
        d = pegar("https://api.anthropic.com/api/oauth/usage", {
            "Authorization": f"Bearer {o['accessToken']}",
            "anthropic-beta": "oauth-2025-04-20", "User-Agent": "claude-cota"})
    except Exception as e:
        p["erro"] = erro_http(e, "claude")
        return p
    for chave, rotulo, total in (("five_hour", "5h", 300), ("seven_day", "sem", 10080)):
        j = d.get(chave)
        if j and j.get("resets_at"):
            p["janelas"].append(janela(rotulo, j.get("utilization") or 0,
                                       datetime.fromisoformat(j["resets_at"]), total))
    return p


def codex():
    p = {"nome": "Codex", "plano": "", "url": "https://chatgpt.com/codex/settings/usage", "janelas": [], "erro": None}
    try:
        t = json.loads((Path.home() / ".codex/auth.json").read_text())["tokens"]
    except Exception:
        p["erro"] = "sem login"
        return p
    try:
        d = pegar("https://chatgpt.com/backend-api/wham/usage", {
            "Authorization": f"Bearer {t['access_token']}",
            "ChatGPT-Account-Id": t.get("account_id", ""), "User-Agent": "claude-cota"})
    except Exception as e:
        p["erro"] = erro_http(e, "codex")
        return p
    p["plano"] = (d.get("plan_type") or "").capitalize()
    rl = d.get("rate_limit") or {}
    for chave, rotulo in (("primary_window", "5h"), ("secondary_window", "sem")):
        j = rl.get(chave)
        if j and j.get("reset_at"):
            total = (j.get("limit_window_seconds") or 0) / 60 or (300 if rotulo == "5h" else 10080)
            p["janelas"].append(janela(rotulo, j.get("used_percent") or 0,
                                       datetime.fromtimestamp(j["reset_at"], timezone.utc), total))
    return p


def ler():
    with ThreadPoolExecutor(2) as ex:
        provs = list(ex.map(lambda f: f(), (claude, codex)))
    return {"hora": datetime.now().strftime("%H:%M"), "provedores": provs}


if __name__ == "__main__":
    r = ler()
    if "--json" in sys.argv:
        print(json.dumps(r, ensure_ascii=False))
        sys.exit()
    for p in r["provedores"]:
        print(f"{p['nome']} {p['plano']}".strip() + (f": {p['erro']}" if p["erro"] else ""))
        for j in p["janelas"]:
            print(f"  {j['rotulo']:>3} {j['pct']:>3}%  {j['detalhe']}")
