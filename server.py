from contextlib import redirect_stderr
from flask import Flask
from flask import render_template, Response, request, jsonify, redirect, url_for
from database import drinksData, questions
app = Flask(__name__)
score = 0


@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route('/learn/intro/<drinkId>', methods=['GET','POST'])
def renderDrinkInfo(drinkId=None):
    global drinksData
    drinkInfo = drinksData[drinkId]
    return render_template("introDrinkPage.html", drinkInfo=drinkInfo)


@app.route('/learn/video/<drinkId>', methods=['GET','POST'])
def renderDrinkVideo(drinkId=None):
    global drinksData
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


# check the users answer for a drag and drop question
def check_drag_and_drop(questionId, user_answers):
    global questions
    global score
    correct_answers = questions[questionId]['answer']
    is_correct = True
    response = {
        'correct': [],
        'incorrect': [],
        'missing': []
    }
    # check if each answer selection is correct
    for answer in user_answers:
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

        
    # if is_correct:
    #     score += 1


    return response
        

def check_ratios(questionId, user_answers):
    global questions
    correct_answer = dict(zip(questions[questionId]['options'], questions[questionId]['answer']))
    response = {
        'correct': [],
        'incorrect': [],
    }
    is_correct = True

    for ingredient, ratio in user_answers.items():
        if correct_answer[ingredient] == ratio:
            response['correct'].append(ingredient)
        else:
            response['incorrect'].append((ingredient, correct_answer[ingredient]))
            is_correct = False

    # if is_correct:
    #     score += 1

    return response


def check_free_form(questionId):
    global questions
    correct_answer = questions[questionId]['answer']


    return correct_answer
    
    
    
    
        


if __name__ == "__main__":

    app.run(debug=True)