function initialize(list){
  ingredients = list.options
}

// render ingredients

function pushIngredients(){
  for(var i=0; i<ingredients.length; i++){
    addIngredients(ingredients[i])
  }
}

function addIngredients(object){
  var x = $("<div>" + object + "</div>")
  $("#main_row").append(x)
}

// on ready

$(document).ready(function(){
  initialize(questionDetails)
})
