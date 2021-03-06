from contextlib import redirect_stderr
import time
from flask import Flask
from flask import render_template, Response, request, jsonify, redirect, url_for
from database import drinksData, questions, studentAnswers, images
app = Flask(__name__)

score = 0
visit_times = {}
correctlyAnsweredQ = set()


@app.route('/')
def welcome():
    update_visit_time('/')
    return render_template("welcome.html")


@app.route('/learn/intro/<drinkId>', methods=['GET','POST'])
def renderDrinkInfo(drinkId=None):
    update_visit_time(f"/learn/intro/{drinkId}")
    global drinksData
    drinkInfo = drinksData[drinkId]
    return render_template("introDrinkPage.html", drinkInfo=drinkInfo)


@app.route('/learn/video/<drinkId>', methods=['GET','POST'])
def renderDrinkVideo(drinkId=None):
    update_visit_time(f"/learn/video/{drinkId}")
    global drinksData
    drinkInfo = drinksData[drinkId]
    return render_template("videoDrinkPage.html", drinkInfo=drinkInfo)


@app.route('/congratulations', methods=['GET'])
def congrats():
    return render_template("congrats.html")


@app.route('/quiz/<questionId>', methods=['GET','POST'])
def renderQuestion(questionId=None):
    global questions
    questionDetails = questions[questionId]

    type = questionDetails["type"]

    if (type=="drag and drop"):
        if request.method == "GET":
            return render_template("dragDrop.html", questionDetails=questionDetails, images=images)
        else:
            user_data = request.get_json()
            user_answers = user_data["answer"].split(",")
            result = check_drag_and_drop(questionId, user_answers)
            update_visit_time(f"/quiz/{questionId}")
            return jsonify(result)

    if (type=="ratios"):
        if request.method == "GET":
            return render_template("ratios.html",questionDetails=questionDetails, images=images)
        else:
            user_data = dict(request.get_json())
            result = check_ratios(questionId, user_data)
            update_visit_time(f"/quiz/{questionId}")
            return jsonify(result)

    if (type=="free form"):
        if request.method == "GET":
            update_visit_time(f"/quiz/{questionId}")
            return render_template("freeForm.html",questionDetails=questionDetails)

        else:
            result = update_freeform_score(questionId)
            return jsonify(result)


@app.route('/studentAnswers',methods=['POST'])
def postAnswers():
    global studentAnswers

    answerObj = request.get_json()

    id = answerObj["id"]

    studentAnswers[id] = answerObj

    additionInfo = studentAnswers[id]
    return jsonify(additionInfo=additionInfo)


def check_drag_and_drop(questionId, user_answers):
    global questions
    global score
    correct_answers = questions[questionId]['answer'
    ]
    print("CORRECT ANSWERS", correct_answers)
    is_correct = True
    response = {
        'correct': [],
        'incorrect': [],
        'missing': []
    }
    # check if each answer selection is correct
    for answer in user_answers:
        if len(answer) == 0:
            continue
        if answer in correct_answers:
            response['correct'].append(answer)
        else:
            response['incorrect'].append(answer)
            is_correct = False

    # check for missing answers in the user response
    for answer in correct_answers:
        if answer not in user_answers:
            response['missing'].append(answer)
            is_correct = False

    # If the user already answered this question, do not update their score
    url = f"/quiz/{questionId}"

    global correctlyAnsweredQ
    if is_correct and questionId not in correctlyAnsweredQ:
        score += 1
        correctlyAnsweredQ.add(questionId)


    return response


def check_ratios(questionId, user_answers):
    global questions
    global score
    global correctlyAnsweredQ
    correct_answer = dict(zip(questions[questionId]['options'], questions[questionId]['answer']))
    response = {
        'correct': [],
        'incorrect': [],
    }
    is_correct = True

    for ingredient, ratio in user_answers.items():
        if correct_answer[ingredient] == ratio:
            item = ingredient, correct_answer[ingredient]
            response['correct'].append(item)
        else:
            item = ingredient, correct_answer[ingredient]
            response['incorrect'].append(item)
            is_correct = False

    url = f"/quiz/{questionId}"
    if is_correct and questionId not in correctlyAnsweredQ:
        score += 1
        correctlyAnsweredQ.add(questionId)



    return response


def update_freeform_score(questionId):
    global score
    global correctlyAnsweredQ
    if questionId not in correctlyAnsweredQ:
        score += 1
        correctlyAnsweredQ.add(questionId)
    return None


def update_visit_time(endpoint):
    current_time = time.time()
    visit_times[endpoint] = current_time


@app.route('/visit_times', methods=['GET'])
def get_times():
    return jsonify(visit_times)

@app.route('/score', methods=['GET'])
def get_score():
    global score
    return jsonify(score)

if __name__ == "__main__":
    app.run(debug=True)
