const faturamentoMensal = {
    SP: 67836.43,
    RJ: 36678.66,
    MG: 29229.88,
    ES: 27165.48,
    Outros: 19849.53
  };
  
  const totalFaturamento = Object.values(faturamentoMensal).reduce((acc, curr) => acc + curr, 0);
  
  const percentuais = Object.entries(faturamentoMensal).map(([estado, faturamento]) => {
    return {
      estado,
      percentual: (faturamento / totalFaturamento) * 100
    };
  });
  
  const resultadosDiv = document.getElementById('resultados');
  
  percentuais.forEach(({estado, percentual}) => {
    const resultado = document.createElement('p');
    resultado.innerText = `${estado} - ${percentual.toFixed(2)}%`;
    resultadosDiv.appendChild(resultado);
  });
  
