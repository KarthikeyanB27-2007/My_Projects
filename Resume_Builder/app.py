from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "objective": request.form["objective"],
            "skills": request.form["skills"].split(","),
            "education": request.form["education"],
            "experience": request.form["experience"],
        }
        return render_template("resume.html", data=data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
