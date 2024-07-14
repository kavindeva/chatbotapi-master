"""
Deploy Flask App in IIS Server
"""

from flask import Flask
app = Flask(__name__)
@app.route("/bot")
def home():
    return "Hello, Welcome to iAssist restapi's."
if __name__ == "__main__":
    app.run()
