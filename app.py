from flask import Flask
from utils.spreadsheet import Spreadsheet
app = Flask(__name__)


@app.route('/')
def root():
    sheet = Spreadsheet()
    return "YouTube Auto Uploader in action 💥!"

if __name__ == '__main__':
    app.run()
