# WolfPal 2.0

## Introduction

There are hundreds of universities in North America and huge number of students pursuing advanced degrees in these universities. During the application phase, the students select certain universities based on the area of specialization and the courses offered in that field. So it would be unfair for the students if they do not get the right courses after taking admission due to lack of resources or lack of communication. 

Wolfpal, a course planning assistant, is a platform which aims to resolve these shortcomings and come up with a good course plan for the students. We have added new functionalities to this novel approach of course planning by applying latest techniques available.

### WolfPal 1.0

Wolfpal 1.0  was a highly efficient platform which had important functionalities like chatting with peers about the courses, average grades of previous batches, course structure. These parameters were judged accurately by experience of similar people and a chatting platform for the same serves the purpose. Moreover, the platform also had a bot functionality where in the students can get answers to certain queries related to planning of courses. The system also provided a list to the students for the course plan and also displayed course information from the course  catalog to the students.

### New Functionalities

The main aim of our new functionalities was to capture maximum students' interests, requirements and skills to suggest them a course plan.
* We added a functionality of suggesting courses by mapping course descriptions with keywords. We used Natural Language Processing techniques for the same.
* The course details are now extracted directly from the NCSU Course Catalog, thus replacing the earlier static database which was designed by manually entering the course details.
* Another functionality we added was a file uploader so that students could add syllabus of the courses for other users to view thereby giving the students more information about the courses.


## Steps to run the program
### Install python dependencies
```
pip install <PACKAGE_NAMES>
```
nltk,
pickle,
re


### Install gems
```
bundle install --without production
```

### Complete Database Migrations
```
rails db:migrate
```

### Populate database
```
rails db:seed
```

### Run server
```
rails server
```

Your app will run on http://localhost:3000


## Contributors

* **Neel Kapadia** - [neelkapadia](https://github.com/neelkapadia)
* **Rohan Chandavarkar** - [rohanchandavarkar](https://github.com/RohanChandavarkar)
* **Rohit Naik** - [rohitnaik246](https://github.com/rohitnaik246)
* **Sainag Shetty** - [sainagshetty](https://github.com/SainagShetty)
