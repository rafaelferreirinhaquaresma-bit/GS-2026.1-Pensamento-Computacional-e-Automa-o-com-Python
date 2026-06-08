
nome_missao = "Orion Test Alpha"
nome_equipe = "Equipe Apollo"

# Matriz principal da missão (6 ciclos)
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacoes):
    indice = pontuacoes.index(max(pontuacoes))
    return areas_monitoradas[indice]


def gerar_recomendacao(alertas):
    if "CRÍTICO" in alertas:
        return "Ativar modo de segurança e priorizar sistemas críticos."
    elif "ATENÇÃO" in alertas:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Manter operação normal e continuar monitoramento."


# PROCESSAMENTO DA MISSÃO

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao, start=1):

    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    analises = [
        analisar_temperatura(temperatura),
        analisar_comunicacao(comunicacao),
        analisar_bateria(bateria),
        analisar_oxigenio(oxigenio),
        analisar_estabilidade(estabilidade)
    ]

    risco = sum(item[1] for item in analises)

    for pos in range(5):
        pontuacao_areas[pos] += analises[pos][1]

    riscos_ciclos.append(risco)

    classificacao = classificar_ciclo(risco)

    alertas = [item[0] for item in analises]
    recomendacao = gerar_recomendacao(alertas)

    print(f"\nCICLO {i}")
    print("-" * 60)

    print(f"Temperatura: {temperatura}°C | {analises[0][0]}")
    print(f"Comunicação: {comunicacao}% | {analises[1][0]}")
    print(f"Bateria: {bateria}% | {analises[2][0]}")
    print(f"Oxigênio: {oxigenio}% | {analises[3][0]}")
    print(f"Estabilidade: {estabilidade}% | {analises[4][0]}")

    print(f"Pontuação de risco: {risco}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")

# RELATÓRIO FINAL

media_temperatura = sum(c[0] for c in dados_missao) / len(dados_missao)
media_comunicacao = sum(c[1] for c in dados_missao) / len(dados_missao)
media_bateria = sum(c[2] for c in dados_missao) / len(dados_missao)
media_oxigenio = sum(c[3] for c in dados_missao) / len(dados_missao)
media_estabilidade = sum(c[4] for c in dados_missao) / len(dados_missao)

ciclo_critico = riscos_ciclos.index(max(riscos_ciclos)) + 1
maior_risco = max(riscos_ciclos)
risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

ciclos_criticos = 0
for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

tendencia = analisar_tendencia(riscos_ciclos[0], riscos_ciclos[-1])

area_mais_afetada = identificar_area_mais_afetada(pontuacao_areas)

classificacao_final = classificar_ciclo(round(risco_medio))

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Ciclos analisados: {len(dados_missao)}")

print(f"Média de temperatura: {media_temperatura:.2f} °C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"Ciclo mais crítico: Ciclo {ciclo_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")

print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")
for area, pontos in zip(areas_monitoradas, pontuacao_areas):
    print(f"{area}: {pontos} pontos")

print("\nÁrea mais afetada:")
print(area_mais_afetada)

print("\nClassificação final da missão:")
print(classificacao_final)

print("\nConclusão:")
print("A missão apresentou instabilidades durante a operação e requer monitoramento contínuo.")