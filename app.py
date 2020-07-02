from flask import Flask
from utils.spreadsheet import Spreadsheet
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


@app.route('/')
def root():
    sheet = Spreadsheet(os.getenv("SPREADSHEET_ID"))
    sheet.getAll()
    return "YouTube Auto Uploader in action 💥!"

if __name__ == '__main__':
    app.run()
