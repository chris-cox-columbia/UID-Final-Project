function initialize(list){
  ingredients = list
}

// render ingredients

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

  $("#main_row").append(x)
}

// on ready

$(document).ready(function(){
  initialize(questionDetails.options)
})
