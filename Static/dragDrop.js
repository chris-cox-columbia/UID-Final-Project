var ingredients = [
  "gin",
  "vodka",
  "soda water",
  "lemon juice",
  "ginger beer",
  "lime slice",
  "tequila",
  "campari"
]

var drink = []

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
  $("#emptyIngredients").empty()
}

function emptyDrink(){
  $("#drink").empty()
}

// make dynamically draggable

$(document).on('mouseenter', '.drag', function(k) {
  var object = $(this)

  if(!object.is('.ui-draggable')) {
    object.draggable({revert: "invalid"})
  }
  // ALL CREDIT HERE: https://stackoverflow.com/questions/17941834/how-to-make-dynamically-added-list-elements-draggable-in-jquery
})


// on ready
$(document).ready(function(){
  pushIngredients()
  pushDrink()
})
