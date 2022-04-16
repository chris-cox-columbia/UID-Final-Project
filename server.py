from contextlib import redirect_stderr
from flask import Flask
from flask import render_template, Response, request, jsonify, redirect, url_for
from database import drinksData, questions
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route('/learn/intro/<drinkId>', methods=['GET','POST'])
def renderDrinkInfo(drinkId=None):
    global questions
    drinkInfo = drinksData[drinkId]
    return render_template("introDrinkPage.html", drinkInfo=drinkInfo)


@app.route('/learn/video/<drinkId>', methods=['GET','POST'])
def renderDrinkVideo(drinkId=None):
    global questions
    drinkInfo = drinksData[drinkId]
    return render_template("videoDrinkPage.html", drinkInfo=drinkInfo)



@app.route('/quiz/<questionId>', methods=['GET','POST'])
def renderQuestion(questionId=None):
    global questions

    questionDetails = questions[questionId]

    type = questionDetails["type"]

    if (type=="drag and drop"):
        return render_template("dragDrop.html", questionDetails=questionDetails)

    if (type=="ratios"):
        return render_template("ratios.html",questionDetails=questionDetails)
    
    if (type=="free form"):
        return render_template("freeForm.html",questionDetails=questionDetails)

if __name__ == "__main__":
    app.run(debug=True)