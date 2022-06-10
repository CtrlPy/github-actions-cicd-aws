# ------------------------------------------------
# Program by ctrlpy
#
#
# Version      Date           Info
# 1.0          10-jun-2022    Initial Version
#
# ----------------------------------------------

from flask import Flask, render_template

application = Flask(__name__)

# test
@application.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    application.run()