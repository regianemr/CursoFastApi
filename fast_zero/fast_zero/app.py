from fastapi import FastAPI

# from fastapi.responses import HTMLResponse

from http import HTTPStatus

from fast_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'mensagem': 'Olá, mundo!'}


@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema):

    return user

# @app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
# def read_root():
#     return """
#     <html>
#         <head>
#             <title> Nosso olá mundo!</title>
#         </head>
#         <body>
#             <h1> Olá Mundo </h1>
#         </body>
#     </html> """
