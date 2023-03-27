**1.**\
**a)** \
   A soma de datas é um questão computacional, onde devem ser considerado os dias, meses e anos para equacionar o problema. Nesse contexto, devem ser levados em conta meses com diferentes dias, por exemplo, há meses que terminam com 30 dias, outros que terminam com 31 dias; o mês de fevereiro é outro ponto que pode ser levado em consideração, pois dependendo se o ano é bissextos ou não, ele pode terminar com 29 ou 28, respectvamente. Outro detalhe, se a data escolhida mais o número de dias que deseja somar ultrapassar o dia 31/12/XXXX deve ser somado 1 ao ano escolhido anteriormente. O conjunto de valores que deve ser recebidos pelo algoritmo são dias
   (1<= x <= 31), meses (1 <= x <= 12) e anos (x >= 0000). 

**b)**
   1. Escolha um dia de 1 e 31; 
   2. Escolha um mês de 1 e 12; 
   3. Escolha um ano a partir de 0001; 
   4. Some X unidades à sua data,
      1. Caso o mês tenha 30 ou 31 dias no máximo, volte a contar a partir do dia 1 e some uma unidade ao mês escolhido; 
      2. Caso o mês resultante for maior que 12, volte a contar a partir do mês 1;
      3. Caso a data resultante ultrapasse 31/12, volte a contar a partir de 
      01/01 e some uma unidade ao ano escolhido; 
   5. Mostre a data resultante; 

**c)** \
   Esse problema computacional descrito seria mais complexo que o anterior, já que deve ser analisado mais situações, ou seja, para se determinar a soma de datas contando dias úteis devemos considerar os dias dos finais de semana, que não contam como dias úteis. Portanto, seria necessário um algoritmo com instruções elementares válidas mais complexas. Não necessáriamente seria igual ao problema anterior, na qual precisa apenas somar X dias à data escolhida e observar se irá ultrapassar o dia 31.
