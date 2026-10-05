from flask import Flask, render_template, jsonify

app = Flask(__name__)


# ==========================================
# DEMO USER — STORED ON THE SERVER
# ==========================================

current_user = {
    "name": "Rawan",
    "plan": "Free"
}


# ==========================================
# MAIN PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# SECURE PRO API
# ==========================================

@app.route("/api/pro-data")
def pro_data():

    # The SERVER checks the user's permission.
    # We do NOT trust anything from the browser.

    if current_user["plan"] != "pro":

        return jsonify({
            "error": "Forbidden",
            "message": "Pro subscription required."
        }), 403


    # This sensitive data is returned ONLY
    # after the server confirms authorization.

    return jsonify({
        "feature": "Advanced Analytics",
        "monthly_revenue": "$48,250",
        "growth_rate": "+18.4%"
    })


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)