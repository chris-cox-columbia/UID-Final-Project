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
  let new_row = $('<div class="col-3" id="ingredient">')
  $(new_row).append("<div class='col-12'>Image</div>")
  $(new_row).append("<div class='col-12'>" + object + "</div>")
  $(new_row).append('<div class="col-12"><input type="text" class="textinput" placeholder="e.g. 3" id="'+index+'"></input><div>')

  // let z = $("<div class='col-4' id='ingredient'>" + object + "<input type='text' placeholder='e.g. 3' id='"+index+"'></input><br>" + "</div>")
  // $(new_row).append(z)


  $("#main_row").append(new_row)
}

// check answer
function buttonAnswer(){
  let button = $('<button class="answer_button">CHECK ANSWER</button>')
  $(button).click(function(){
    let submission = buildAnswer()
    check(submission)
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
  $("#"+index).css({'background-color':'#E7F2D6'})
}

function makeRed(index){
  $("#"+index).css({'background-color':'#F1CAB7'})
}

// on ready

$(document).ready(function(){
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
