from flask import Flask, render_template, request

app = Flask(__name__)

# Home page – reservation form
@app.route('/')
def index():
    return render_template('index.html')

# Process reservation and show ticket
@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    room = request.form['room']
    guests = request.form['guests']
    hotel = request.form['hotel']

    # Simple calculation (optional)
    room_rates = {'Standard': 1000, 'Deluxe': 2000, 'Suite': 3500}
    days = 1
    total_cost = room_rates.get(room, 1000) * days

    return render_template('ticket.html',
                           name=name, email=email, phone=phone,
                           checkin=checkin, checkout=checkout,
                           room=room, guests=guests, hotel=hotel,
                           total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
