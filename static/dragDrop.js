// var ingredients = [
//   "gin",
//   "vodka",
//   "soda water",
//   "lemon juice",
//   "ginger beer",
//   "lime slice",
//   "tequila",
//   "campari"
// ]

var drink = []

// initialize

function initialize(list){
  ingredients = list.options
  id = list.id
}

// Rendering ingredient options

function pushIngredients(){
  for(var i=0; i<ingredients.length; i++){
    addIngredients(ingredients[i])
  }
}

function addIngredients(object){
  var x = $("<div>")
  $(x).prop({
    class: "drag",
    id: object,
    innerHTML: object
  })

  $(x).attr({
    "data-name": object
  })

  $("#ingredientList").append(x)
}

// Rendering chosen ingredients

function pushDrink(){
  for(var i=0; i<drink.length; i++){
    addDrink(drink[i])
  }
}

function addDrink(object){
  var x = $("<div>")
  $(x).prop({
    class: "drag",
    id: object,
    innerHTML: object
  })

  $(x).attr({
    "data-name": object
  })

  $("#drink").append(x)
}

// clear div on drag

function emptyIngredients(){
  $("#ingredientList").empty()
}

function emptyDrink(){
  $("#drink").empty()
}

function remove(array, object){
  for(var i=0; i<array.length; i++){
    if(array[i] == object){
      array.splice(i,1)
    }
  }
}

// make dynamically draggable

$(document).on('mouseenter', '.drag', function(k) {
  var object = $(this)

  if(!object.is('.ui-draggable')) {
    object.draggable({revert: "invalid"})
  }
  // ALL CREDIT HERE: https://stackoverflow.com/questions/17941834/how-to-make-dynamically-added-list-elements-draggable-in-jquery
})

// check answers

function toString(answer){
  var newString = ""
  $.each(answer, function(index, object){
    newString += object + ","
  })

  return newString
}

function check(submission){

  var hold = {}
  hold.answer=toString(submission)

  $.ajax({
      type: "POST",
      url: "/quiz/"+id,
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(hold),
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

function displayAnswer(answer){
  $("#answer").empty()
  $("#answer").append("Correct: " + answer["correct"])
  $("#answer").append("Incorrect: " + answer["incorrect"])
  $("#answer").append("Missing: " + answer["missing"])
}

function buttonAnswer(){
  let button = $('<button class="btn-primary">Check answer</button>')
  $(button).click(function(){
    check(drink)
  })
  $("#answer").append(button)
}

// on ready
$(document).ready(function(){
  initialize(questionDetails)
  pushIngredients()
  pushDrink()
  console.log(questionDetails)

  $("#ingredientTarget").droppable({

    drop: function(event, ui){
      //MODEL
      var item = $(ui.draggable).data("name");
      ingredients.push(item)
      // DELETE FROM OLD LIST
      remove(drink, item)

      console.log("Unselecting: " + item)

      //VIEW
      emptyIngredients()
      emptyDrink()

      pushIngredients()
      pushDrink()
    }
  })

    $("#drinkTarget").droppable({

      drop: function(event, ui){
        //MODEL
        var item = $(ui.draggable).data("name");
        drink.push(item)
        // DELETE FROM OLD LIST
        remove(ingredients, item)

        console.log("Selecting: " + item)

        //VIEW
        emptyIngredients()
        emptyDrink()

        pushIngredients()
        pushDrink()
      }

  })
})
