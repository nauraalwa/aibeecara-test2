# API for LLM Backend

To prevent from too much credits being used by the user, we can create an API that limits each user's credits in a single API Key.

# How to test:

# 1. Install the dependencies

Make a virtual environment in Python and install the dependencies in requirements.txt

```
pip install -r requirements.txt
```

# 2. Run the main.py

Use uvicorn to activate the API
Change the system prompt using to your use case, recommended to use instruction prompting technique

```
uvicorn main:app --reload
```

# 3. Test the API

Run test-api.py and enter your own prompt to test the API.