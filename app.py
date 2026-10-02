from flask import Flask, render_template, request
from inference_engine import analyze_profile

app = Flask(__name__)


# ==========================================
# HOME
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================
# ASSESSMENT
# ==========================================

@app.route("/assessment")
def assessment():

    return render_template(
        "assessment.html"
    )


# ==========================================
# HOW IT WORKS
# ==========================================

@app.route("/how-it-works")
def how_it_works():

    return render_template(
        "how_it_works.html"
    )


# ==========================================
# CAREERS
# ==========================================

@app.route("/careers")
def careers():

    return render_template(
        "careers.html"
    )


# ==========================================
# RESULT
# ==========================================

@app.route("/result", methods=["POST"])
def result():

    user_facts = {

        "education":
            request.form["education"],

        "programming":
            request.form["programming"],

        "mathematics":
            request.form["mathematics"],

        "problem_solving":
            request.form["problem_solving"],

        "technology":
            request.form["technology"],

        "data_interest":
            request.form["data_interest"],

        "creativity":
            request.form["creativity"],

        "security_interest":
            request.form["security_interest"],

        "work_style":
            request.form["work_style"],

        "teamwork":
            request.form["teamwork"],

        "activity":
            request.form["activity"],

        "career_priority":
            request.form["career_priority"]

    }


    # ==========================================
    # RUN EXPERT SYSTEM
    # ==========================================

    analysis = analyze_profile(
        user_facts
    )


    # ==========================================
    # SEND DATA TO RESULT PAGE
    # ==========================================

    return render_template(

        "result.html",

        recommendations=
            analysis["recommendations"],

        derived_facts=
            analysis["derived_facts"],

        reasoning_trace=
            analysis["reasoning_trace"]
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )