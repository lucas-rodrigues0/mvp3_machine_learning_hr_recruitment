# Machine Learning HR Recruitment prediction


Projeto de MVP realizado para o curso de Pós graduação em Engenharia de Software da PUC-Rio - Pontifícia Universidade Católica do Rio de Janeiro.  


## Sumário

- [Objetivo](#objetivo)
- [Tecnologias](#tecnologias)
- [Arquitetura](#arquitetura)
- [Dataset](#dataset)
- [Configuração e Instalação](#configuração-e-instalação)
- [Testes automáticos](#testes-automáticos)
- [Endpoints](#endpoints)


## Objetivo

O projeto de MVP tem como objetivo treinar um modelo de Machine Learning e integrá-lo a um sistema web com um Front-end para imputar novos dados que serão analisados e gerar uma nova predição que será retornada à tela para a exibição.


Foi escolhido um dataset com dados de processo de recrutamento e seleção de candidatos. A partir de dados dos candidatos e do processo de seleção, o modelo é capaz de prever se o candidato será contratado ou não. As especificações dos dados necessários podem ser vistos na sessão [Dataset](#dataset)


## Tecnologias

- [Python](https://www.python.org/)
- [Flask-openapi3](https://luolingchun.github.io/flask-openapi3/v3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Scikit Learn](https://scikit-learn.org/stable/)
- [Pytest](https://docs.pytest.org/en/stable/)


## Arquitetura

O sistema é composto pelo Back-end implementado no diretório `API`, e pelo Front-end no diretório `FRONT`.  


O modelo de Machine Learning encontra-se embarcado no sistema back-end.  
O front-end possui um formulário para cadastramento de candidatos, que pede todos os dados necessários para o modelo realizar uma predição.  
O back-end retorna então a lista de todos os candidatos cadastrados já com o resultado da predição. Todos os dados são inseridos no banco de dados.  
É possível editar os dados de um candidato já cadastrado. Será então feita uma nova predição para a total atualização dos dados do candidato no banco de dados.  


O banco de dados utilizado é um SQLite que cria automaticamente o diretório `database` para a persistência dos dados. O sistema de log também irá criar o diretório `log` para o seu funcionamento.  


A árvore de diretórios utilizada é:  
```
.
├── api/
|   ├── database/                                               # gerado automaticamente
|   ├── log/                                                    # gerado automaticamente
|   ├── machine_learning/
|   │   ├── data/
|   │   │   └── golden_dataset_hr_recruitment.csv
|   │   ├── models/
|   │   │   └── hr_recruitment_GBclassifier.pkl
|   │   ├── notebooks/
|   │   │   └── hr_recruitment_predict_ML_notebook.ipynb
|   │   ├── pipelines/
|   │   │   ├── hr_recruitment_pipeline_test_randomForrest.pkl
|   │   │   └── hr_recruitment_GBpipeline.pkl
|   │   └── scalers/
|   │       └── standard_scaler_recruitment.pkl
|   ├── model/
|   │   ├── __init__.py
|   │   ├── base.py
|   │   ├── candidate.py
|   │   ├── evaluator.py
|   │   ├── loader.py
|   │   ├── ml_model.py
|   │   ├── pipeline.py
|   │   └── preprocessor.py
|   ├── schemas/
|   |   ├── __init__.py
|   |   ├── candidate_schema.py
|   |   └── error_schema.py
|   ├── tests/
|   |   ├── __init__.py
|   |   └── test_models.py
|   ├── app.py
|   └── logger.py
├── front/
|   ├── scripts/
|   |   └── index.js
|   ├── styles/
|   |   └── style.css
|   └── index.html
├── .gitignore
├── requirements.txt
└── README.md
```


## Dataset

As informações do Dataset podem ser encontradas no repositório do Kaggle, com as referências de sua autoria e especificações. O Link a seguir é do dataset original.  


Para finalidade do projeto o dataset foi copiado integralmente e sem alteração, armazenado em um repositório do github, pra facilitar a avaliação necessária. Qualquer outro uso deverá seguir as especificações do repositório original bem como mencionar a autoria de `Rabie El Kharoua`.  


O dataset original foi gerado para fins didáticos.  


[Link do Dataset no Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data)

[Link da cópia do Dataset no GitHub](https://github.com/lucas-rodrigues0/dataset_recruitment_data)


As especificações das colunas de acordo com o Dataset utilizado são:

- __Age__  
    Description: Age of the candidate.  
    Data Type: Integer.  
    Data Range: 20 to 50 years.  

- __Gender__  
    Description: Gender of the candidate.  
    Data Type: Binary.  
    Categories: Male (0) or Female (1).  

- __Education Level__  
    Description: Highest level of education attained by the candidate.  
    Data Type: Categorical.  
    Categories:  
    * 1: Bachelor's (Type 1)  
    * 2: Bachelor's (Type 2)  
    * 3: Master's  
    * 4: PhD  

- __Experience Years__  
    Description: Number of years of professional experience.  
    Data Type: Integer.  
    Data Range: 0 to 15 years.  

- __Previous Companies Worked__  
    Description: Number of previous companies where the candidate has worked.  
    Data Type: Integer.  
    Data Range: 1 to 5 companies.  

- __Distance From Company__  
    Description: Distance in kilometers from the candidate's residence to the hiring company.  
    Data Type: Float (continuous).  
    Data Range: 1 to 50 kilometers.  

- __Interview Score__  
    Description: Score achieved by the candidate in the interview process.  
    Data Type: Integer.  
    Data Range: 0 to 100.  

- __Skill Score__  
    Description: Assessment score of the candidate's technical skills.  
    Data Type: Integer.  
    Data Range: 0 to 100.  

- __Personality Score__  
    Description: Evaluation score of the candidate's personality traits.  
    Data Type: Integer.  
    Data Range: 0 to 100.  

- __Recruitment Strategy__  
    Description: Strategy adopted by the hiring team for recruitment.  
    Data Type: Categorical.  
    Categories:  
    * 1: Aggressive  
    * 2: Moderate  
    * 3: Conservative  

- __Hiring Decision (Target Variable)__  
    Description: Outcome of the hiring decision.  
    Data Type: Binary (Integer).  
    Categories:  
    * 0: Not hired  
    * 1: Hired  

### Dataset Information
* Records: 1500
* Features: 10
* Target Variable: HiringDecision (Binary)


## Configuração e Instalação

Depois de clonar o projeto, para a configuração e instalação do sistema é aconselhável a utilização de um ambiente virtual para as dependências. O ambiente virtual será utilizado somente com o sistema back-end, e por tanto pode ser criado dentro do diretório `api`.  

na raiz do diretório executar o comando:
```
python3 -m venv .venv
```

para ativar o ambiente rodar o comando:
```
# sistema unix
source .venv/bin/activate

# sistema windows
.\.venv\Script\activate
```

Com o ambiente ativado, fazer a instalação das dependências necessárias. Execute o comando:
```
pip install -r requirements.txt
```

Para levantar o servidor Back-end, na raiz do diretório `api`, e com o ambiente virtual ativado, executar o comando:
```
python app.py
```
Para acessar o servidor:
```
http://127.0.0.1:5000/
```

Para o Front-end, basta abrir o arquivo `front/index.js` no browser.

## Testes automáticos

Foram implementados testes automatizados para verificar métricas do modelo com o intuito de avaliar se um novo modelo possui metricas suficiente ou melhor que a do modelo embarcado. Para comparação foi utilizado uma pipeline com o Random Forest, que possui metricas semelhantes ao modelo embarcado. As métricas utilizadas nos testes são `acurácia`, `recall`, `precisão` e `f score`  

Para rodar os teste, na raiz do diretório `api`, e com o ambiente virtual ativado, executar o comando:
```
pytest -v
```

## Endpoints

A rota home `"/"` redirecionará para a rota `"/openapi"` de documentação Swagger, Redocs ou Rapidoc fornecida pelo Flask openapi. Na documentão é possivel ver as especificações de cada endpoint.
```
http://127.0.0.1:5000/
```


Os endpoints implementados são:


* GET /candidate  
    Lista todos os candidatos cadastrados na base de dados

* POST /candidate  
    Adiciona ou atualiza candidato na base de dados

* DELETE /candidate/{id}  
    Remove candidato da base de dados pelo seu ID

