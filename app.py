from flask import Flask, request, jsonify, render_template, url_for, redirect, session
import cohere
from cohere.responses.classify import Example
import sqlite3
app = Flask(__name__, static_url_path='/static')
app.secret_key = '99587061'

@app.route('/')
def index():
    return render_template('index.html', the_title='COHERE TEST')

@app.route('/endpoint', methods=['POST'])
def process_data():
    
    input_data = request.form.get('userSymptomsSummary')
    session['input_data'] = input_data
    inputsT=[session.get('input_data')] 
    print("\n",inputsT,"\n")
    # Do something with input_data
    return "Success"

@app.route('/calculate', methods=['POST'])
def calculate():
    #input_data = "I am young. I have a flu and high fever. I have pain in neck, back or joints. I have trouble breathing or coughing. I have sudden pain. I am bleeding. I have a loss of mobility, stiffness, serious, broken bones. I am swelling. I have skin irration and/or rash. I have been exposed to chemicals or environmental toxins. I have stress/anxiety/other mental health issues"
    #input_data = request.form['userSymptomsSummary']
    co = cohere.Client('oOv0i8UBwNAqI6viyLhqbynSMeiGfWYWamrE3DLy') # This is your trial API key
    
    examples=[Example("flu", "Family Doctor"), Example("covid", "Family Doctor"), Example("fever", "Family Doctor"), Example("feeling unwell ", "Family Doctor"), Example("I broke my hand", "Emergency Room"), Example("I got into an accident", "Emergency Room"), Example("I have severe migraines", "Emergency Room"), Example("bleeding interally", "Emergency Room"), Example("trouble breathing", "Emergency Room"), Example("rash", "Dermatologist"), Example("skin is rough", "Dermatologist"), Example("acne", "Dermatologist"), Example("Severe", "Emergency Room"), Example("posture", "Chiropractor"), Example("scoliosis", "Chiropractor"), Example("kid", "Pediatrician"), Example("headaches", "Family Doctor"), Example("small cut", "Hospital"), Example("bleeding", "Emergency Room"), Example("deep cut", "Emergency Room"), Example("youth", "Pediatrician"), Example("under age", "Pediatrician"), Example("Crashed", "Emergency Room"), Example("Very hurt", "Emergency Room"), Example("Suicide", "Therapist"), Example("Mental", "Therapist"), Example("killing myself", "Therapist"), Example("depression", "Therapist"), Example("abdominal ", "Emergency Room"), Example("severe", "Emergency Room"), Example("consciousness", "Emergency Room"), Example("overdose", "Emergency Room"), Example("posion", "Emergency Room"), Example("Seizure", "Emergency Room"), Example("allergic reaction", "Emergency Room"), Example(" sudden", "Emergency Room"), Example("loss", "Emergency Room"), Example("Broken bones", "Emergency Room"), Example("dislocated joints", "Emergency Room"), Example("Severe burns, cuts, or injuries to the head or spine", "Emergency Room"), Example("Common illnesses like colds, flu, and infections", "Family Doctor"), Example("Chronic conditions like diabetes, high blood pressure, and asthma ", "Family Doctor"), Example("Injuries like sprains, strains, and minor fractures ", "Hospital"), Example("anxiety ", "Therapist"), Example("mental health", "Therapist"), Example("Serious injuries like broken bones, head injuries, and deep cuts ", "Emergency Room"), Example("Chest pain, heart attack, or stroke symptoms", "Emergency Room"), Example("Severe allergic reactions or anaphylaxis", "Emergency Room"), Example("Difficulty breathing or shortness of breath", "Emergency Room"), Example("Seizures or convulsions", "Emergency Room"), Example("Severe stomach pain or vomiting", "Emergency Room"), Example("trauma", "Therapist"), Example("Relationship problems and family conflicts ", "Therapist"), Example("Grief", "Therapist"), Example("Addiction and substance abuse", "Therapist"), Example("Eating disorders ", "Therapist"), Example("stress", "Therapist"), Example("Back and neck pain ", "Chiropractor"), Example("Headaches and migraines ", "Chiropractor"), Example("Joint pain and stiffness ", "Chiropractor"), Example("Sports injuries ", "Chiropractor"), Example("Poor posture ", "Chiropractor"), Example("Carpal tunnel syndrome ", "Chiropractor"), Example("Skin conditions like acne, eczema, and psoriasis ", "Dermatologist"), Example("Skin cancer screenings and treatment ", "Dermatologist"), Example("Hair and nail disorders ", "Dermatologist"), Example("Cosmetic concerns like wrinkles, age spots, and scars ", "Dermatologist"), Example("warts", "Dermatologist"), Example("counseling", "Therapist"), Example("growth and development", "Pediatrician"), Example("eyes", "Optometrist"), Example("vision", "Optometrist"), Example("teeth", "Dentist"), Example("braces", "Dentist"), Example("invisaline ", "Dentist"), Example("fillings", "Dentist"), Example("gum disease", "Dentist"), Example("orthodontics", "Dentist"), Example("root canals", "Dentist"), Example("tooth extractions", "Dentist"), Example("dental implants", "Dentist"), Example("eye exams", "Optometrist"), Example("prescription glasses", "Optometrist"), Example("contact lenses", "Optometrist"), Example("treatment of eye diseases and disorders", "Optometrist"), Example("glaucoma", "Optometrist"), Example("cataracts", "Optometrist"), Example("Illness", "Family Doctor"), Example("surgery", "Emergency Room"), Example("neck pain", "Chiropractor"), Example("diet-related health concerns", "Family Doctor"), Example("pain management", "Family Doctor"), Example("voice disorders", "Therapist"), Example("Speech and communication difficulties", "Therapist"), Example("reproductive system disorders", "Family Doctor"), Example("urinary tract issues", "Hospital"), Example("sleep disorders", "Family Doctor"), Example("inflammation", "Hospital"), Example("foot and ankle injuries", "Hospital"), Example("mobility issues", "Family Doctor"), Example("loss of mobility", "Emergency Room"), Example("life care", "Emergency Room"), Example("lung ", "Emergency Room"), Example("disability", "Emergency Room"), Example("chronic pain", "Chiropractor"), Example("joint pain", "Chiropractor"), Example("severe illness", "Emergency Room"), Example("joint ", "Chiropractor"), Example("diagnostic tests", "Hospital"), Example("flashing lights.", "Emergency Room"), Example("suddenly", "Emergency Room"), Example("deep cut", "Emergency Room"), Example("won\'t stop bleeding", "Emergency Room"), Example("suddenly became", "Emergency Room"), Example("numbness", "Emergency Room"), Example("rash all over my body", "Emergency Room"), Example("suddenly decreased", "Emergency Room"), Example("ringing", "Emergency Room"), Example("severe headache", "Hospital"), Example("a lot of pain", "Emergency Room"), Example("sudden weight loss", "Emergency Room"), Example("coughing up blood.", "Emergency Room"), Example("a lot of pain", "Emergency Room"), Example("panic attacks", "Therapist"), Example("remembering things.", "Hospital"), Example("acute", "Emergency Room"), Example("sexual assault", "Therapist"), Example("physical assault", "Emergency Room"), Example("routine check-ups", "Family Doctor"), Example("painful", "Emergency Room"), Example("unbearable", "Emergency Room"), Example("skin", "Dermatologist"), Example("Serious injuries", "Emergency Room"), Example("temperature is high", "Emergency Room"), Example("tightness in the chest", "Emergency Room"), Example("chest pain", "Emergency Room"), Example("Ingestion ", "Emergency Room"), Example("swelling of the face or throat", "Emergency Room"), Example("suicidal thoughts", "Therapist"), Example("Self harm", "Therapist"), Example("Serious injuries", "Emergency Room"), Example("tests", "Hospital"), Example("urgent", "Hospital"), Example("emotional", "Therapist"), Example("Hormonal", "Therapist"), Example("reproductive", "Hospital"), Example("weight", "Family Doctor"), Example("cramping", "Family Doctor"), Example("diarrheaa", "Family Doctor"), Example("stabbed", "Emergency Room"), Example("fatigued", "Family Doctor"), Example("breast", "Hospital"), Example("exhaustion and nausea", "Family Doctor"), Example("neck", "Chiropractor"), Example("back", "Chiropractor"), Example("joint", "Chiropractor"), Example("medium", "Hospital"), Example("severe", "Emergency Room"), Example("senior", "Emergency Room"), Example("kid", "Pediatrician"), Example("breathing", "Emergency Room"), Example("coughing", "Family Doctor"), Example("sudden", "Emergency Room"), Example("bleeding", "Emergency Room"), Example("loss of mobility", "Emergency Room"), Example("stiffness", "Chiropractor"), Example("serious", "Emergency Room"), Example("broken bones", "Emergency Room"), Example("swelling", "Emergency Room"), Example("skin", "Dermatologist"), Example("rash", "Dermatologist"), Example("toxic", "Emergency Room"), Example("stress", "Therapist"), Example("anxiety", "Therapist"), Example("mental health", "Therapist"), Example("painful", "Emergency Room")]
    #inputs=[input_data] 
    print("SESSSION \n\n\n\n\n\n" , session)
    inputs=[session.get('input_data')] 
    print("\n",inputs,"\n")
    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )
    result = response[0].prediction
    # Storing Result and input string into Database
    print("\n\n\n RESULTS TESTTSTST: "  + result + "\n\n\n")
    if result is None:
        result = "No result available"

    if result == "null":
        result = "No result available"
    session.clear();
    return jsonify({'result': result})

@app.route('/results')
def show_results():
    result = request.args.get('result')
    return render_template('results.html', the_title='Results', result=result)


if __name__ == '__main__':
    app.run(debug=True)
