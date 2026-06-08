# GS-2026.1-Pensamento-Computacional-e-Automa-o-com-Python
# Mission Control AI

## Global Solution - FIAP

### Integrantes
- Rafael Ferreirinha Quaresma - RM:571949
- Lucas Klein da Veiga - RM:570029

---

## Missão

**Titan Research Mission**

O projeto Mission Control AI simula o monitoramento inteligente de uma missão espacial experimental.

O sistema analisa ciclos de monitoramento contendo:

- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional

Com base nesses dados, o programa:

- Gera alertas automáticos
- Calcula o risco de cada ciclo
- Classifica o estado da missão
- Identifica a área mais afetada
- Analisa a tendência da missão
- Exibe um relatório final

---

## Estrutura dos Dados

Cada ciclo é representado por:

```python
[
    temperatura,
    comunicacao,
    bateria,
    oxigenio,
    estabilidade
]
