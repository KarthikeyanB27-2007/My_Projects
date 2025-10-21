from flask import Flask, render_template, request
import secrets

app = Flask(__name__)

# Sample matches for dropdown
matches = {
    "ind_aus": {"teams": "India vs Australia", "date": "Oct 25, 2025", "venue": "M. A. Chidambaram Stadium, Chennai"},
    "eng_sa": {"teams": "England vs South Africa", "date": "Nov 10, 2025", "venue": "Lord's Cricket Ground, London"},
    "nz_pak": {"teams": "New Zealand vs Pakistan", "date": "Nov 15, 2025", "venue": "Eden Park, Auckland"},
    # Added international matches
    "aus_eng_ashes": {"teams": "Australia vs England (Ashes)", "date": "Dec 26, 2025", "venue": "Melbourne Cricket Ground, Melbourne"},
    "wi_ind": {"teams": "West Indies vs India", "date": "Jan 20, 2026", "venue": "Kensington Oval, Bridgetown, Barbados"},
    "pak_eng": {"teams": "Pakistan vs England", "date": "Feb 1, 2026", "venue": "Gaddafi Stadium, Lahore"},
    "sa_aus": {"teams": "South Africa vs Australia", "date": "Mar 5, 2026", "venue": "Newlands Cricket Ground, Cape Town"},
    "ind_pak_t20wc": {"teams": "India vs Pakistan (T20 World Cup)", "date": "Mar 16, 2026", "venue": "R. Premadasa Stadium, Colombo"},
    "sl_nz": {"teams": "Sri Lanka vs New Zealand", "date": "Feb 28, 2026", "venue": "Galle International Stadium, Galle"},
    "eng_aus_odi": {"teams": "England vs Australia (ODI)", "date": "Sep 1, 2025", "venue": "The Oval, London"},
    # Added IPL matches
    "csk_rcb": {"teams": "Chennai Super Kings vs Royal Challengers Bangalore (IPL)", "date": "Apr 1, 2026", "venue": "M. A. Chidambaram Stadium, Chennai"},
    "mi_kkr": {"teams": "Mumbai Indians vs Kolkata Knight Riders (IPL)", "date": "Apr 10, 2026", "venue": "Wankhede Stadium, Mumbai"},
    "rr_dc": {"teams": "Rajasthan Royals vs Delhi Capitals (IPL)", "date": "Apr 15, 2026", "venue": "Sawai Mansingh Stadium, Jaipur"},
    "pbks_srh": {"teams": "Punjab Kings vs Sunrisers Hyderabad (IPL)", "date": "Apr 22, 2026", "venue": "Himachal Pradesh Cricket Association Stadium, Dharamsala"},
    "gt_lsg": {"teams": "Gujarat Titans vs Lucknow Super Giants (IPL)", "date": "Apr 28, 2026", "venue": "Narendra Modi Stadium, Ahmedabad"},
    "rcb_mi": {"teams": "Royal Challengers Bangalore vs Mumbai Indians (IPL)", "date": "May 5, 2026", "venue": "M. Chinnaswamy Stadium, Bengaluru"},
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        match_key = request.form["match"]
        match_info = matches.get(match_key, {})

        ticket_data = {
            "name": name,
            "match": match_info.get("teams", "N/A"),
            "date": match_info.get("date", "N/A"),
            "venue": match_info.get("venue", "N/A"),
            "ticket_id": secrets.token_hex(4).upper(),
            "seat_number": "A" + str(secrets.randbelow(100) + 1)
        }
        return render_template("ticket.html", ticket=ticket_data)
    return render_template("index.html", matches=matches)

if __name__ == "__main__":
    app.run(debug=True)















