class DataSearch{
    constructor(){
        console.log("DataSearch constructor started.")
        this.category = {
          "DSC": [16],
          "SEC": [1],
          "ALG": [9,10,15,17,32,33],
          "APP": [13,22,23,24,25],
          "SYS": [11,12,14,18,19,20,21,22],
          "SS": [2,3,4,5],
          "SF": [6,7,8,9,10,11,12,13,14]
        };

        this.workload = [
            {
              "id": 1,
              "syllabus_id": 1,
              "core": 1,
              "assignments": 1,
              "exams": 1,
              "project": 2,
              "created_at": "2018-03-03 19:08:09.201902",
              "updated_at": "2018-03-03 19:08:09.201902"
            },
            {
              "id": 2,
              "syllabus_id": 15,
              "core": 1,
              "assignments": 2,
              "exams": 2,
              "project": 0,
              "created_at": "2018-03-03 19:08:09.249027",
              "updated_at": "2018-03-03 19:08:09.249027"
            },
            {
              "id": 3,
              "syllabus_id": 9,
              "core": 1,
              "assignments": 2,
              "exams": 2,
              "project": 0,
              "created_at": "2018-03-03 19:08:09.292185",
              "updated_at": "2018-03-03 19:08:09.292185"
            },
            {
              "id": 4,
              "syllabus_id": 10,
              "core": 0,
              "assignments": 2,
              "exams": 1.5,
              "project": 0,
              "created_at": "2018-03-03 19:08:09.337326",
              "updated_at": "2018-03-03 19:08:09.337326"
            },
            {
              "id": 5,
              "syllabus_id": 11,
              "core": 1,
              "assignments": 0.5,
              "exams": 1.5,
              "project": 1.5,
              "created_at": "2018-03-03 19:08:09.380505",
              "updated_at": "2018-03-03 19:08:09.380505"
            }
          ];

        this.average = [
            {
              "id": 150,
              "A": 20,
              "B": 13,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.821164",
              "updated_at": "2018-03-03 19:08:07.821164",
              "syllabus_id": 1
            },
            {
              "id": 151,
              "A": 56,
              "B": 15,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.848643",
              "updated_at": "2018-03-03 19:08:07.848643",
              "syllabus_id": 2
            },
            {
              "id": 152,
              "A": 27,
              "B": 8,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.875139",
              "updated_at": "2018-03-03 19:08:07.875139",
              "syllabus_id": 3
            },
            {
              "id": 153,
              "A": 9,
              "B": 0,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.904578",
              "updated_at": "2018-03-03 19:08:07.904578",
              "syllabus_id": 4
            },
            {
              "id": 154,
              "A": 21,
              "B": 4,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.935980",
              "updated_at": "2018-03-03 19:08:07.935980",
              "syllabus_id": 5
            },
            {
              "id": 155,
              "A": 14,
              "B": 9,
              "C": 3,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:07.968382",
              "updated_at": "2018-03-03 19:08:07.968382",
              "syllabus_id": 6
            },
            {
              "id": 156,
              "A": 29,
              "B": 11,
              "C": 3,
              "D": 0,
              "Other": 4,
              "created_at": "2018-03-03 19:08:08.098883",
              "updated_at": "2018-03-03 19:08:08.098883",
              "syllabus_id": 7
            },
            {
              "id": 157,
              "A": 77,
              "B": 6,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.141081",
              "updated_at": "2018-03-03 19:08:08.141081",
              "syllabus_id": 8
            },
            {
              "id": 158,
              "A": 33,
              "B": 10,
              "C": 2,
              "D": 1,
              "Other": 4,
              "created_at": "2018-03-03 19:08:08.173463",
              "updated_at": "2018-03-03 19:08:08.173463",
              "syllabus_id": 9
            },
            {
              "id": 159,
              "A": 53,
              "B": 24,
              "C": 4,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.204867",
              "updated_at": "2018-03-03 19:08:08.204867",
              "syllabus_id": 10
            },
            {
              "id": 160,
              "A": 49,
              "B": 51,
              "C": 4,
              "D": 2,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.239213",
              "updated_at": "2018-03-03 19:08:08.239213",
              "syllabus_id": 11
            },
            {
              "id": 161,
              "A": 25,
              "B": 4,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.272617",
              "updated_at": "2018-03-03 19:08:08.272617",
              "syllabus_id": 12
            },
            {
              "id": 162,
              "A": 32,
              "B": 8,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.317720",
              "updated_at": "2018-03-03 19:08:08.317720",
              "syllabus_id": 13
            },
            {
              "id": 163,
              "A": 12,
              "B": 3,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.396232",
              "updated_at": "2018-03-03 19:08:08.396232",
              "syllabus_id": 14
            },
            {
              "id": 164,
              "A": 110,
              "B": 73,
              "C": 9,
              "D": 2,
              "Other": 2,
              "created_at": "2018-03-03 19:08:08.469827",
              "updated_at": "2018-03-03 19:08:08.469827",
              "syllabus_id": 15
            },
            {
              "id": 165,
              "A": 57,
              "B": 50,
              "C": 6,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.502211",
              "updated_at": "2018-03-03 19:08:08.502211",
              "syllabus_id": 16
            },
            {
              "id": 166,
              "A": 29,
              "B": 2,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.534594",
              "updated_at": "2018-03-03 19:08:08.534594",
              "syllabus_id": 17
            },
            {
              "id": 167,
              "A": 35,
              "B": 13,
              "C": 12,
              "D": 4,
              "Other": 1,
              "created_at": "2018-03-03 19:08:08.580718",
              "updated_at": "2018-03-03 19:08:08.580718",
              "syllabus_id": 18
            },
            {
              "id": 168,
              "A": 15,
              "B": 15,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.619971",
              "updated_at": "2018-03-03 19:08:08.619971",
              "syllabus_id": 19
            },
            {
              "id": 169,
              "A": 37,
              "B": 5,
              "C": 2,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.648429",
              "updated_at": "2018-03-03 19:08:08.648429",
              "syllabus_id": 20
            },
            {
              "id": 170,
              "A": 3,
              "B": 8,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.671001",
              "updated_at": "2018-03-03 19:08:08.671001",
              "syllabus_id": 21
            },
            {
              "id": 171,
              "A": 22,
              "B": 5,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.692609",
              "updated_at": "2018-03-03 19:08:08.692609",
              "syllabus_id": 22
            },
            {
              "id": 172,
              "A": 6,
              "B": 3,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.714179",
              "updated_at": "2018-03-03 19:08:08.714179",
              "syllabus_id": 23
            },
            {
              "id": 173,
              "A": 9,
              "B": 2,
              "C": 2,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.739695",
              "updated_at": "2018-03-03 19:08:08.739695",
              "syllabus_id": 24
            },
            {
              "id": 174,
              "A": 59,
              "B": 1,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.764228",
              "updated_at": "2018-03-03 19:08:08.764228",
              "syllabus_id": 25
            },
            {
              "id": 175,
              "A": 9,
              "B": 3,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.788760",
              "updated_at": "2018-03-03 19:08:08.788760",
              "syllabus_id": 26
            },
            {
              "id": 176,
              "A": 17,
              "B": 3,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.812312",
              "updated_at": "2018-03-03 19:08:08.812312",
              "syllabus_id": 27
            },
            {
              "id": 177,
              "A": 16,
              "B": 8,
              "C": 3,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.836847",
              "updated_at": "2018-03-03 19:08:08.836847",
              "syllabus_id": 28
            },
            {
              "id": 178,
              "A": 103,
              "B": 33,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.859417",
              "updated_at": "2018-03-03 19:08:08.859417",
              "syllabus_id": 29
            },
            {
              "id": 179,
              "A": 4,
              "B": 3,
              "C": 1,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.883950",
              "updated_at": "2018-03-03 19:08:08.883950",
              "syllabus_id": 30
            },
            {
              "id": 180,
              "A": 63,
              "B": 0,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.910446",
              "updated_at": "2018-03-03 19:08:08.910446",
              "syllabus_id": 31
            },
            {
              "id": 181,
              "A": 39,
              "B": 1,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.939949",
              "updated_at": "2018-03-03 19:08:08.939949",
              "syllabus_id": 32
            },
            {
              "id": 182,
              "A": 7,
              "B": 6,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.961474",
              "updated_at": "2018-03-03 19:08:08.961474",
              "syllabus_id": 33
            },
            {
              "id": 183,
              "A": 37,
              "B": 0,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:08.995821",
              "updated_at": "2018-03-03 19:08:08.995821",
              "syllabus_id": 34
            },
            {
              "id": 184,
              "A": 11,
              "B": 5,
              "C": 0,
              "D": 0,
              "Other": 0,
              "created_at": "2018-03-03 19:08:09.030170",
              "updated_at": "2018-03-03 19:08:09.030170",
              "syllabus_id": 35
            }
          ];

        this.course = [
            {
              "id": 36,
              "code": "CSC510",
              "syllabus_id": 1,
              "prerequisites": "Discrete Maths; Data Structures",
              "course_name": "Software Engineering",
              "core": true,
              "channel_id": 1,
              "created_at": "2018-02-21 19:35:14.354210",
              "updated_at": "2018-02-21 19:35:14.354210"
            },
            {
              "id": 37,
              "code": "CSC515",
              "syllabus_id": 2,
              "prerequisites": "Software Engineering",
              "course_name": "Software Security",
              "core": false,
              "channel_id": 2,
              "created_at": "2018-02-21 19:35:14.378345",
              "updated_at": "2018-02-21 19:35:14.378345"
            },
            {
              "id": 38,
              "code": "CSC519",
              "syllabus_id": 3,
              "prerequisites": "Software Engineering",
              "course_name": "DevOps",
              "core": false,
              "channel_id": 3,
              "created_at": "2018-02-21 19:35:14.400445",
              "updated_at": "2018-02-21 19:35:14.400445"
            },
            {
              "id": 39,
              "code": "CSC710",
              "syllabus_id": 4,
              "prerequisites": "Software Engineering",
              "course_name": "Software Engineering as a human activity",
              "core": false,
              "channel_id": 4,
              "created_at": "2018-02-21 19:35:14.428526",
              "updated_at": "2018-02-21 19:35:14.428526"
            },
            {
              "id": 40,
              "code": "CSC712",
              "syllabus_id": 5,
              "prerequisites": "Software Engineering",
              "course_name": "Software Testing and Reliability",
              "core": false,
              "channel_id": 5,
              "created_at": "2018-02-21 19:35:14.451633",
              "updated_at": "2018-02-21 19:35:14.451633"
            },
            {
              "id": 41,
              "code": "CSC503",
              "syllabus_id": 6,
              "prerequisites": "Automata, Grammar and Computability",
              "course_name": "Computational Applied Logic",
              "core": true,
              "channel_id": 6,
              "created_at": "2018-02-21 19:35:14.474694",
              "updated_at": "2018-02-21 19:35:14.474694"
            },
            {
              "id": 42,
              "code": "CSC512",
              "syllabus_id": 7,
              "prerequisites": "Automata, Grammar; Data Structures",
              "course_name": "Compiler Construction",
              "core": true,
              "channel_id": 7,
              "created_at": "2018-02-21 19:35:14.498818",
              "updated_at": "2018-02-21 19:35:14.498818"
            },
            {
              "id": 43,
              "code": "CSC517",
              "syllabus_id": 8,
              "prerequisites": "UG Software Engineering",
              "course_name": "Object Oriented Design and Development",
              "core": false,
              "channel_id": 8,
              "created_at": "2018-02-21 19:35:14.522473",
              "updated_at": "2018-02-21 19:35:14.522473"
            },
            {
              "id": 44,
              "code": "CSC520",
              "syllabus_id": 9,
              "prerequisites": "Discrete Maths; Data Structures",
              "course_name": "Artificial Intelligence",
              "core": true,
              "channel_id": 9,
              "created_at": "2018-02-21 19:35:14.546538",
              "updated_at": "2018-02-21 19:35:14.546538"
            },
            {
              "id": 45,
              "code": "CSC522",
              "syllabus_id": 10,
              "prerequisites": "Discrete Maths; Data Structures",
              "course_name": "Automated Learning and Data Analysis",
              "core": false,
              "channel_id": 10,
              "created_at": "2018-02-21 19:35:14.569600",
              "updated_at": "2018-02-21 19:35:14.569600"
            },
            {
              "id": 46,
              "code": "CSC540",
              "syllabus_id": 11,
              "prerequisites": "Data Structures",
              "course_name": "Database Management concepts and Systems",
              "core": true,
              "channel_id": 11,
              "created_at": "2018-02-21 19:35:14.594665",
              "updated_at": "2018-02-21 19:35:14.594665"
            },
            {
              "id": 47,
              "code": "CSC547",
              "syllabus_id": 12,
              "prerequisites": "Operating Systems; Computer Networks",
              "course_name": "Cloud Computing Technology",
              "core": false,
              "channel_id": 12,
              "created_at": "2018-02-21 19:35:14.617726",
              "updated_at": "2018-02-21 19:35:14.617726"
            },
            {
              "id": 48,
              "code": "CSC554",
              "syllabus_id": 13,
              "prerequisites": "Data Structures",
              "course_name": "Human-Computer Interaction",
              "core": false,
              "channel_id": 13,
              "created_at": "2018-02-21 19:35:14.641823",
              "updated_at": "2018-02-21 19:35:14.641823"
            },
            {
              "id": 49,
              "code": "CSC750",
              "syllabus_id": 14,
              "prerequisites": "Database Management concepts and Systems",
              "course_name": "Service Oriented Computing",
              "core": false,
              "channel_id": 14,
              "created_at": "2018-02-21 19:35:14.665378",
              "updated_at": "2018-02-21 19:35:14.665378"
            },
            {
              "id": 50,
              "code": "CSC505",
              "syllabus_id": 15,
              "prerequisites": "Discrete Maths; Data Structures",
              "course_name": "Design and Analysis of Algorithms",
              "core": true,
              "channel_id": 15,
              "created_at": "2018-02-21 19:35:14.689442",
              "updated_at": "2018-02-21 19:35:14.689442"
            },
            {
              "id": 51,
              "code": "CSC591F",
              "syllabus_id": 16,
              "prerequisites": null,
              "course_name": "Foundations of Data Science",
              "core": false,
              "channel_id": 16,
              "created_at": "2018-02-21 19:35:14.712441",
              "updated_at": "2018-02-21 19:35:14.712441"
            },
            {
              "id": 52,
              "code": "CSC591S",
              "syllabus_id": 17,
              "prerequisites": null,
              "course_name": "Spatial and Temporal Data Mining",
              "core": false,
              "channel_id": 17,
              "created_at": "2018-02-21 19:35:14.736535",
              "updated_at": "2018-02-21 19:35:14.736535"
            },
            {
              "id": 53,
              "code": "CSC541",
              "syllabus_id": 18,
              "prerequisites": "Data Structures",
              "course_name": "Advanced Data Structures",
              "core": false,
              "channel_id": 18,
              "created_at": "2018-02-21 19:35:14.758614",
              "updated_at": "2018-02-21 19:35:14.758614"
            },
            {
              "id": 54,
              "code": "CSC548",
              "syllabus_id": 19,
              "prerequisites": "UG Operating Systems Principles",
              "course_name": "Parallel Systems",
              "core": false,
              "channel_id": 19,
              "created_at": "2018-02-21 19:35:14.783948",
              "updated_at": "2018-02-21 19:35:14.783948"
            },
            {
              "id": 55,
              "code": "CSC591D",
              "syllabus_id": 20,
              "prerequisites": null,
              "course_name": "Data Intensive Computing",
              "core": false,
              "channel_id": 20,
              "created_at": "2018-02-21 19:35:14.807079",
              "updated_at": "2018-02-21 19:35:14.807079"
            },
            {
              "id": 56,
              "code": "CSC742",
              "syllabus_id": 21,
              "prerequisites": "Advanced Data Structures",
              "course_name": "Database Management Systems",
              "core": false,
              "channel_id": 21,
              "created_at": "2018-02-21 19:35:14.830301",
              "updated_at": "2018-02-21 19:35:14.830301"
            },
            {
              "id": 57,
              "code": "CSC724",
              "syllabus_id": 22,
              "prerequisites": "Operating Systems Principles",
              "course_name": "Advanced Distributed Systems",
              "core": false,
              "channel_id": 22,
              "created_at": "2018-02-21 19:35:14.854749",
              "updated_at": "2018-02-21 19:35:14.854749"
            },
            {
              "id": 58,
              "code": "CSC530",
              "syllabus_id": 23,
              "prerequisites": "Data Structures; Algorithms",
              "course_name": "Computational Methods for Molecular Biology",
              "core": false,
              "channel_id": 23,
              "created_at": "2018-02-21 19:35:14.879841",
              "updated_at": "2018-02-21 19:35:14.879841"
            },
            {
              "id": 59,
              "code": "CSC555",
              "syllabus_id": 24,
              "prerequisites": null,
              "course_name": "Social Computing",
              "core": false,
              "channel_id": 24,
              "created_at": "2018-02-21 19:35:14.902902",
              "updated_at": "2018-02-21 19:35:14.902902"
            },
            {
              "id": 60,
              "code": "CSC561",
              "syllabus_id": 25,
              "prerequisites": null,
              "course_name": "Principles of Computer Graphics",
              "core": true,
              "channel_id": 25,
              "created_at": "2018-02-21 19:35:14.926968",
              "updated_at": "2018-02-21 19:35:14.926968"
            },
            {
              "id": 61,
              "code": "CSC591E",
              "syllabus_id": 26,
              "prerequisites": null,
              "course_name": "Educational Data Mining",
              "core": false,
              "channel_id": 26,
              "created_at": "2018-02-21 19:35:14.949909",
              "updated_at": "2018-02-21 19:35:14.949909"
            },
            {
              "id": 62,
              "code": "CSC565",
              "syllabus_id": 27,
              "prerequisites": "Discrete Maths",
              "course_name": "Graph Theory",
              "core": true,
              "channel_id": 27,
              "created_at": "2018-02-21 19:35:14.975008",
              "updated_at": "2018-02-21 19:35:14.975008"
            },
            {
              "id": 63,
              "code": "CSC580",
              "syllabus_id": 28,
              "prerequisites": null,
              "course_name": "Numerical Analysis",
              "core": true,
              "channel_id": 28,
              "created_at": "2018-02-21 19:35:15.000045",
              "updated_at": "2018-02-21 19:35:15.000045"
            },
            {
              "id": 64,
              "code": "CSC501",
              "syllabus_id": 29,
              "prerequisites": "UG Operating Systems Principles",
              "course_name": "Operating Systems Principles",
              "core": true,
              "channel_id": 29,
              "created_at": "2018-02-21 19:35:15.022710",
              "updated_at": "2018-02-21 19:35:15.022710"
            },
            {
              "id": 65,
              "code": "CSC506",
              "syllabus_id": 30,
              "prerequisites": null,
              "course_name": "Architecture of Parallel Computers",
              "core": true,
              "channel_id": 30,
              "created_at": "2018-02-21 19:35:15.046772",
              "updated_at": "2018-02-21 19:35:15.046772"
            },
            {
              "id": 66,
              "code": "CSC570",
              "syllabus_id": 31,
              "prerequisites": null,
              "course_name": "Computer Networks",
              "core": true,
              "channel_id": 31,
              "created_at": "2018-02-21 19:35:15.070836",
              "updated_at": "2018-02-21 19:35:15.070836"
            },
            {
              "id": 67,
              "code": "CSC591U",
              "syllabus_id": 32,
              "prerequisites": null,
              "course_name": "User Experience",
              "core": false,
              "channel_id": 32,
              "created_at": "2018-02-21 19:35:15.094901",
              "updated_at": "2018-02-21 19:35:15.094901"
            },
            {
              "id": 68,
              "code": "CSC720",
              "syllabus_id": 33,
              "prerequisites": "Artificial Intelligence",
              "course_name": "Artificial Intelligence 2",
              "core": true,
              "channel_id": 33,
              "created_at": "2018-02-21 19:35:15.118964",
              "updated_at": "2018-02-21 19:35:15.118964"
            },
            {
              "id": 69,
              "code": "CSC722",
              "syllabus_id": 34,
              "prerequisites": "Artificial Intelligence",
              "course_name": "Advanced Topics in Machine Learning",
              "core": false,
              "channel_id": 34,
              "created_at": "2018-02-21 19:35:15.143771",
              "updated_at": "2018-02-21 19:35:15.143771"
            },
            {
              "id": 70,
              "code": "CSC568",
              "syllabus_id": 35,
              "prerequisites": "UG Operating Systems; Communication Networks",
              "course_name": "Enterprise Storage Architecture",
              "core": false,
              "channel_id": 35,
              "created_at": "2018-02-21 19:35:15.166833",
              "updated_at": "2018-02-21 19:35:15.166833"
            }
          ];
        // this.transfercomplete = false;
        // this.workload = {};
        // var sync = true;
        // let request = new XMLHttpRequest();
        // request.open("GET", "assets/main_course.json", !sync);
        // //request.responseType = 'json';
        // request.send();
        // request.onreadystatechange = (this.course = function() {
        //     if (request.readyState == 4 && request.status == "200") {
        //         var yourData = JSON.parse(request.response);
        //         return yourData["main"];
        //     }
        // });
        // this.course = JSON.parse(request.response).main;
        // //request.end();
        // // var yourDataStr = JSON.stringify(request.responseText)
        // // this.course = JSON.parse(yourDataStr).main;
        //
        //
        // let request2 = new XMLHttpRequest();
        // request2.open("GET", "assets/average.json", !sync);
        // //request.responseType = 'json';
        // request2.send();
        // request2.onreadystatechange = (this.average = function() {
        //     if (request2.readyState == 4 && request2.status == "200") {
        //         var yourData = JSON.parse(request2.response);
        //         return yourData["average"];
        //     }
        // });
        // this.average = JSON.parse(request2.response).average;
        // // var yourDataStr = JSON.stringify(request.responseText)
        // // this.average = JSON.parse(yourDataStr).average;
        //
        // let request3 = new XMLHttpRequest();
        // request3.addEventListener("load", function(){
        //   console.log("Data Transfer Complete");
        //   this.transfercomplete = true;
        // });
        // request3.open("GET", "assets/workload.json", !sync);
        // //request.responseType = 'json';
        // request3.send();
        // request3.onreadystatechange = (this.workload = function() {
        //     if (request3.readyState == 4 && request3.status == "200") {
        //         var yourData = JSON.parse(request3.response);
        //         console.log(yourData.workload);
        //         //alert("Your data: " + yourData);
        //         //alert("Your data - String: " + JSON.stringify(yourdata));
        //         return yourData.workload;
        //     }
        // });
        // this.workload = JSON.parse(request3.response).workload;
        // console.log(JSON.parse(request3.response));
        // // var yourDataStr = JSON.stringify(request.responseText)
        // // this.workload = JSON.parse(yourDataStr).workload;
        //
        // let request4 = new XMLHttpRequest();
        // request4.open("GET", "assets/category.json", !sync);
        // //request.responseType = 'json';
        // request4.send();
        // request4.onreadystatechange = (this.category = function() {
        //     if (request4.readyState == 4 && request4.status == "200") {
        //         var yourData = JSON.parse(request4.response);
        //         return yourData;
        //     }
        // });
        // this.category = JSON.parse(request4.response);
        // var yourDataStr = JSON.stringify(request.responseText)
        // this.category = JSON.parse(yourDataStr);

        //alert(this.workload);
    }

