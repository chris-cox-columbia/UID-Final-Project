from server import check_drag_and_drop, check_ratios, check_free_form
"""
 # check ratios example
questionId = "5"
user_answers = {
    "Grapefruit Soda": 5,
    "Rum":3,
    "Lime Juice":2,
    "Campari":1
    }
print(check_ratios(questionId, user_answers))

# check drag and drop example
questionId = "7"
user_answers = ["Olives", "Lime Juice", "Campari"]
print(check_drag_and_drop(questionId, user_answers))

# check free form example
questionId = "6"
print(check_free_form(questionId))
"""


import requests
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'answer':"Olives,Lime Juice,Campari"}

session = requests.Session()
print(session.post('http://127.0.0.1:5000/quiz/4',headers=headers,data=payload).text)


headers = {'User-Agent': 'Mozilla/5.0'}
payload = {
    "Grapefruit Soda": 5,
    "Rum":3,
    "Lime Juice":2,
    "Campari":1
    }

session = requests.Session()
print(session.post('http://127.0.0.1:5000/quiz/5',headers=headers,data=payload).text)
