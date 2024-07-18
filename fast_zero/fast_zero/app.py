from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'mensagem': 'Olá, mundo!'}


@app.get('/aula1')
def read_root():
    return {'aula: 1'}


@app.get('/aula2')
def read_root():
    return {'aula: 2'}
