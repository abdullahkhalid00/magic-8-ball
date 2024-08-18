import random
import time
from inference import *


def get_response_list(file):
    responses = []
    with open(file, 'rb') as f:
        for line in f:
            responses.append(line.decode().strip())
    return responses


if __name__ == "__main__":
    responses = get_response_list('./responses.txt')
    while True:
        q = input("What's your question? ")
        print('Thinking...')
        time.sleep(3)
        """
        responses = get_response_list('./responses.txt')
        response = responses[random.randint(0, len(responses) - 1)]
        """
        response = generate_response(question=q, instructions=load_instructions('./instructions.txt'))
        print(f"The 8 ball says: {response.strip()}")
        flag = input('Would you like to ask again? (Y/n) ')
        if flag.lower() == 'n':
            break
