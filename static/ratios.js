function initialize(list){
  ingredients = list.options
  id = list.id
}

function updateScore(){
  hold = {}


  $.ajax({
      type: "GET",
      url: "/score",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(hold),
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
// render ingredients

function pushIngredients(){
  for(var i=0; i<ingredients.length; i++){
    addIngredients(i, ingredients[i])
  }
}

function addIngredients(index, object){
  let new_row = $('<div class="row">')
  let x = $("<div class='col-4'>" + object + "</div>")
  let y = $('<input type="text" placeholder="e.g. 3" id="'+index+'"></input><br>')
  $(new_row).append(x)
  $(new_row).append(y)

  $("#main_row").append(new_row)
}

// check answer
function buttonAnswer(){
  let button = $('<button class="btn-primary">Check answer</button>')
  $(button).click(function(){
    let submission = buildAnswer()
    check(submission)
    updateScore()
  })
  $("#answer").append(button)
}

function buildAnswer(){
  let submission = {}
  $.each(ingredients, function(index, object){
    submission[object] = $.trim( $("#"+index+"").val())
  })

  return submission
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

    $.each(ingredients, function(index2, object2){
      if(object2==object[0]){makeGreen(index2)}
    })
  })

  $.each(result["incorrect"], function(index, object){

    $.each(ingredients, function(index2, object2){
      if(object2==object[0]){makeRed(index2)}
    })
  })
}

function makeGreen(index){
  $("#"+index).css({'background-color':'lightgreen'})
}

function makeRed(index){
  $("#"+index).css({'background-color':'red'})
}

// on ready

$(document).ready(function(){
  updateScore()
  initialize(questionDetails)
  pushIngredients()
  buttonAnswer()

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
})
