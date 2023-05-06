from flask import Flask, request, jsonify, render_template
import cohere
from cohere.responses.classify import Example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', the_title='COHERE TEST')


@app.route('/receive-string', methods=['POST'])
def receive_string():
    my_string = request.form['my_string']
    print(my_string)
    return 'String received'

@app.route('/calculate', methods=['POST'])
def calculate():
    input_data = request.form['number']

    co = cohere.Client('oOv0i8UBwNAqI6viyLhqbynSMeiGfWYWamrE3DLy') # This is your trial API key
    
    examples=[Example("I have a flu", "Family Doctor"), Example("I would like a covid vaccine", "Family Doctor"), Example("I have a fever", "Family Doctor"), Example("I am feeling unwell and have small headaches", "Family Doctor"), Example("I broke my hand", "Hospital"), Example("I got into an accident", "Hospital"), Example("I have severe migraines", "Hospital"), Example("I am bleeding interally", "Hospital"), Example("I am having trouble breathing", "Hospital"), Example("I have a rash", "dermatologist"), Example("My skin is rough", "dermatologist"), Example("I have acne", "dermatologist")]
    inputs=[input_data] 


    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )
    return jsonify({'result': response[0].prediction})

if __name__ == '__main__':
    app.run(debug=True)
