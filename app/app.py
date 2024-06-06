from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"]) 
def home():
    
    with open("app/data/person.json") as f:
        personas = json.load(f)

    alumn = {
        "name": "Gize Yuhann Martinez Espinosa",
        "matricula": "20211045",
        "cuatrimestre": "9",
        "grupo":"B"
    }

    if request.method == "POST":
        name = request.form.get("name")
        matricula = request.form.get("matricula")
        personas.append({
            "name": name,
            "matricula": matricula
        })
    return render_template("index.html", data = personas, alumn = alumn)

if __name__ == "__main__":
    app.run(debug=True)