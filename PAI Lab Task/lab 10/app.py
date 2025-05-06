from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic response logic
def get_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return "You can apply online through our admission portal."
    elif "eligibility" in user_input:
        return "Eligibility criteria include a minimum of 60% in your previous degree."
    elif "documents" in user_input:
        return "Required documents: transcripts, ID, and passport-size photos."
    elif "deadline" in user_input:
        return "The admission deadline is July 31st."
    else:
        return "Sorry, I didn't understand that. Please ask about admission, eligibility, or deadlines."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def chatbot_response():
    user_input = request.args.get('msg')
    response = get_response(user_input)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
