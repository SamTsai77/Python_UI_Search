import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("famous_visit_spots.csv", "r") as f:
    reader = csv.DictReader(f)
    visit_data = list(reader)




@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/visits/")
def visit_list():
    # template found in templates/index.html
    results = []
    if not request.args.get("place"):
        return jsonify(results)

    search_string = request.args.get("place").lower().strip()
    print(f"Searching for: {search_string}")


    for visit in visit_data:
        print(f"Checking visit: {visit}")
        place = visit["Place"].lower()
            

        if search_string in place:
            results.append(visit)
            print(f"Found matching visit: {visit}")

    return jsonify(results)

app.run(debug=True)
