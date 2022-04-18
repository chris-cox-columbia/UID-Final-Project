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
  var x = $("<div>" + object + "</div><br>")
  var y = $('<input type="text" placeholder="e.g. 3" id="'+object+'"></input><br>')
  $("#main_row").append(x)
  $("#main_row").append(y)
}

// on ready

$(document).ready(function(){
  initialize(questionDetails)
  pushIngredients()
})
