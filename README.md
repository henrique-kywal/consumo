# consumo
Projeto para finalização da pós de arquiteto em software.  
*Preferi aproveitar uma idéia que tive de criar um app para acompanhar o consumo de combustível do meu carro*

### Instalação/configuração do python

Criei o ambiente virtual:  
`python3 -m venv .venv`

Ativei o ambiente:  
`source .venv/bin/activate`

Instalei as primeiras **dependências**:  
- `pip install fastapi uvicorn sqlalchemy pydantic pytest`
- `pip freeze > requirements.txt` *(Pacote de todas as bibliotecas e suas versões instaladas no ambiente).*  
- `python -m pip install fastapi` *(Executa os endpoints e define o comportamento da API.)*
- `python -m pip install fastapi uvicorn sqlalchemy` (Biblioteca para trabalhar com banco relacionais - ORM)
- `python -m pip install pytest` (Para realizar testes automatizados)

Comando para iniciar a aplicação em **http://127.0.0.1:8000**:  
- `python -m uvicorn app.main:app --reload`

### Documentação no Swagger UI ###
http://127.0.0.1:8000/docs#/


### Imagens ###

- [C4 no draw.io](https://raw.githubusercontent.com/henrique-kywal/consumo/a57fd510dbebcd752dc6c7ea3161d82b258cf414/api-consumo/docs/API%20Consumo.drawio.svg)  
- [Preview do Swagger](https://github.com/henrique-kywal/consumo/blob/main/api-consumo/docs/API_Consumo_-_Swagger_UI.png?raw=true)  
- [Exemplo da tela do vscode](https://github.com/henrique-kywal/consumo/blob/main/api-consumo/docs/tela_vscode_app_consumo.png?raw=true)

