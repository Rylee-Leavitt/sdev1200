#
# Rylee Leavitt
# 2/21/25
# Trivia Game Programming Project
# SDEV 1200
#

# game_Questions.py

class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct_ans):
        #__init__ initializes the attributes of the Question object with the provided values.
        
        self.question = question
        #takes the value provided when the instance is created & assigns it to the instance variable question

        self.ans1 = ans1
        #assigns the value of the parameter ans1 to the instance variable ans1

        self.ans2 = ans2
        #assigns the value of the parameter ans2 to the instance variable ans2

        self.ans3 = ans3
        #assigns the value of the parameter ans3 to the instance variable ans3

        self.ans4 = ans4
        #assigns the value of the parameter ans4 to the instance variable ans4

        self.correct_ans = correct_ans
        #assigns the value of the parameter correct_ans to the instance variable correct_ans

    # Accessors (getters)
    def get_question(self):
        return self.question #returns the trivia question

    def get_ans1(self): #returns possible answer #1
        return self.ans1

    def get_ans2(self): #returns possible answer #2
        return self.ans2

    def get_ans3(self): #returns possible answer #3
        return self.ans3

    def get_ans4(self): #returns possible answer #4
        return self.ans4

    def get_correct_ans(self): #returns Correct answer
        return self.correct_ans

    # Mutators (setters)
    def set_question(self, question): #sets self.question = question
        self.question = question

    def set_ans1(self, ans1): #sets self.ans1 = ans1
        self.ans1 = ans1

    def set_ans2(self, ans2): #sets self.ans2 = ans2
        self.ans2 = ans2

    def set_ans3(self, ans3): #sets self.ans3 = ans3
        self.ans3 = ans3

    def set_ans4(self, ans4): #sets self.ans4 = ans4
        self.ans4 = ans4

    def set_correct_ans(self, correct_ans): #self.correct_ans = correct_ans
        self.correct_ans = correct_ans

questions_List = [
    Question("What is Astarions secret?", "He's a Vampire Spawn", "He Hates Gnomes", "He is a Shapechanger ", "He is incapable of love", 1),
    # Answer: He's a Vampire Spawn

    Question("What is Astarion's Class?", "Druid", "Rougue", "Wizard", "Barbarian", 2),
    # Answer: Rougue

    Question("Who is Cazador to Astarion?", "Romantic interest", "Bestie", "Enslavor/Abuser", "Aquaintance", 3),
    # Answer: Enslavor/Abuser

    Question("How long has Astarion been a vampire?", "500 years", "2,000 years", "100 years", "200 years", 4),
    # Answer: 200 years

    Question("What is Astarions Greatest Fear?", "Forever feeling like a slave to someone else", "Breaking a nail", "Most Things Fear him", "Losing TAV", 1),
    # Answer: Forever feeling like a slave to someone else

    Question("What does Astarion want most'?", "TAV", "Revenge", "to be elbow deep in gore", "A juicy Rat", 2),
    # Answer: Revenge

    Question("What are Astarion's scars?", "A ballad of love", "A Freak Accident", "A Drawing", "An Infernal Contract", 4),
    # Answer: An Infernal Contract

    Question("What is Astarion's Last Name?", "Ironfist", "Karlach", "Ancunin", "Pablo", 3),
    # Answer: Ancunin

    Question("How did Astarion Die?", "An Arrow to the Knee", "Mind Flayer Parasite", "A group of thugs", "Cazador", 3),
    # Answer: A group of thugs

    Question("Is Astarion The Hottest/ Most attractive Companion?", "Yes!", "No >:(", "Shadowheart is better", "No, The bear!", 1)
    # Answer: Yes!
]

