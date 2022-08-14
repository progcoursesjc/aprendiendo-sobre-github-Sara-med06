class Teacher:
    
    def __init__(self, name):
        self.courses = {}
        self.name = name 

    def create_course(self, name):
        if (name in self.courses):
            print(f"Course {name} is already created") 
        else: 
           self.courses[name] = Course(name)
           print(f"Course {name} was added")

    def create_quiz(self, course_name, quiz_name, percentage, questions):
        if (course_name in self.courses):
            course = self.courses[course_name]
            course.create_quiz(quiz_name, percentage, questions)
        else: 
           print(f"Course {course_name} doesn't exist") 

    def create_question(self, course_name, quiz_name, question):
        if (course_name in self.courses):
            course = self.courses[course_name]
            
            if (quiz_name in course.quizes):
                quiz = course.quizes[quiz_name]
                quiz.create_question(question)
            else:
                print(f"Question {question} can´t be added")
        else:
                print(f"Question {question} can´t be added")

class Course:
    
    def __init__(self, name):
        self.quizes = {}
        self.name = name

    def create_quiz(self, quiz_name, percentage, questions):
        if (quiz_name in self.quizes):
            print(f"quiz {quiz_name} is already created") 
        elif (self.can_add_quiz(percentage)): 
           self.quizes[quiz_name] = Quiz(quiz_name, percentage, questions)
           print(f"Quiz {quiz_name} was added")
        else:
            print(f"quiz {quiz_name} can´t be added")
            
    def can_add_quiz(self, new_percentage):
        percentage = new_percentage

        for quiz in self.quizes.values():
            percentage  += quiz.percentage
        
        if percentage >= 100:
            print(f"percentage: {percentage}% can´t exceed 100%") 
            return False

        return True

class Quiz:

    def __init__(self, name, percentage, question_number):
        self.questions = {}
        self.name = name 
        self.percentage = percentage
        self.question_number = question_number
        
    def create_question(self, question):

        if (question in self.questions):
            print(f"question {question} is already created") 
        elif (self.can_add_question()): 
           self.questions[question] = Question(question)
           print(f"Question {question} was added")
        else:
            print(f"Question {question} can´t be added") 
    
    def can_add_question(self):
        if len(self.questions) < self.question_number:
            return True
        
        print(f"Number questions can´t exceed {self.question_number}") 
        return False

class Question:
    def __init__(self, question):
        self.question = question 

teacher = Teacher("juan")
teacher.create_course('Ejemplo')
teacher.create_quiz('Ejemplo2', 'quiz11', 25, 5)
teacher.create_quiz('Ejemplo', 'quiz1', 25, 5)
teacher.create_question('Ejemplo', 'quiz1', '¿Cómo crear un array?')
teacher.create_question('Ejemplo', 'quiz1', '¿Qué es POO?')
teacher.create_question('Ejemplo', 'quiz1', '¿Qué significa if?')
teacher.create_question('Ejemplo', 'quiz1', '¿Qué es una clase?')
teacher.create_question('Ejemplo', 'quiz1', '¿Qué significa instanciar?')
teacher.create_quiz('Ejemplo', 'quiz2', 25, 3)
teacher.create_question('Ejemplo', 'quiz2', '¿Cómo crear un objeto?')
teacher.create_question('Ejemplo', 'quiz2', '¿Qué es un ciclo?')
teacher.create_question('Ejemplo', 'quiz2', '¿Qué significa else?')
teacher.create_question('Ejemplo', 'quiz2', '¿Qué es una lista?')




