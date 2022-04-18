function initialize(list){
  ingredients = list.options
  id = list.id
}

// render ingredients

function pushIngredients(){
  for(var i=0; i<ingredients.length; i++){
    addIngredients(i, ingredients[i])
  }
}

function addIngredients(index, object){
  var x = $("<div>" + object + "</div><br>")
  var y = $('<input type="text" placeholder="e.g. 3" id="'+index+'"></input><br>')
  $("#main_row").append(x)
  $("#main_row").append(y)
}

// check answer
function buttonAnswer(){
  let button = $('<button class="btn-primary">Check answer</button>')
  $(button).click(function(){
    let answer = buildAnswer()
    check(answer)
  })
  $("#answer").append(button)
}

function buildAnswer(){
  let answer = {}
  $.each(ingredients, function(index, object){
    answer[object] = $.trim( $("#"+index+"").val())
  })

  return answer
}

function check(submission){

  $.ajax({
      type: "POST",
      url: "/quiz/"+id,
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(submission),
      success: function(result){
        console.log(result)
        displayAnswer(result)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

// display answers
function displayAnswer(result){
  $("#answer").empty()
  $("#answer").append("Correct: " + answer["correct"])
  $("#answer").append("Incorrect: " + answer["incorrect"])
}

// on ready

$(document).ready(function(){
  initialize(questionDetails)
  pushIngredients()
  buttonAnswer()
})
