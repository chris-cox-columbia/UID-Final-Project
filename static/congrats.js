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



$(document).ready(function(){
    updateScore();
})