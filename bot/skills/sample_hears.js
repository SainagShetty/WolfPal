/*

WHAT IS THIS?

This module demonstrates simple uses of Botkit's `hears` handler functions.

In these examples, Botkit is configured to listen for certain phrases, and then
respond immediately with a single line response.

*/
const fs = require('fs');

module.exports = function(controller) {

  function course_selection_help(convo){
    convo.ask("What is your area of interest?", function(response, convo){
      convo.say("Gotcha! Let me look for it.");
      convo.next();
      var res = response.text.toLowerCase();
      res = res.split(" ").join("_");
      var found_anything = false;
      var counter = 0;
      var dir = __dirname + "/data_files/";
      fs.readdirSync(dir).forEach(file => {
          console.log(file + " , " + res);
            if(file.search(res) >= 0 || res.search(file.substring(0, file.indexOf('.'))) >= 0){
              found_anything = true;
              var data = JSON.parse(fs.readFileSync(dir+file, 'utf-8'));
              console.log(data.courses);
              var courses = data.courses;
              courses.forEach(course => {
                convo.say(++counter + ". " + course.toString());
                convo.next();
              });
            }
      });
      counter = 0;
      if(!found_anything){
        convo.say("Uh oh! I don't know anything about this topic right now. Don't you worry, I'll update my database soon!");
      }else{
        convo.say("These are the courses that I could find related your area of interest.");
        convo.next();
        convo.say("Phewww! Had to dig deep to find the info. I hope it solved your purpose.");
      }
      convo.next();
    });
  }

    function ask_for_course_suggestion(convo){
      convo.ask("Need some course suggestions?", function(response, convo){
        convo.next();
        console.log(response.text);
        var agree = ['yes','please','i do', 'sure', 'why not'];
        var question = false;
        response = response.text.toLowerCase();
        agree.forEach(entry => {
          if(response.search(entry) >= 0){
            question = true;
          }
        });
        if(question){
          course_selection_help(convo);
        }else{
          convo.say("Cool!");
        }
      });
    }

    var greetings = ['hello', 'Hello', 'Hi', 'hi', 'Hola', 'hola', 'hey', 'Hey', 'greet', 'Greet'];
    controller.hears(greetings, 'direct_message,direct_mention', function(bot, message) {
        console.log(message.text);
        bot.startConversation(message, function(error, convo){
          console.log(message.text);
          convo.say("Hello there!");
          convo.next();
          if(message.text.search("course")>=0){
            convo.say("Absolutely!");
            convo.next();
            course_selection_help(convo);
          }else{
            ask_for_course_suggestion(convo);
          }
        });
    });

    controller.hears(['help','Help','HELP'], 'direct_message,direct_mention', function(bot, message){
      bot.startConversation(message, function(error, convo){
        convo.say("I can help you with the course selection.");
        convo.next();
        if(message.text.search("course")>=0){
          convo.say("Absolutely!");
          convo.next();
          course_selection_help(convo);
        }else{
          ask_for_course_suggestion(convo);
        }
      });
    });

    var response_to_thankyou = ["Happy to help!", "Glad I could help you!", "You're welcome!", "No problem!", "Don't mention it!"];
    controller.hears(['thank', 'Thank', 'appreciate', 'Appreciate'], 'direct_message,direct_mention', function(bot, message){
      bot.startConversation(message, function(error, convo){
        console.log(response_to_thankyou.length);
        var idx = Math.floor((Math.random())*(response_to_thankyou.length-0.1));
        console.log(idx);
        convo.say(response_to_thankyou[idx]);
        convo.next();
      });
    });
};
