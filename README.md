# Buscador de Imagens - Rottweiler

## Descrição

Este projeto realiza a busca de imagens da raça Rottweiler utilizando a API do Pixabay. As imagens são baixadas automaticamente e salvas em uma pasta local.

O objetivo é demonstrar consumo de API, manipulação de arquivos e organização básica de código em Python.

## Funcionamento

O programa envia uma requisição para a API do Pixabay utilizando uma chave de autenticação. A resposta é recebida em formato JSON, e a partir dela são extraídas as URLs das imagens.

Cada imagem é então baixada e salva localmente.

## Uso de variável de ambiente (.env)

A chave da API não fica exposta diretamente no código. Ela é armazenada em um arquivo separado chamado `.env`.

Conteúdo do arquivo `.env`:

API_KEY=chave_da_api

No código, a leitura dessa variável é feita com a biblioteca `python-dotenv`.

### Explicação do load_dotenv

O comando:

from dotenv import load_dotenv

serve para importar a função responsável por carregar variáveis de ambiente.

Quando executamos:

load_dotenv()

O Python lê o arquivo `.env` presente na pasta do projeto e carrega as variáveis definidas nele para dentro do ambiente de execução.

Após isso, é possível acessar essas variáveis utilizando:

API_KEY = os.getenv("API_KEY")

Ou seja:

* O `.env` guarda a chave
* `load_dotenv()` carrega essas informações
* `os.getenv()` permite usar a chave no código

Esse processo evita que informações sensíveis fiquem expostas no código fonte.

## Estrutura

buscadorRottweiler/

.gitignore
buscador_rottweiler.py
.env (não versionado)
rottweilers/ (não versionado)

## Execução

Instalar dependências:

pip install requests python-dotenv

Executar:

python buscador_rottweiler.py

## Observação

O arquivo `.env` não é enviado para o GitHub por motivos de segurança. A chave da API deve ser criada individualmente pelo usuário.

## Autor

Vladimir
