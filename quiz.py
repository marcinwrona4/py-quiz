import random

class Question:
    def __init__(self, id, question, category, answers, correctAnswer):
        self.id = id
        self.question = question
        self.category = category
        self.answers = answers
        self.correctAnswer = correctAnswer


class Quiz:
    def __init__(self):
        self.questionsList = []
        self.prepareQuestions()

    def prepareQuestions(self):
        with open('questions.txt', 'r') as fh:
            for line in fh:
                all = tuple(line.rstrip().split(','))
                id = all[0]
                question = all[1]
                category = all[2]
                answer1 = all[3]
                answer2 = all[4]
                answer3 = all[5]
                answer4 = all[6]
                correctAnswer = all[7]

                qObj = Question(id, question, category, [answer1, answer2, answer3, answer4], correctAnswer)
                self.questionsList.append(qObj) 

    def startQuiz(self):
        correctAnswers = 0

        print("Witaj w quizie!\n")

        while True:
            inp = input("Wpisz 1, aby rozpocząć quiz\n\
Wpisz \"exit\", aby wyjść z programu\n")

            match inp:
                case "1":
                    random.shuffle(self.questionsList)
                    print()

                    for el in self.questionsList:  
                        print(el.question)
                        answer = input()
                        if answer == el.correctAnswer:
                            print("Poprawna odpowiedź\n")
                            correctAnswers += 1
                        else:
                            print(f"Błędna odpowiedź. Poprawna to: {el.correctAnswer}\n")

                    print(f"Poprawnych odpowiedzi: {correctAnswers} / {len(self.questionsList)}\n")
                    correctAnswers = 0
                case "exit":
                    break
                case _:
                    print("Niepoprawny wybór. Spróbuj ponownie\n")


quiz = Quiz()
quiz.startQuiz()
