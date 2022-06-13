# Projeto-Redes-Complexas

## Lógica de forma grosseira

Temos diversas classes referentes a diferentes objetos, mas estes são os mais importantes:

- Sistema
- Duto
- Solver

### Sistema
Monta o sistema de redes complexas e estrutura as equações de massa, as equações de energia e
o sistema de equações que será resolvido via scipy.optimize.fsolve.

### Duto
Diversas informações pertinentes à rede são determinadas nesta classe, por estarem intimamente associadas
aos dutos. Valores de vazão, resistência hidráulica, presença ou ausência de bomba, comprimento e diâmetro 
dos dutos, fator de friccao, coeficiente de perdas singulares e rugosidade absoluta definem um duto neste
projeto.

### Solver
Esta classe é responsável por aplicar o fsolve e entregar a solução do sistema de equações que foi montado
anteriormente.

## Testes
Os testes unitários implementados visam garantir que o projeto entregue os resultados esperados para cada caso
com uma precisão mínima.
