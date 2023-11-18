from flask import Flask, render_template_string, request, url_for
from flight_data import FlightData
from pydantic import ValidationError

app = Flask(__name__)

# serve the homepage to the user
@app.route('/', methods=['GET'])
def index():
    # render the form for the user input
    return render_template_string('''
        <form action="{{ url_for('submit_form') }}" method="post">
            Flight Number: <input type="text" name="flight_number"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # validate inputs using pydantic
        flight_data = FlightData(flight_number=request.form['flight_number'])
        # process valid input
        return f"Flight number: {flight_data.flight_number} submitted. Processing your request."
    except ValidationError as e:
        " Handle validation errors"
        return render_template_string("""
        Invalid flight number format. <a href="{{ url_for('index') }}">Try again</a>.
        """)

if __name__ == '__main__':
    app.run(debug=True)