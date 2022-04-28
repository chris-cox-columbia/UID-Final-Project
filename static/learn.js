function dialog_pop_up(){
      $("#extra_info_button").button().on( "click", function() {
            $("#dialog").dialog("open");
      });
      $("#dialog").dialog({
            autoOpen: false,
            modal: true,
            width: 500,
      })
}

function next_button_video(drinkInfo) {
      let next = drinkInfo.next
      $("#next_button_video").button().on("click", function () {
            if(next==""){
                  url = "/quiz/1"
            }
            else{
                  url = "/learn/intro/"+next
            }
            window.location.replace(url)
      });
}

function back_button_video() {
      $("#back_button_video").button().on("click", function () {
            url = "/learn/intro/" + drinkInfo.id
            window.location.replace(url)
      });
}

function next_button_intro() {
      $("#next_button_intro").button().on("click", function () {
            url = "/learn/video/" + drinkInfo.id
            window.location.replace(url)
      });
}

function back_button_intro(drinkInfo) {
      let id = drinkInfo.id
      $("#back_button_intro").button().on("click", function () {
            if(id=="1"){
                  url = "/"
            }
            else{
                  url = "/learn/video/"+(parseInt(id)-1).toString()
            }
            window.location.replace(url)
      });
}

function underline(){
      for (const [key, value] of Object.entries(drinkInfo.ingredient_list)) {
            console.log(key);
            $('#ingred_name_' + key).css("text_decoration", "underline");
            $('#ingred_name_' + key).css("text_decoration_color", drinkInfo.ingredient_details[value][0]);
      }
}

$(document).ready(function(){
      next_button_video(drinkInfo);
      back_button_video();
      next_button_intro();
      back_button_intro(drinkInfo);
      dialog_pop_up();
      underline();
})