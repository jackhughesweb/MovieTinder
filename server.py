from flask import Flask, render_template, request, Response
from recom import *
import random
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def return_index():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status_get():
    return giveJSON(random.randint(1, 100))
    
@app.route('/opinion', methods=['POST'])
def opinion_process():
    opinion = request.form['opinion']
    movie_id = request.form['movie_id']
    storeJSON(movie_id, opinion)
    return giveJSON(random.randint(1, 100))

@app.route('/')
def base():
    return 'Hello!'




if __name__ == "__main__":
    app.run(debug=True)