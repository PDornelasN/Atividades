# Atividade 3

## Fit de funções

### Funções Treinadas
- **Seno** (`sin(x)`) no intervalo [0, 2π]
- **Cosseno** (`cos(x)`) no intervalo [0, 2π]
- **Tangente** (`tan(x)`) no intervalo [0, 2π] 
- **Sinc** (`sin(x)/x`) no intervalo [-10, 10]
- **Gaussiana** (`exp(-x²)`) no intervalo [-10, 10]

Nesta atividade foi feito o fit das funções acima, utilizamos o `tensorflow` como biblioteca de machine learning. O tipo de rede neural foi uma rede retangular com 3 camadas ocultas. A função de ativação utilizada foi a `tanh`.


## Derivadas

Neste código o objetivo é calcular a derivada de uma função seno, porém a rede não foi treinada com a função seno e sua derivada, mas sim com polinomios. Foi utilizado o `skit-learn` como biblioteca de machine learning. 


Neste código a base de dados de treinamento é fundamental para um bom resultado, simplismente utilizar polinômios de vários graus com coeficientes aleatórios não é suficiente. A base de dados deve conter pontos que representem bem a função que se deseja aproximar. Dessa forma modificamos a base de dados para conter polinômios de grau 5, 4 e 2 e suas derivadas. Essa é uma boa escolha se olharmos para as raízes das funções seno e cosseno no intervalo analizado. Outra escolha foi esolher esses polinômios com raízes simétricas em zero, isso ajuda a rede a ter casos de treinamento que se parecem com essas funções. 