import random
import time


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
        time.sleep(5)
        print(f"The 8 ball says: {responses[random.randint(0, len(responses) - 1)]}")
        flag = input('Would you like to ask again? (Y/n) ')
        if flag.lower() == 'n':
            break
