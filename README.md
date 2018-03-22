# WolfPal: Your Planning Assistant
Software Engineering Project for Spring 2018

## Project Statement
- February Report [Here](https://github.com/ragarwa7/WolfPal/blob/master/Reports/team-k_wolfpal_feb_report.pdf)
- March Report[Here](https://github.com/ragarwa7/WolfPal/blob/master/Reports/team-k_wolfpal_mar_report.pdf)
- Edited on [ShareLatex](https://www.sharelatex.com/project/5a6fa9c8bcab1c4195f0a889)

We propose a system to propose a prospective graduate plan for a new student for enrolling into a new semester and helping increase communication between relevant peers for the courses. There is a lot of information available online which can help student make a well informed decision but this information is sparsely present. Due to the scattered presence,this information is sometimes hard to find which makes it ineffective. Additionally,  the  students  prefer  to  communicate with their peer who have information about a course.According to our survey, this technique was used by most ofthe students. The students also reported that sometimes itis hard to find peers with knowledge about a particular subject.  Also, the information about the events and activitiesare available on university’s website but still students do notknow about it due to scattered presence of every availablething.  In this paper, we propose a solution of tackling thesetwo problems - lack of information and lack of communication.

## Steps to Run App

1. Sign up for using the application.
2. Interact with the bot to begin your plan evaluation. 
3. Choose the graduate track which interest you. 
4. Choose the courses which interest you. An appropriate graduate plan will be suggested to you based on these choices. 
5. Choose the graduate plan that suits you most perfectly. 
6. Once your courses are finalized, you have the option to open the unique forum for a specific course, as well as a forum which is completely general. You can access different elements of the forum using keywords pertaining to a specific topic. 

# About WolfPal Chatbot
User can always find a red `Contact WolfPal` button on the bottom right of the page. Click it to open the chat window to chat with our chatbot, and close it by click `X` button on the top right of the chat window. This bot contains three categories of questions and answers that we think users might ask frequently. The following section shows how to use this bot.

## 1. First time use it.
The bot asks questions about users `area of interest`, `undergrad GPA`, and `confidence of project`. Based on users answers, it can give the user some suggestion for course selection. Those questions will only ask for the first time. However, users can change `area of interest` if needs.

## 2. Three category
The three categories of questions and answers are `Suggest course`, `Course detail` and `About me`. 2.1 to 2.3 shows the use cases of those categories.

### 2.1. Suggest course
<Details>
In this category, there is two kind of information a user can get, and users can change their interest subject here

- One information the user can get is `the list of courses` that related to your interest subject(see the following figure).

![alt text](https://github.com/ragarwa7/WolfPal/blob/bot_new/images/related.PNG)

- The other information is recommends courses by difficulty. The function of difficulty is counted by the score of workload and users information. We assign four constants on each courses according to last years data, which are represent `core`, `assignment`, `exam`, and `project` workload. Compare with users GPA and the ability of project, the bot will recommend 4 courses that it's easiest for a user(see the following figure).

![alt text](https://github.com/ragarwa7/WolfPal/blob/bot_new/images/recommend.PNG)

- Click `Change interest subject` can change interest subject. The acceptable subjects for our current bots are,
    - Data Science
    - Software Engineering
    - Algorithm
    - Application
    - System
    - Software Security
    
![alt text](https://github.com/ragarwa7/WolfPal/blob/bot_new/images/changeAoi.PNG)
</Details>

### 2.2.Course detail
<Details>
In this category, the bot will return `Average grade` and `Prerequisites` for the course.

![alt text](https://github.com/ragarwa7/WolfPal/blob/bot_new/images/detail.PNG)
</Details>

### 2.3. About me
<Details>
We want the bot has ability to guide the user how to use WolfPal. Right now, it give the hyperlink of our github page. Therefore, a user can find explanation and use cases on `readMe` page, and create issues to report bugs or ask questions.
</Details>