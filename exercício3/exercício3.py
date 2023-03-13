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
