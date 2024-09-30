class Question():
    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer



class Quiz:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.indexofquestion = 0
        self.score = 0
    
    def get_questions(self):
        print(self.questions[self.indexofquestion].text)
        while self.indexofquestion < len(self.questions):
            print(f"{self.indexofquestion + 1 }. Sorunuz: {self.questions[self.indexofquestion].text}\nSeçenekler: {'\n- '.join(self.questions[self.indexofquestion].choices)}")
            user_answer = input("Cevabınızı girin: ")
            if self.questions[self.indexofquestion].answer == user_answer:
                print("Doğru cevap!")
                self.score += 1
            else:
                print("Yanlış cevap!")
            self.indexofquestion += 1
            
        print(f"skorunuz: {self.score}")

        


q1 = Question("En iyi programlama dili Hangisidir ?", ["c#", "python", "javascript", "php"], "python")
q2 = Question("En popüler Programlama Dili Hangisidir?", ["c#", "javascript", "python", "java"], "c#")
q3 = Question("En çok kazandıran Programlama Dili Hangisidir?", ["python", "c#", "javascript", "java"], "python")


listofquestions = [q1, q2, q3]
quizlist = Quiz(listofquestions)
quiz = quizlist.get_questions()
