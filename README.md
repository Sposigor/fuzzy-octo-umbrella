# DESAFIO - SEMANA 2 

Um algoritmo é um conjunto de instruções e procedimentos lógicos para a solução de um determinado problema.

Vamos pensar na declaração do Imposto de Renda de Pessoa Física (IRPF).

Para encontrar a base de cálculo do IRPF, é preciso subtrair do salário bruto de um contribuinte a alíquota do INSS (Tabela 1) e o valor referente aos dependentes (R$189,59 por dependente). Os valores das alíquotas para cálculo do imposto estão na Tabela 2:
#### **Tabela 1: Contribuição INSS**
```
| Salário de contribuição (R$) | Alíquota INSS |
|:----------------------------:|:-------------:|
|         até 1.045,00         |      7,5%     |
|   de 1.045,01 até 2.089,60   |       9%      |
|   de 2.089,61 até 3.134,40   |      12%      |
|   de 3.134,41 até 6.101,06   |      14%      |
```
Para o desafio proposto, o cálculo da alíquota do INSS poderá ser realizado direto de acordo a faixa salarial (cálculo antigo), ou considerando as novas alíquotas progressivas previstas na Reforma da Previdência, ou seja, significa que as taxas serão cobradas apenas sobre a parcela do salário que se enquadrar em cada faixa, fazendo com que o percentual descontado do total dos ganhos seja diferente.

Exemplo do cálculo para alíquota progressiva: um trabalhador que ganha R$ 5.445,00 pagará 7,5% sobre R$ 1.045,00 (R$ 78,38), acrescido de 9% sobre diferença da faixa de 1.045,01 até 2.089,60 (R$ 1.044,59), sendo R$ 94,01, mais 12% sobre diferença da faixa de 2.089,61 até 3.134,40 (R$ 1.044,79), sendo R$ 125,37, e mais 14% sobre diferença da faixa de 3.134,41 até o valor total do salário de R$ 5.445,00 (R$ 2.310,59), sendo R$ 323,48, totalizando o valor da alíquota do INSS em R$ 621,25.
#### **Tabela 2: Alíquotas do Imposto de Renda**
```markdown
|   Base de cálculo (R$)   | Alíquota (%) | Parcela a deduzir do IR (R$) |
|:------------------------:|:------------:|:----------------------------:|
| de 1.903,99 até 2.826,65 |     7,5%     |            142,80            |
| de 2.826,66 até 3.751,05 |      15%     |            354,80            |
| de 3.751,06 até 4.664,68 |     22,5%    |            636,13            |
|     acima de 4.664,68    |     27,5%    |            869,36            |
```
Considerando que os algoritmos são utilizados constantemente em nosso cotidiano, o desafio da semana é elaborar um algoritmo para calcular o imposto de renda mensal a ser pago por um indivíduo a partir do seu salário bruto mensal e quantidade de dependentes. Represente o algoritmo elaborado fazendo uso de um fluxograma e um pseudocódigo.