
var drink = []

// initialize

function initialize(list){
  ingredients = list
}

// Rendering ingredient options

function pushIngredients(images){
  for(var i=0; i<ingredients.length; i++){
    addIngredients(ingredients[i], images)
  }
}

function addIngredients(object, images){
  let img = images[object]
  var x = $("<div>")
  let html = "<img src='../static/"+img+"' id='ingredienticon'><br>"

  $(x).prop({
    class: "drag col-3",
    id: object.replace(/\s/g, ""),
    innerHTML: html + object
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
  let img = images[object]
  var x = $("<div>")
  let html = "<img src='../static/"+img+"' id='ingredienticon'><br>"

  $(x).prop({
    class: "drag col-3",
    id: object.replace(/\s/g, ""),
    innerHTML: html + object
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


function updateScore(){
  $.ajax({
      type: "GET",
      url: "/score",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      success: function(result){
        console.log("Score: ", result)
        // change the text of the score id div
        $("#score").text(   result + "/10"  )
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

function check(submission, questionId){

  var hold = {}
  hold.answer=toString(submission)

  $.ajax({
      type: "POST",
      url: "/quiz/"+questionId,
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(hold),
      success: function(result){
        console.log(result)
        compare(result)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

function compare(result){
  $.each(result["correct"], function(index, object){
    makeGreen(object.replace(/\s/g, ""))
  })

  $.each(result["missing"], function(index, object){
    makeRed(object.replace(/\s/g, ""))
  })
}

function makeGreen(index){
  $("#"+index).css({'background-color':'#E7F2D6'})
}

function makeRed(index){
  $("#"+index).css({'background-color':'#F1CAB7'})
}

function buttonAnswer(questionId){
  let button = $('<button class="answer_button">CHECK ANSWER</button>')
  $(button).click(function(){
    check(drink, questionId)
    updateScore()
  })
  $("#answer").append(button)
}

// on ready
$(document).ready(function(){
  let questionId = questionDetails.id
  updateScore()
  initialize(questionDetails.options)
  pushIngredients(images)
  pushDrink()
  buttonAnswer(questionId)

  let next = questionDetails.next;
  $("#next_button").click(function(){
      if(next==""){
        let url='/congratulations'
        window.location.replace(url);
        }
      else{
        let url='/quiz/'+next
        window.location.replace(url);
      }
    })

  let id = questionDetails.id;
  $('#back_button').click(function(){
      if(id=="1"){
        let url = '/learn/video/3'
        window.location.replace(url);
      }
      else{
        let prev = (parseInt(id)-1).toString()
        let url = '/quiz/'+prev
        window.location.replace(url);
      }
    })



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

      pushIngredients(images)
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

        pushIngredients(images)
        pushDrink()
      }

  })
})
