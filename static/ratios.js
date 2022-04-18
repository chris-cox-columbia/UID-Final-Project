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
function displayAnswer(answer){
  $("#answer").empty()
  $("#answer").append("Correct: " + answer["correct"])
  $("#answer").append("Incorrect: " + answer["incorrect"])
}

// on ready

$(document).ready(function(){
  let next = questionDetails.next;
  console.log(next)
  $("#next_button").click(function(){
      console.log("hello next")
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
  $("#back_button").click(function(){
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

  initialize(questionDetails)
  pushIngredients()
  buttonAnswer()
})
