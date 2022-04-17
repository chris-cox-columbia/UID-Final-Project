from server import check_drag_and_drop, check_ratios, check_free_form

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
