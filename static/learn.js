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

function next_button_video() {
      $("#next_button_video").button().on("click", function () {
            url = "/"
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

function back_button_intro() {
      $("#back_button_intro").button().on("click", function () {
            url = "/"
            window.location.replace(url)
      });
}

$(document).ready(function(){
      next_button_video();
      back_button_video();
      next_button_intro();
      back_button_intro();
      dialog_pop_up();
})