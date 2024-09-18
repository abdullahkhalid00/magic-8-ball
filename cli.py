import argparse
from inference import generate_response


def main():
    parser = argparse.ArgumentParser(description='Ask the Magic 🎱 Ball a question.')
    parser.add_argument('-q', '--question', type=str, required=True, help="The question you want to ask the Magic 🎱 Ball")
    args = parser.parse_args()
    question = args.question
    response = generate_response(question)
    print(f"Magic 🎱 Ball says: {response}")


if __name__ == '__main__':
    main()
