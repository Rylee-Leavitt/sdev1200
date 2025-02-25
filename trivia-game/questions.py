#
# Rylee Leavitt
# 2/21/25
# Trivia Game Programming Project
# SDEV 1200
#

# questions.py

class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct_ans):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.correct_ans = correct_ans

    # Accessors (getters)
    def get_question(self):
        return self.question

    def get_ans1(self):
        return self.ans1

    def get_ans2(self):
        return self.ans2

    def get_ans3(self):
        return self.ans3

    def get_ans4(self):
        return self.ans4

    def get_correct_ans(self):
        return self.correct_ans

    # Mutators (setters)
    def set_question(self, question):
        self.question = question

    def set_ans1(self, ans1):
        self.ans1 = ans1

    def set_ans2(self, ans2):
        self.ans2 = ans2

    def set_ans3(self, ans3):
        self.ans3 = ans3

    def set_ans4(self, ans4):
        self.ans4 = ans4

    def set_correct_ans(self, correct_ans):
        self.correct_ans = correct_ans


questions = [
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

