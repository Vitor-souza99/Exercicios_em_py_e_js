# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('exercício3/faturamento.json', 'r') as f:
    faturamentoMensal = json.load(f)['Marco']

faturamento = [dia['faturamento'] for dia in faturamentoMensal if dia['faturamento'] > 0 and dia['dia'] % 7 not in [5, 6]]

menorFaturamento = min(faturamento)

maiorFaturamento = max(faturamento)

diasComFaturamento = [f for f in faturamento if f > 0]
mediaMensal = sum(diasComFaturamento) / len(diasComFaturamento)

diasAcimaDaMedia = len([f for f in faturamento if f > mediaMensal])

#resultado:
print("Menor valor de faturamento:", menorFaturamento)
print("Maior valor de faturamento:", maiorFaturamento)
print("Número de dias com faturamento acima da média mensal:", diasAcimaDaMedia)
