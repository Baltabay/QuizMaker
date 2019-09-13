import sys

# The Simple class question, it contains right description(with options in some cases) and answer for that question
class Question:

    def __init__(self, description, answer, options = None):

        # Needed data
        self.description = description
        self.answer = answer

        # Only for Test class
        self.options = options

    def setDescription(self , description):
        self.description = description

    def setOptions(self , options):
        self.options = options

    def toString(self):
        return self.description + "\n" + self.options + "\n"

    def getDescription(self):
        return self.description

# The FillIn class, type of question that cointains only description with open blank
class FillIn(Question):

    def __init__(self, Question):

        self.question = Question
        self.description = Question.description

        self.getRightDescription()

    def getRightDescription(self):
        self.question.setDescription(self.description.replace("{blank}" , "_______"))

# The Test class, general type of question with description and options
class Test(Question):

    def __init__(self, Question):

        self.question = Question
        self.options = Question.options
        self.getRightDescription()

    def getRightDescription(self):

        rawDescription = self.options.split("\n")

        rawText = ""
        options = ["A) ", "B) ", "C) ", "D) ", "E) ", "F) "]
        
        for i in range(len(rawDescription)-1):
            rawText += options[i] + rawDescription[i] + "\n"
            
        self.question.setOptions(rawText)

# The Quiz class, used to build(load) Quiz!
class Quiz:

    def __init__(self, filePath):
        self.path = filePath
        self.questions = []

        try:
            self.loadQuestion()
        except Exception:
            print("Wrong quiz file format or file does not exits!")

    def loadQuestion(self):
        file = open(self.path , "r").read().split("\n")
        text = []

        for i in file:

            if i == '':

                if len(text) == 2:
                    q = Question(text[0] , text[1])
                    FillIn(q);
                    self.questions.append(q)
                elif len(text) >= 6 and len(text) <= 8: 
                    options = ""
                    for i in range(1, len(text)-1):
                        options = options + text[i] + "\n"
                    
                    q = Question(text[0] , text[len(text)-1] , options)
                    Test(q)
                    self.questions.append(q)

                text.clear()
                continue

            text.append(i)


# The QuizMaker class, initialisere and runs the quiz!
class QuizMaker:


    # NOTICE!!!
    # You need to specify the correct path to the files with the questions
    pathToFile = 'C:\\Users\\hp\\Desktop\\QuizMakerProject\\'

    def __init__(self, fileName):
        self.quiz = Quiz(filePath=self.pathToFile+fileName)
        self.questions = self.quiz.questions
        self.length = len(self.questions)
        self.rightAnswers = 0

    def printLine1(self):
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n")

    def printLine2(self):
        print("---------------------------------------------------------\n")

    def start(self):
        print("=================WELCOME TO PYTHON QUIZ!=================\n")

        self.counter = 0
        
        for numerator in range(1, self.length+1):
            if self.questions[self.counter].options is None:
                print(str(numerator)+ ".  " + self.questions[self.counter].getDescription())
                self.check(self.questions[self.counter])
                self.printLine2()
                self.counter += 1
            else:
                print(str(numerator)+ ".  " + self.questions[self.counter].toString())
                self.check(self.questions[self.counter])
                self.printLine2()
                self.counter += 1


        self.printLine1()
        print("   QUIZ IS O...O...OVER")
        print("   You got " + str(self.rightAnswers) + " out of " + str(self.length))

        if self.rightAnswers < self.length/2:
            print("   LOSEEEER")
        else:
            print("   CONGRATS!!!")
        self.printLine1()

    def check(self ,question):

        userAnswer = input("Your answer is : ")

        # You can hide the label is correct after each question
        if userAnswer.lower() == question.answer.lower():
            print("               Right")
            self.rightAnswers += 1
        else:
            print("               Wrong")
            


quizmaker = QuizMaker(sys.argv[1]).start()
