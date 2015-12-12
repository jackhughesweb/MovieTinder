from flask import Flask, render_template, request, Response
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def return_index():
    return render_template('index.html')
    
@app.route('/opinion', methods=['POST'])
def opinion_process():
    return '{ "test": "testing" }'

@app.route('/')
def base():
    return 'Hello!'




if __name__ == "__main__":
    app.run(debug=True)