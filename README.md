<p align="center">
   <a href="#english">🇺🇸 English</a> • <a href="#portuguese">🇧🇷 Português</a>
</p>

---

<a id="english"></a>
# FinSight

FinSight is a web application created with the idea of providing a dashboard to visualize key indicators of companies and funds from around the world.

## Prerequisites
- Docker and Docker Compose
- Git

## Technologies Used
- [Python](https://python.org)
- [Docker](https://www.docker.com)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org)
- [Plotly](https://plotly.com/python/)
- [YFinance](https://pypi.org/project/yfinance/)
- [Humanize](https://pypi.org/project/humanize/)

## Installation

1. Clone and access the repository:
    ```bash
    git clone <REPOSITORY_URL>
    cd <FOLDER_NAME>
    ```
2. Build the Docker image:
    ```bash
    docker compose build app
    ```

3. Run the container:
    ```bash
    docker compose up app
    ```

4. Access the application in your browser:
    ```
    http://localhost:8501
    ```

## Next Steps
- Create new metrics and indicators
- Improve the user interface
- Add more data sources
- In the future, rewrite using Django

---

<a id="portuguese"></a>
# FinSight

FinSight é um aplicativo web que surgiu com a ideia de criar um painel para visualizar os principais indicadores de empresas e fundos mundo a fora.

## Pré-requisitos
- Docker e Docker Compose
- Git

## Tecnologias utilizadas
- [Python](https://python.org)
- [Docker](https://www.docker.com)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org)
- [Plotly](https://plotly.com/python/)
- [YFinance](https://pypi.org/project/yfinance/)
- [Humanize](https://pypi.org/project/humanize/)


## Instalação

1. Clone e acesse o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DA_PASTA>
    ```
2. Faça o build da imagem Docker:
    ```bash
    docker compose build app
    ```

3. Execute o container:
    ```bash
    docker compose up app
    ```

4. Acesse a aplicação no navegador:
    ```
    http://localhost:8501
    ```

## Próximos passos
- Criar novas métricas e indicadores
- Melhorar a interface do usuário
- Adicionar mais fontes de dados
- Futuramente, reescrever usando Django