    getCourseName(id){
        for (let m of this.course){
            if (id === m.syllabus_id){
                return m.course_name;
            }
        }
        /*console.log("can't find syllabusId: " + syllabusId);*/
        return "";
    }

    getCourseId(name){
        //name = name.toLowerCase();
        var mycode = name.toUpperCase();
        console.log("mycode: " + mycode);
        while(mycode.includes(" ") || mycode.includes("-")){
            mycode = mycode.replace(" ", "");
            console.log("mycode: " + mycode);
            mycode = mycode.replace("-","");
            console.log("mycode: " + mycode);
        }
        for (let c of this.course){
            if (name.localeCompare(c.course_name.toLowerCase()) == 0){
                //alert(name + "," + c.course_name + "," + c.syllabus_id);
                return c.syllabus_id;
            }
            if(mycode === c.code){
                return c.syllabus_id;
            }
        }
        return -1;
    }

    getCoursePrereq(id){
        for (let c of this.course) {
            if (id === c.syllabus_id)
                return c.prerequisites;
        }
        return null;
    }

    getCourseAverage(id){
        if ( id === -1){
            return -1;
        }
        for (let c of this.average){
            if (id === c.syllabus_id){
                var total = c.A + c.B + c.C + c.D + c.Other;
                var median = total/2;
                var list = {'A':c.A, 'B':c.B, 'C':c.C, 'D':c.D, 'Other':c.Other};
                var i=-1;
                var items = Object.values(list)[++i];
                while (median > items && i<Object.keys(list).length){
                    median -= items;
                    items = Object.keys(list)[++i];
                }
                return Object.keys(list)[i];
            }
        }
        return -1;
    }

