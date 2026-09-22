"""
Quote of the Day — SDEV 4320 Lab 6 deployment app

This app is already finished. You are not writing or fixing code today,
you are deploying it. Read it once so you know what you're pushing live,
then move to the deployment guide.

Run it locally first, to confirm it works before you deploy it:
    pip install -r requirements.txt
    python app.py

Then visit http://localhost:5000
"""

import random
from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Programs must be written for people to read. — Harold Abelson",
    "The best error message is the one that never shows up. — Thomas Fuchs",
    "Simplicity is prerequisite for reliability. — Edsger Dijkstra",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Code is read more often than it is written. — Guido van Rossum",
]


@app.route("/")
def home():
    quote = random.choice(QUOTES)
    return f"""
    <html>
      <head><title>Quote of the Day</title></head>
      <body style="font-family: sans-serif; max-width: 600px; margin: 80px auto; text-align: center;">
        <h1>Quote of the Day</h1>
        <p style="font-size: 20px;">{quote}</p>
        <p><a href="/">Refresh for another</a> &middot; <a href="/api/quote">JSON version</a></p>
      </body>
    </html>
    """


@app.route("/api/quote")
def api_quote():
    return jsonify({"quote": random.choice(QUOTES)})


if __name__ == "__main__":
    app.run(debug=True)
