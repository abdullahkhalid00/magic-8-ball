# Magic 8 Ball in Python 🎱

A very basic implementation of the magic 8 ball game that simply asks the user for a question and uses a Gemini Pro model to generate an answer. The model simulates a magic 8 ball in real life.

## Usage

Get your Google API Key from [here](https://ai.google.dev/gemini-api/docs/api-key).

Open up  a terminal and clone the repository.

```bash
git clone <repo-link>
```

Navigate to the cloned repo directory.

```bash
cd magic_8_ball
```

Set up your Google API key as an environment variable.

Alternatively, you can create a `.env` file in your directory and use the `python-dotenv` library to read environment variables.

```python
GOOGLE_API_KEY='<your-api-key>'
```

Create a Python virtual environment and activate it.

```bash
python -m venv env
env\Scripts\activate
```

Install the necessary dependencies in `requirements.txt` file.

```bash
pip install -r requirements.txt
```

Open up a terminal and navigate to the `app` directory. Start the server by running `main.py`.

```bash
uvicorn main:app --reload
```

Open the `index.html` file in your browser of choice and play the game.

### Testing FastAPI Endpoint

Test the API by make a POST request on the `/ask` endpoint.

```bash
curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d "{\"question\":\"Will I succeed?\"}"
```

### Running in CLI

You can also play the game in command line by running `cli.py` in any terminal.

```bash
python cli.py --question "<your-question>"
```

## Deployment on Hugging Face 🤗

Despite much effort, I could not find my way around Vercel for deploying the frontend, instead I created another frontend on Gradio and deployed it as a Hugging Face Space.

## Contribution

Feel free to open up a pull request to point out a bug or an improvement.
