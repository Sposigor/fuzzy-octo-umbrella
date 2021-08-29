# Calculo de IRRF

# Tabela de aliquotas do INSS: https://www.gov.br/inss/pt-br/saiba-mais/seus-direitos-e-deveres/calculo-da-guia-da-previdencia-social-gps/tabela-de-contribuicao-mensal

# Salário de Contribuição (R$) | Alíquota
# Até R$ 1.100,00 | 7,5%
# De R$ 1.100,01 a R$ 2.203,48 | 9%
# De R$ 2.203,49 até R$ 3.305,22 | 12%
# De R$ 3.305,23 até R$ 6.433,57 | 14%
# Tabela com ano base de 2021

# Tabela de aliquotas do IRRF: https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/tributos/irpf-imposto-de-renda-pessoa-fisica#dedu--o-mensal-por-dependente

# Dedução mensal por dependente = R$ 189,59

# Base de cálculo (R$) | Alíquota (%) | Parcela a deduzir do IRPF (R$)
# Até 1.903,98 | isento | isento
# De 1.903,99 até 2.826,65 | 7,5 | 142,80
# De 2.826,66 até 3.751,05 | 15 | 354,80
# De 3.751,06 até 4.664,68 | 22,5 | 636,13
# Acima de 4.664,68 | 27,5 | 869,36

def inss_irrf(rendimento): 
        
    # Tabelas do INSS para calcular o desconto
    aINSS = [0.0, 7.5, 9, 12, 14, 5000]
    dINSS = [0.0, 82.50, 99.31, 132.21, 437.97]
    bINSS = [0.0, 1100, 2203.48, 3305.22, 6433.57, 10000000]
        
    # Variaveis para suporte do calculo
    tProgressiva = 0
    x = 5
        
    # Repetição para encontrar o local dentro da lista com base no rendimento
    for i in range(0,len(aINSS)-1):
        if bINSS[i] <= rendimento < bINSS[i+1]:
            x = i
                    
    # Condição para situação do teto do desconto          
    if rendimento >= bINSS[4]:
        tProgressiva = 751.99
            
    # Condição para as demais situações de desconto na tabela progressiva
    else:
        for i in range(x, 0, -1):
            tProgressiva += dINSS[i]
                
    # Calculo de desconto do INSS que é (Salário - Faixa que se enquadra) * aliquota da faixa / 100
    dAtual = (((rendimento - bINSS[x]) * aINSS[x+1])/100)
        
    # Resto da aliquota de progressão do desconto
    INSS = tProgressiva + dAtual
        
    # Tabelas do IRRF para calcular o desconto
    aIRRF = [0.0, 7.5, 15, 22.5, 27.5, 5000]
    dIRRF = [0.0, 142.80, 354.80, 636.13, 869.36]
    bIRRF = [0.0, 1903.98, 2826.65, 3751.05, 4664.68, 10000000]
        
    # Variaveis para suporte do calculo
    y = 5
    IRRF = 0
        
    # Valor base para calcular o IRRF que é Salário - INSS
    irAtual = rendimento - INSS
        
    # Repetição para encontrar o local dentro da lista com base no rendimento
    for i in range(0,len(aINSS)-1):
        if bIRRF[i] < irAtual < bIRRF[i+1]:
            y = i
        
    # Condição para situação do teto do desconto 
    if irAtual > 4018.71:
        # Formula para calcular o imposto retido na fonte
        IRRF = ((irAtual * aIRRF[i-1]) / 100) - dIRRF[i-1]
            
    elif irAtual > 2900:
        # Formula para calcular o imposto retido na fonte
        IRRF = ((irAtual * aIRRF[i-2]) / 100) - dIRRF[i-2]
            
    elif irAtual > 1903.98:
        # Formula para calcular o imposto retido na fonte
        IRRF = ((irAtual * aIRRF[i-3]) / 100) - dIRRF[i-3]
            
    else:
        # Valores menores que a primeira faixa que são isentos de imposto
        IRRF = 0.0
        
    # Resultado da Formula
    return round(IRRF, 2), round(INSS, 2)