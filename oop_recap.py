#%%
class Chair:
    def __init__(self, color, number_of_legs):
        if int != type(number_of_legs):
            raise ValueError("number_of_legs must be type int")

        self.color = color
        self.number_of_legs = number_of_legs

chair1 = Chair("Black", 4)

print()