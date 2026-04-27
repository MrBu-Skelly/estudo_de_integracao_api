# estudo_de_integracao_api

API Currency Tracker
Este projeto é um script de automação desenvolvido em Python para realizar a extração e o monitoramento de dados financeiros em tempo real. Ele foi construído para colocar em prática conceitos de integração de sistemas e manipulação de dados externos.

Objetivo do Projeto
Desenvolver uma ferramenta que consuma APIs REST, trate retornos em formato JSON e apresente informações úteis (como cotações de moedas) de forma automatizada.

Tecnologias e Ferramentas
Linguagem: Python 3.x

Bibliotecas: requests (para chamadas HTTP)

Formato de Dados: JSON

API Utilizada: AwesomeAPI

Funcionalidades
Requisições HTTP: Uso do método GET para buscar dados de cotação atualizados.

Parsing de JSON: Conversão da resposta da API em dicionários Python para extração de campos específicos (como o preço de compra - bid).

Interface via Terminal: Exibição clara dos valores para o usuário.

Como Rodar o Projeto
Clone este repositório.

Certifique-se de ter o Python instalado.

Instale a biblioteca requests:

Bash
pip install requests
Execute o arquivo principal:

Bash
python main.py
Aprendizados Técnicos
Neste projeto, reforcei meus conhecimentos em:

Funcionamento de Endpoints e rotas de API.

Diferença entre métodos de requisição (foco no GET).

Tratamento de dados dinâmicos (extração de valores dentro de objetos JSON aninhados).

Organização de código seguindo boas práticas de desenvolvimento.
