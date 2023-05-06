from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', the_title='COHERE TEST')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_data = request.form['number']
    result = int(input_data) * 5
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
