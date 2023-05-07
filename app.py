from flask import Flask, request, jsonify, render_template, url_for
import cohere
from cohere.responses.classify import Example
import sqlite3
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html', the_title='COHERE TEST')

@app.route('/endpoint', methods=['POST'])
def process_data():
    global input_data
    input_data = request.form['userSymptomsSummary']
    print("TETSTSTSTSTS ", input_data)
    # Do something with input_data
    return "Success"

@app.route('/calculate', methods=['POST'])
def calculate():
    #input_data = "I am young. I have a flu and high fever. I have pain in neck, back or joints. I have trouble breathing or coughing. I have sudden pain. I am bleeding. I have a loss of mobility, stiffness, serious, broken bones. I am swelling. I have skin irration and/or rash. I have been exposed to chemicals or environmental toxins. I have stress/anxiety/other mental health issues"
    #input_data = request.form['userSymptomsSummary']
    co = cohere.Client('oOv0i8UBwNAqI6viyLhqbynSMeiGfWYWamrE3DLy') # This is your trial API key
    
    examples=[Example("I have a flu", "Family Doctor"), Example("I would like a covid vaccine", "Family Doctor"), Example("I have a fever", "Family Doctor"), Example("I am feeling unwell and have small headaches", "Family Doctor"), Example("I broke my hand", "Hospital"), Example("I got into an accident", "Hospital"), Example("I have severe migraines", "Hospital"), Example("I am bleeding interally", "Hospital"), Example("I am having trouble breathing", "Hospital"), Example("I have a rash", "dermatologist"), Example("My skin is rough", "dermatologist"), Example("I have acne", "dermatologist")]
    inputs=[input_data] 


    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )
    result = jsonify({'result': response[0].prediction})
    # Storing Result and input string into Database
    
    return result

# gets the inputs and results and adds them to a table in a database
def add_to_db(inputs, result):
    # Create a connection object to the database
    conn = sqlite3.connect('MedVisor.db')

    # Create a cursor object
    cursor = conn.cursor()

    table_name = "resultsTable"

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))

    # Get the result
    result = cursor.fetchone()

    # Check if the table exists
    if result:
        # Insert a new row into the table
        cursor.execute("INSERT INTO resultsTable (summary, result) VALUES (?, ?)", (inputs, result))
        conn.commit()

        # gets all the rows in the table
        # cursor.execute("SELECT * FROM resultsTable")
        # conn.commit()
        # rows = cursor.fetchall()

        # Print the fetched data
        # for row in rows:
        #     print(row)

        # Close the connection
        conn.close()
        
    else:
        # Create a table
        cursor.execute('''CREATE TABLE resultsTable
                        (id INTEGER PRIMARY KEY,
                        summary TEXT,
                        result TEXT)''')

        # Commit the changes
        conn.commit()

if __name__ == '__main__':
    app.run(debug=True)
