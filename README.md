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
cd 8_ball
```

Set up the API key by creating a `.env` file in your cloned directory. Alternatively, you can rename the `.env-sample` file and paste your API key in it.

```python
GOOGLE_API_KEY='<your-api-key>'
```

Play by running `main.py`.

```bash
python main.py
```

## Contribution

Feel free to open up a pull request to point out a bug or an improvement.
 