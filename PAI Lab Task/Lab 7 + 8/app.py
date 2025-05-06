from flask import Flask, render_template, request
import requests

app = Flask(__name__)

MEALDB_API = "https://www.themealdb.com/api/json/v1/1/search.php?s="

@app.route("/", methods=["GET", "POST"])
def index():
    recipes = []
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        response = requests.get(MEALDB_API + query)
        data = response.json()
        if data["meals"]:
            recipes = data["meals"]
    return render_template("index.html", recipes=recipes, query=query)

if __name__ == "__main__":
    app.run(debug=True)
