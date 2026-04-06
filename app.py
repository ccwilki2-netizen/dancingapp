from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Fake database
studios = [
    {"name": "Rhythm Nation Studio", "city": "Detroit"},
    {"name": "Urban Groove Dance", "city": "Chicago"},
    {"name": "Elite Motion Dance Co.", "city": "Detroit"},
    {"name": "Midnight Moves Studio", "city": "New York"},
    {"name": "Smooth Steps Academy", "city": "Detroit"},
]

def assign_status():
    return random.choice(["Normal", "Elite", "Suspicious 👀"])

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        city = request.form.get("city")

        for studio in studios:
            if studio["city"].lower() == city.lower():
                results.append({
                    "name": studio["name"],
                    "status": assign_status()
                })

    return render_template("index.html", results=results, request=request)

if __name__ == "__main__":
    app.run(debug=True)