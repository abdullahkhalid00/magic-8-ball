import google.generativeai as genai
import dotenv

dotenv.load_dotenv()


def load_instructions(file):
    instructions = []
    with open(file, 'rb') as f:
        for line in f:
            instructions.append(line.decode().strip())
    return '\n'.join(instructions)

def generate_response(question, instructions):
    genai.configure()
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro',
        system_instruction=instructions
    )
    response = model.generate_content(question)
    return response.text
