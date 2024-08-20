from inference import *
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Question(BaseModel):
    question: str


@app.get('/')
async def read_root():
    return {'message': 'Welcome to Magic 8 Ball 🎱!'}

@app.post('/ask')
async def ask_question(question: Question):
    try:
        response = generate_response(question.question)
        return {'response': response.strip()}
    except Exception as e:
        return {'error': str(e)}
