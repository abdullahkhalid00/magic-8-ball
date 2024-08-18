from inference import *
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post('/ask')
async def ask_question(request: Request):
    try:
        data = await request.json()
        question = data.get('question', '')
        response = generate_response(question, instructions=load_instructions('../instructions.txt'))
        return {'response': response.strip()}
    except Exception as e:
        return {'error': str(e)}
