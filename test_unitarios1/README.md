Projeto: Exemplos Simples de Python com Testes Unitários (pytest)

Este projeto contém 2 exemplos básicos em Python com testes unitários escritos com pytest.


Estrutura do projeto

meu_projeto/
├── calc.py
├── texto.py
├── test_calc.py
├── test_texto.py
└── README.md


✅ Descrição dos exemplos
1️⃣ Soma de dois números
Arquivo da função: calc.py

Função: soma(a, b)
Retorna a soma de dois números.

Teste: test_calc.py
Testa se a função soma retorna o valor correto em diferentes situações.

2️⃣Contar caracteres de uma string
Arquivo da função: texto.py

Função: contar_caracteres(texto)
Retorna a quantidade de caracteres na string.

Teste: test_texto.py
Testa a função com strings de diferentes tamanhos.


Como executar os testes
Instale o pytest (se ainda não estiver instalado):

bash
Copiar
Editar
pip install pytest
Navegue até a pasta do projeto no terminal:

bash
Copiar
Editar
cd caminho/para/meu_projeto
Execute os testes:

bash
Copiar
Editar
pytest
O pytest vai identificar todos os arquivos que começam com test_ e executar os testes.
O resultado vai mostrar quais testes passaram ou falharam.

✏️ Explicação rápida sobre testes
Cada teste usa assert para verificar se o resultado da função está correto.
Se a verificação for verdadeira, o teste passa; se for falsa, o teste falha.

Exemplo:

python
Copiar
Editar
assert soma(2, 3) == 5
Verifica se o retorno da função soma(2, 3) é igual a 5.