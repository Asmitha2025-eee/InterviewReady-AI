from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():

    data = request.json

    technical = float(data['technical'])
    communication = float(data['communication'])
    projects = float(data['projects'])
    certifications = float(data['certifications'])

    score = (
        technical * 0.4 +
        communication * 0.3 +
        projects * 0.2 +
        certifications * 0.1
    )

    if score >= 7:
        level = "Interview Ready"
    elif score >= 4:
        level = "Intermediate"
    else:
        level = "Beginner"

    suggestions = []

    if technical < 7:
        suggestions.append("Improve coding skills.")

    if communication < 7:
        suggestions.append("Practice communication and mock interviews.")

    if projects < 7:
        suggestions.append("Build more projects.")

    return jsonify({
        "score": round(score * 10, 2),
        "level": level,
        "suggestions": suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)