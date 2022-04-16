from contextlib import redirect_stderr
from flask import Flask
from flask import render_template, Response, request, jsonify, redirect, url_for
app = Flask(__name__)

drinksData = {"1":{"id":"1",
                    "name":"Moscow Mule",
                    "description":["Highball cocktail - mixed drink with alcoholic base and large proportion of non-alcoholic mixer",
                                    "Born in Manhattan in 1940s",
                                    "Often served in copper mug, which takes on the cold temperature and keeps the drink cold"],
                    "ingredient_number":"three",
                    "ingrdient_list":["Ginger Beer","Lime Slice","Vodka"],
                    "ingredient_details":{
                                    "Ginger Beer":{
                                                    "quantity":"two parts",
                                                    "hexcode":"#FFB200"
                                                    },
                                    "Lime Slice":{
                                            "quantity":"Garnish",
                                            "hexcode":"#DCFF00"
                                            },
                                    "Vodka":{
                                            "quantity":"One Part",
                                            "hexcode":"#FFFFFF"
                                        }
                                    },
                    "procedure":["Add Ginger Beer and Vodka together at a ratio of 2:1",
                                 "Garnish with a lime slice optionally squeezing some lime juice inside",
                                 "Serve with chilled ice"],
                    "emphasize":{"procedure_1":["Ginger Beer","Vodka"],"procedure_2":["lime slice"]},
                    "next":"2"
                    }
            }

questions = {"1":{"id":"1",
                  "type":"drag and drop",
                  "question":"Drag the ingredients for a moscow mule into the shaker.",
                  "options":["Gin",
                            "Vodka",
                            "Soda Water",
                            "Lemon Juice",
                            "Ginger Beer",
                            "Lime Slice",
                            "Campari",
                            "Tequila"],
                    "answer":["Gin",
                            "Ginger Beer",
                            "Lime Slice",],
                    "next":"2"
                    },   
            "2":{"id":"2",
                  "type":"ratios",
                  "question":"Give the ingredient ratio in a Moscow Mule (garnishes have ratio of 0):",
                  "emphasize":{"Moscow Mule"},
                  "options":["Gin",
                            "Lime Slice",
                            "Ginger Beer"
                            ],
                    "answer":[2,0,1],
                    "next":"2"
                    }, 
            "3":{"id":"3",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Moscow Mule: (not all boxes must be used)",
                  "emphasize":{"Moscow Mule"},
                  "answer":{"Ginger Beer":"2",
                            "Lime Slice":"0",
                            "Gin":"0"}
                },            
            }

@app.route('/')
def welcome():
    return render_template("welcome.html")


@app.route('/renderQuestion/<questionId>', methods=['GET'])
def renderPlayer(questionId=None):
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