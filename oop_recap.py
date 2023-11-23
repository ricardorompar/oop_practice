#%%
class Chair:
    def __init__(self, color, number_of_legs):
        if int != type(number_of_legs):
            raise ValueError("number_of_legs must be type int")

        self.color = color
        self.number_of_legs = number_of_legs

chair1 = Chair("Black", 4)

class Counter:
    def __init__(self, number_of_people = 0):
        self.number_of_people = number_of_people
    
    def increase(self):
        self.number_of_people += 1

counter1 = Counter()
counter1.increase()
print(counter1.number_of_people)