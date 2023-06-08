
class Game:
    """
    [2][2][2][2][2][2][2][2][2][2][2][3]
    """
    def __init__(self, score_array=None):
        self.score = int(0)
        self.frame = 0
        self.score_array = score_array
        if (score_array==None):
            self.score_array = [[], [], [], [], [], [], [], [], [], []]
        elif (len(self.score_array)!=10):
            print(f"Incorrect frame Initialized")
            exit(66)
        self.update_score()


    def roll(self, pins: int):
        self.score_array[self.frame] = pins

    def update_score(self):
        for i in self.score_array[:-1]:
            pass
        

    def score(self):
        return int(self.score)

    def print(self):
        print("The Array is: ", self.score_array)  # printing the array

    def create_new(self):
        pass

if __name__ == '__main__':
    print(f"this is not intended to be run Stand Alone({__file__})")