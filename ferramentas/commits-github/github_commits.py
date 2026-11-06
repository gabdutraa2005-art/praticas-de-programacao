#!/usr/bin/env python3
"""Commits no GitHub: quantos fiz hoje, há quantos dias seguidos e os últimos.

Usa o login que o gh (GitHub CLI) já guarda. Conta os commits de que sou autor no branch
principal dos meus repositórios, agrupados pelo dia no fuso local. (O gráfico do GitHub, pela
API, conta em UTC: um commit às 22h no Brasil cairia no dia seguinte.)
Sem argumento imprime um resumo; com --json imprime o que a extensão da barra do GNOME mostra.
"""
import json, subprocess, sys
from collections import Counter
from datetime import datetime, timedelta

JANELA_DIAS = 120  # histórico lido para calcular a sequência
REPOS = []  # vazio = todos os meus repositórios; ou só alguns, ex.: ["praticas-de-programacao"]
SEMANAS_GRADE = 13  # colunas da grade, uns 3 meses
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

QUERY = """
query($desde: GitTimestamp!) {
  viewer {
    login
    url
    repositories(first: 30, ownerAffiliations: OWNER, orderBy: {field: PUSHED_AT, direction: DESC}) {
      nodes {
        name
        defaultBranchRef { target { ... on Commit {
          history(first: 100, since: $desde) {
            nodes { messageHeadline committedDate url author { user { login } } }
          }
        } } }
      }
    }
  }
}
"""


def buscar(desde):
    """Pede ao gh os commits recentes de cada repositório (uma chamada só, em GraphQL)."""
    r = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-f", f"desde={desde}"],
        capture_output=True, text=True, timeout=40,
    )
    if r.returncode != 0:
        msg = (r.stderr or r.stdout).strip().splitlines()
        raise RuntimeError(msg[-1] if msg else "gh falhou")
    return json.loads(r.stdout)["data"]["viewer"]


def quando(dt, hoje):
    if dt.date() == hoje:
        return f"hoje {dt:%H:%M}"
    if dt.date() == hoje - timedelta(days=1):
        return f"ontem {dt:%H:%M}"
    return f"{DIAS[dt.weekday()]} {dt:%d/%m}"


def montar_grade(por_dia, hoje):
    """Grade igual à do GitHub: cada coluna é uma semana (domingo em cima), a última é a atual."""
    desde_domingo = (hoje.weekday() + 1) % 7  # weekday(): segunda = 0 ... domingo = 6
    inicio = hoje - timedelta(days=desde_domingo + 7 * (SEMANAS_GRADE - 1))
    semanas = []
    for s in range(SEMANAS_GRADE):
        domingo = inicio + timedelta(days=7 * s)
        dias = []
        for d in range(7):
            data = domingo + timedelta(days=d)
            dias.append({"data": f"{data:%d/%m}", "n": por_dia[data],
                         "hoje": data == hoje, "futuro": data > hoje})
        # nome do mês na coluna em que ele começa
        mes_anterior = (domingo - timedelta(days=7)).month
        semanas.append({"mes": MESES[domingo.month - 1] if domingo.month != mes_anterior else "",
                        "dias": dias})
    # a primeira coluna leva o nome do mês só se o próximo nome não vier colado nela
    if len(semanas) > 1 and not semanas[1]["mes"]:
        semanas[0]["mes"] = MESES[inicio.month - 1]
    return semanas


def ler():
    agora = datetime.now().astimezone()
    hoje = agora.date()
    desde = (agora - timedelta(days=JANELA_DIAS)).isoformat(timespec="seconds")
    v = buscar(desde)

    commits = []
    for repo in v["repositories"]["nodes"]:
        if REPOS and repo["name"] not in REPOS:
            continue
        alvo = (repo.get("defaultBranchRef") or {}).get("target") or {}
        for c in (alvo.get("history") or {}).get("nodes", []):
            if ((c.get("author") or {}).get("user") or {}).get("login") != v["login"]:
                continue
            dt = datetime.fromisoformat(c["committedDate"].replace("Z", "+00:00")).astimezone()
            commits.append({"repo": repo["name"], "msg": c["messageHeadline"], "dt": dt, "url": c["url"]})
    commits.sort(key=lambda c: c["dt"], reverse=True)

    por_dia = Counter(c["dt"].date() for c in commits)
    n_hoje = por_dia[hoje]

    # sequência: dias seguidos com commit. Sem commit hoje ainda, conta até ontem (ainda dá tempo).
    dia = hoje if n_hoje else hoje - timedelta(days=1)
    seq = 0
    while por_dia[dia]:
        seq += 1
        dia -= timedelta(days=1)

    if n_hoje:
        nivel = "ok"
    elif agora.hour >= 21:
        nivel = "critico"
    else:
        nivel = "alerta"

    grade = montar_grade(por_dia, hoje)
    return {
        "login": v["login"],
        "perfil": v["url"],
        "hora": f"{agora:%H:%M}",
        "hoje": n_hoje,
        "nivel": nivel,
        "sequencia": seq,
        "sequencia_mais": seq >= JANELA_DIAS,
        "semana": sum(por_dia[hoje - timedelta(days=i)] for i in range(7)),
        "periodo": sum(d["n"] for s in grade for d in s["dias"]),
        "dias_com_commit": sum(1 for s in grade for d in s["dias"] if d["n"]),
        "grade": grade,
        "ultimos": [{"repo": c["repo"], "msg": c["msg"], "quando": quando(c["dt"], hoje), "url": c["url"]}
                    for c in commits[:5]],
    }


def main():
    try:
        d = ler()
    except FileNotFoundError:
        d = {"erro": "gh não instalado"}
    except Exception as e:  # rede, login expirado, timeout
        d = {"erro": str(e)[:120]}

    if "--json" in sys.argv:
        print(json.dumps(d, ensure_ascii=False))
        return
    if "erro" in d:
        print("Erro:", d["erro"])
        sys.exit(1)
    seq = f"{d['sequencia']}{'+' if d['sequencia_mais'] else ''}"
    print(f"@{d['login']}  ·  hoje: {d['hoje']}  ·  sequência: {seq} dias  ·  7 dias: {d['semana']}")
    print(f"3 meses: {d['periodo']} commits em {d['dias_com_commit']} dias\n")
    # grade no terminal, igual à do menu
    topo = [" "] * (2 * len(d["grade"]) + 2)  # cada coluna ocupa 2 caracteres
    for i, s in enumerate(d["grade"]):
        topo[2 * i:2 * i + len(s["mes"])] = s["mes"]
    print("     " + "".join(topo).rstrip())
    for linha, nome in enumerate(["dom", "seg", "ter", "qua", "qui", "sex", "sáb"]):
        celulas = []
        for s in d["grade"]:
            dia = s["dias"][linha]
            celulas.append("  " if dia["futuro"] else "■ " if dia["n"] else "· ")
        print(f"{nome:>4} " + "".join(celulas))
    print()
    for c in d["ultimos"]:
        print(f"  {c['quando']:>12}  {c['repo']}: {c['msg']}")


if __name__ == "__main__":
    main()
