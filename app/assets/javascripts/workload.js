class Workload{
    constructor(){
        //default highest workload
        this.name = "";
        this.core = 1;
        this.assingment = 2;
        this.exam = 2;
        this.project = 2;
    }

    set(name, core, assignment, exam, project){
        this.name = name;
        this.core = core;
        this.assingment = assignment;
        this.exam = exam;
        this.project = project;
    }
}