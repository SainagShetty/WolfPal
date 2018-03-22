/*
* The structure of chat bot is reference form "tscok"
* code( http://jsfiddle.net/tscok/0jyu98L2/ )
*/

var Chat = function() {
    //var dataSearch = new DataSearch();
    var messages = {};
    var topic = "";//input switch
    var subject = ""; //execute on "other" topic
    var profile = {};
    var dataSearch = {};
    var recommend = {};
    var buttonId = 0;

    function loadJSON() {

        profile ={
          "interest": {
            "question": "What is your area of interest?",
            "answer": ""
          },
          "ugg": {
            "question": "What was your grade in undergrad? (0-4)",
            "answer": ""
          },
          "project": {
            "question": "How you grade yourself in completing projects successfully? (0-5)",
            "answer": ""
          }
        }
        //profile = JSON.parse(profiledata);
        // var xobj = new XMLHttpRequest();
        // //xobj.overrideMimeType("application/json");
        // xobj.open('GET', 'assets/profile.json'); // Replace 'my_data' with the path to your file
        // xobj.responseType = 'json';
        // xobj.send();
        // xobj.onreadystatechange = (profile = function() {
        //     if (xobj.readyState == 4 && xobj.status == "200") {
        //         profile = xobj.response;
        //         return profile;
        //     }
        // });
    }

    function outputButton(text, id, delay){
        var delay = delay || 0;
        var b = document.createElement('BUTTON');
        //b.appendChild(document.createTextNode(text));
        b.className = 'button';
        b.innerHTML = text;
        b.setAttribute("id", id);
        b.setAttribute("name", id+buttonId);
        b.setAttribute("onClick", "Chat.pressedButton(this.id)");
        setTimeout(function(){
            messages.appendChild(b);
            // var objDiv = document.getElementById("chatText");
            // objDiv.scrollTop = objDiv.scrollHeight;
            messages.scrollTop = messages.scrollHeight;
        },delay);
    }

    function pressedButton(id){
        //alert("Button pressed: " + document.getElementById(id).innerHTML);
        document.getElementsByName("input")[0].setAttribute("contenteditable", "true");
        document.getElementsByName(id+(buttonId-1))[0].setAttribute("style", "background:  #888  ;");
        topic = id;
        switch(topic){
            case "suggest_course":
                getAoI();
                break;
            case "course_detail":
                getCourse();
                break;
            case "change_AOI":
                getAoI();
                break;
            case "about_me":
                aboutMe();
                break;
            case "recommend":
                suggestion();
                talk();
                break;
            case "related":
                output("The courses related to " + subject + " are: " , true);
                var list = dataSearch.makeCourseList_name(subject);
                var index = 0;
                for( let x of list){
                    output(++index + ". " + dataSearch.getCourseName(x), true);
                    sleep(75);
                }
                talk();
                break;
            default:
                output(id, true, 500);
                talk();
        }
    }

    function output(text, bot, delay) {
        var bot = bot || false;
        var delay = delay || 0;
        var message = document.createElement('div');
        message.className = bot ? 'message bot' : 'message';
        message.innerHTML = text;

        //animate
        setTimeout(function(){
            messages.appendChild(message);
            var objDiv = document.getElementById("chatText");
            objDiv.scrollTop = objDiv.scrollHeight;
        }, delay);
    }

    function how2recommend() {
        document.getElementsByName("input")[0].setAttribute("contenteditable", "false");
        output("Your chosen subject is \'" + subject + "\', what do you want to know?", true, 500);
        outputButton("List of courses related to the subject", "related", 500);
        outputButton("Recommend courses", "recommend", 500);
        outputButton("Change interest subject", "change_AOI", 500);
        buttonId++;
    }

    function input(evt) {
        switch (evt.which) {
            case 13:
                evt.preventDefault();
                output(evt.target.innerHTML, false);
                handleInput(evt.target.innerHTML);
                evt.target.innerHTML = '';
                break;
        }
    }

    function handleInput(input) {
        while(input.includes('&nbsp')){
            input = input.replace('&nbsp;', '');
        }
        input = input.toLowerCase();
        console.log(input);
        switch(topic){
            case "ugg":
                if ( input>=0 && input<=4)
                    profile.ugg.answer = input;
                else
                    output("Number must between 0 and 4.", true);
                talk();
                break;
            case "project":
                if (input>=0 && input<=5) {
                    profile.project.answer = input;
                    recommend.setProfile(profile.interest.answer, profile.ugg.answer, profile.project.answer);
                }
                else
                    output("Number must between 0 and 5.", true);
                talk();
                break;
            // case "suggest_course":
            //     suggestion(input);
            //     break;
            case "aoi":
                setSubject(input);
                break;
            case "course_detail":
                console.log(input);
                detail(input);
                talk();
                break;
        }

    }

    function talk() {
        if (profile.ugg.answer === ""){
            topic = "ugg";
            requiredUgg();
        }
        else if (profile.project.answer === ""){
            topic = "project";
            requiredPro();
        }
        else {
            topic = "other";
            setTimeout(function(){
                other();
            }, 1000);
        }
    }

    function other() {
        document.getElementsByName("input")[0].setAttribute("contenteditable", "false");
        output("Pick one category below in which you need help", 500);
        outputButton("Suggest Course", "suggest_course",500);
        outputButton("Course Detail", "course_detail",500);
        outputButton("About me", "about_me", 500);
        buttonId++;
    }

    function requiredInt() {
        var question = profile.interest.question;
        output(question, true, 500);
    }

    function requiredUgg() {
        var question = profile.ugg.question;
        output(question, true, 500);
    }

    function requiredPro() {
        var question = profile.project.question;
        output(question, true, 500);
    }

    function getSubject(input){
        //let subject = "";
        if (input.includes("data science"))
            subject = "data science";
        else if (input.includes("software engineering"))
            subject = "software engineering";
        else if (input.includes("algorithm"))
            subject = "algorithm";
        else if (input.includes("application"))
            subject = "application";
        else if (input.includes("system"))
            subject = "system";
        else if (input.includes("software security"))
            subject = "software security";
    }

    function setSubject(input){
        //var subject = "";
        if (input.includes("data science")) {
            subject = "data science";
        }
        else if (input.includes("software engineering"))
            subject = "software engineering";
        else if (input.includes("algorithm"))
            subject = "algorithm";
        else if (input.includes("application"))
            subject = "application";
        else if (input.includes("system"))
            subject = "system";
        else if (input.includes("software security"))
            subject = "software security";
        else
            output("Sorry, can't find courses related to this subject.", true, 500);
        how2recommend();
    }

    function getCourse(){
        output("Enter course name(ex. Data Structures) or code(ex. csc540).", true, 500);
    }

    function getAoI(){
        topic = "aoi";
        output("Can you tell me your area of interest?", true, 500);
    }

    function suggestion(input) {
        //getSubject(input);

        if (subject !== "") {
            //output("The courses related to " + subject + " is: " , true);
            //output( dataSearch.makeCourseList_name(subject) , true);
            //setTimeout(function(){
            output("Top 4 recommendations for you is: ", true, 500);
            let print = recommend.makeRecommend(subject);
            for (let p of print) {
                output(p, true, 550);
            }
            //}, 500);
        }
        else
            output("Sorry, can't find courses related to this subject.", true, 500);
    }

    function detail(input) {
        var courseId = dataSearch.getCourseId(input.trim());
        if (courseId <0)
            output("Sorry, can't find this course, please try another course name", true, 500 );
        else {
            var courseAverage = (courseId === -1) ? -1 : dataSearch.getCourseAverage(courseId);
            output(" ''" + dataSearch.getCourseName(courseId)+ "'' ", true, 500);
            var string = "Average grade on last year is: " + courseAverage;
            output(string, true, 500);

            var coursePrereq = dataSearch.getCoursePrereq(courseId);
            if (coursePrereq !== null) {
                string = "The prerequisites are: " + coursePrereq;
                output(string, true, 500);
            }
        }
    }

    function aboutMe(){
        output("<a href=\"https://github.com/ragarwa7/WolfPal\">See details on project github page</a>",true);
        talk();
    }

    function init() {
        output('Hey pal, I can help you with course selection, if you tell me a bit about yourself.', true);
        messages = document.querySelector('.messages');
        setTimeout(function(){
          loadJSON();
          setTimeout(function(){
            recommend = new Recommend();
            dataSearch = new DataSearch();
          }, 250);
          setTimeout(function(){
            talk();
          }, 1000);
        }, 0);
    }

    function sleep(ms){
        var start_time = new Date().getTime();
        while((new Date().getTime() - start_time) < ms){}
    }

    return {
        init: init,
        input: input,
        pressedButton: pressedButton
    }

}();

function myfun(){
  setTimeout(function(){
      Chat.init();
  },500);
}

myfun();
