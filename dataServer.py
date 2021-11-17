import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import json

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

@app.route('/',  methods=['GET'])
def index():
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True, port='8001')
    
