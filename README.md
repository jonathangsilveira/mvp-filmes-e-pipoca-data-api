# Filmes & Pipoca - API de dados

Esta API (Application Programming Interface) é um MVP que armazena informações sobre filmes fornecido pela [API TMDB](https://developer.themoviedb.org/reference/intro/getting-started).
Tem como objetivo validar os conteúdos passados nas disciplinas da sprint de Arquitetura de software da pós-graduação em Engenharia de Software, pela PUC-Rio.

# Requisitos

- Implementação de uma API REST ou GraphQL.
- Dockerfile para cada componente desenvolvido com todo o processo de implementação da solução em um container docker.
- Qualidade da Documentação da API em Swagger.
- Criatividade e Inovação.

# Funcionalidades

Este componente da arquitetura persiste as informações sobre as ações do usuário em relação a filmes fornecidos pelo componente A:

- Criação de lista de filmes de interesse (Watchlist);
- Adição de filmes na lista de interesse (Watchlist);
- Exclusão de filmes da lista de interesse (Watchlist);
- Retornar lista de interesse com seus respectivos filmes;
- Armazenar avaliação de filmes;

# Arquitetura da aplicação

![fluxograma](https://github.com/jonathangsilveira/mvp-filmes-e-pipoca-gateway-api/blob/main/fluxograma.png)

# Tecnologias

- Python 3.11.8;
- SQLite (Persistencia em banco de dados);
- Flask;
- SQLALchemy;
- Protocolo de comunicação Rest/JSON
- Documentação da API no padrao Swagger.

# Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Este comando criar o ambiente virtual para o projeto:

```
py -3 -m venv .venv
```

Este comando ativa o ambiente virtual para o terminal:

```
.\.venv\Scripts\activate
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

Para executar a API basta executar:

```
flask --app .\app\app.py  run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
flask --app .\app\app.py  run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/api/](http://localhost:5000/api) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker buildx build -t mvp-filmes-e-pipoca-gateway-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 mvp-filmes-e-pipoca-gateway-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/api/](http://localhost:5000/api/) no navegador.
