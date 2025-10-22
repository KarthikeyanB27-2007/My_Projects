# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to hold candidate data dynamically
candidates = []

@app.route('/')
def home():
    return render_template('add_candidates.html', candidates=candidates)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    name = request.form.get('name')
    party = request.form.get('party')
    if name and party:
        candidates.append({"name": name, "party": party, "votes": 0})
    return redirect(url_for('home'))

@app.route('/voting')
def voting():
    if not candidates:
        return "No candidates added yet! Please add candidates first."
    return render_template('voting.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    selected = request.form.get('candidate')
    for c in candidates:
        if c['name'] == selected:
            c['votes'] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', candidates=candidates)

if __name__ == '__main__':
    app.run(debug=True)