    getWorkload(id){
        for (let w of this.workload){
            if (id === w.syllabus_id){
                let c = new Workload();
                c.set(this.getCourseName(id), w.core, w.assignments, w.exams, w.project);
                return c;
            }
        }
        //console.log("can't getWorkload of this id: " + id);
        let c = new Workload();
        //c.set(this.getCourseName(id), 0,0,0,0);
        c.name = this.getCourseName(id);
        return c;
    }

    /*
        give subject name then return a list of course that related to the subject
     */
    makeCourseList_number(subject){
        let list = [];
        switch(subject){
            case "data science":
                list = list.concat(this.category.DSC);
                list = list.concat(this.category.ALG);
                break;
            case "software engineering":
                list = list.concat(this.category.SEC);
                list = list.concat(this.category.SF);
                break;
            case "algorithm":
                list = list.concat(this.category.ALG);
                break;
            case "application":
                list = list.concat(this.category.APP);
                break;
            case "system":
                list = list.concat(this.category.SYS);
                break;
            case "software security":
                list = list.concat(this.category.SS);
                break;
        }

        console.log("get course list(number): " + list);
        return list;

    }//end of getCourseList

    makeCourseList_name(subject){
        let list = this.makeCourseList_number(subject);
        // let cNameList = [];
        // for(let l of list){
        //     cNameList.push(this.getCourseName(l));
        // }
        // console.log("get course list(name): " + cNameList);
        return list;
    }

}

//const dataSearch = new DataSearch();
//let a = dataSearch.getWorkload(14);
//console.log(a.name + ", " + a.core + ", " + a.assingment + ", " + a.exam + ", " + a.project);
