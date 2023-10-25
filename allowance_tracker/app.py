from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample data (you can load this data from the kids.json file)
kids_data = {
    "Alice": {"allowance": 10, "bonus_points": 0},
    "Bob": {"allowance": 15, "bonus_points": 0},
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    # Return the kids' data as JSON
    return jsonify(kids_data)

@app.route('/add_chore', methods=['POST'])
def add_chore():
    kid_name = request.form.get('kid_name')
    bonus_earned = float(request.form.get('bonus_earned'))
    
    if kid_name in kids_data:
        # Update the kid's bonus points
        kids_data[kid_name]["bonus_points"] += bonus_earned

        # Save the data to a JSON file (optional)
        save_data_to_json()

        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Kid not found")

@app.route('/apply_allowance_change', methods=['POST'])
def apply_allowance_change():
    kid_name = request.form.get('kid_name')
    allowance_change = float(request.form.get('allowance_change'))
    
    if kid_name in kids_data:
        # Update the kid's allowance
        kids_data[kid_name]["allowance"] += allowance_change

        # Save the data to a JSON file (optional)
        save_data_to_json()

        return jsonify(success=True)
    else:
        return jsonify(success=False, message="Kid not found")

def save_data_to_json():
    # Save the kids' data to a JSON file (optional)
    with open('data/kids.json', 'w') as json_file:
        json.dump(kids_data, json_file)

if __name__ == '__main__':
    app.run(debug=True)
