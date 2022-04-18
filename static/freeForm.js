function getInformation(input, studentAnswers){
    let ingredient = $("#ing"+input.toString()).val()
    let ratio = $("#rat"+input.toString()).val()
    let info = {'ing':ingredient,'rat':ratio}
    if((ingredient == '' || ingredient == undefined) && (ratio == '' || ratio == undefined)){
        makeRowColor(input,'white');
        return false}
    else{
        studentAnswers[ingredient]=ratio
        return info
    }
}

function makeRowColor(i, color){
    $("#ing"+i.toString()).css({'background-color':color});
    $("#rat"+i.toString()).css({'background-color':color});
}

function makeRatioRed(i){
        $("#ing"+i.toString()).css({'background-color':'lightgreen'});
        $("#rat"+i.toString()).css({'background-color':'lightpink'});
}


function checkAnswer(ingredient, ratio, answer,i){
    if (!(ingredient in answer)){
        makeRowColor(i, 'lightpink');
        return false
    }
    else{
        let suggestedRatio = answer[ingredient]
        if(suggestedRatio!=ratio){
            makeRatioRed(i);
            return false
        }
        else{
            makeRowColor(i,'lightgreen');
            return true
        }
    }

}


function sendAnswerToDb(studentAnswers, id){
    let answerObj = {}
    answerObj["id"]=id
    answerObj["answer"] = studentAnswers
    $.ajax({
        type: "POST",
            url: "http://127.0.0.1:5000/studentAnswers",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(answerObj),
            success: function(result){
                console.log(result);
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
        }
    })

}

$(document).ready(function(){
    let studentAnswers = {}
    let answer = questionDetails.answer
    let qid = questionDetails.id

    let lenCorrectAnswer = Object.keys(answer).length

    $("#submit").click(function(){
        let correctAnswers = 0
        let incorrectAnswers = 0
        for (let i=0; i<5; i++){
            let info = getInformation(i, studentAnswers);
            if (info != false){
                let ing = info.ing
                let rat = info.rat
                let correctEntry = checkAnswer(ing,rat,answer,i)
                if(correctEntry){
                    correctAnswers++
                }
                else{
                    incorrectAnswers++
                }
            }
        }
        if(correctAnswers==lenCorrectAnswer && incorrectAnswers==0){
            $("#feedback").text("Congrats you are correct");
            sendAnswerToDb(studentAnswers,qid);
        }
        else{
            $("#feedback").text("You got this wrong");
            sendAnswerToDb(studentAnswers,qid);
        }
        console.log(studentAnswers)
    })

    $("#clear").click(function(){
        for (let i=0; i<5; i++){
            $("#ing"+i.toString()).val("")
            $("#rat"+i.toString()).val("")
            makeRowColor(i,'white');
            $("#feedback").text("");
        }
        sendAnswerToDb({},qid);
    })
})