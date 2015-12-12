from flask import Flask, render_template, request, Response
from recom.py import *
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def return_index():
    return render_template('index.html')
    
@app.route('/opinion', methods=['POST'])
def opinion_process():
    opinion = request.form['opinion']
    movie_id = request.form['movie_id']
    storeJSON(movie_id, opinion)
    return giveJSON()

@app.route('/')
def base():
    return 'Hello!'




if __name__ == "__main__":
    app.run(debug=True)