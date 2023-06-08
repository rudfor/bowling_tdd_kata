class Game:
    """
    [2][2][2][2][2][2][2][2][2][2][2][3]
    """

    def __init__(self, score_array=None):
        self.score = int(0)
        self.frame = 0
        self.score_array = score_array
        if (score_array == None):
            self.score_array = [[], [], [], [], [], [], [], [], [], []]
        elif (len(self.score_array) != 10):
            print(f"Incorrect frame Initialized")
            raise ValueError('Invalid Frame')
            exit(66)
        self.update_score()

    @staticmethod
    def is_empty(frame_data=[]):
        if frame_data is None:
            frame_data = []
        elif len(frame_data) == 0:
            frame_data = []
        return len(frame_data) == 0

    @staticmethod
    def is_gutter(frame=0, frame_data=[]):
        if Game.is_empty(frame_data):
            frame_data = []
        if frame < 9:
            return sum(frame_data) == 0

    @staticmethod
    def is_strike(frame=0, frame_data=[]):
        if Game.is_empty(frame_data):
            return False
        if frame < 9:
            return frame_data[0] == 10

    @staticmethod
    def is_spare(frame=0, frame_data=[]):
        if Game.is_empty(frame_data):
            frame_data = [0, 0]
        if Game.is_strike(frame, frame_data):
            return False
        if frame < 9:
            return sum(frame_data) == 10

    def get_frame_score(self, frame=0, depth=2):
        if depth == 0:
            return 0
        frame_score = sum(self.score_array[frame])
        if Game.is_empty(frame_data=self.score_array[frame]):
            return frame_score
        elif Game.is_gutter(frame, frame_data=self.score_array[frame]):
            return frame_score
        elif Game.is_strike(frame, frame_data=self.score_array[frame]):
            next_score = self.get_frame_score(frame + 1, depth - 1)
            if next_score == 0:
                return 0
            else:
                frame_score += next_score
                if len(self.score_array[frame+1]) == 1:
                    if len(self.score_array[frame+2]) != 0:
                        frame_score += self.score_array[frame + 2][0]
                else:
                    frame_score += sum(self.score_array[frame + 1])

        elif Game.is_spare(frame, frame_data=self.score_array[frame]):
            frame_score += sum(self.score_array[frame + 1])
            if len(self.score_array[frame+1]) != 0:
                frame_score += self.score_array[frame + 1][0]
        return frame_score

    def roll(self, pins: int):
        self.score_array[self.frame] = pins

    def update_score(self):
        score = 0
        frame = 0
        for i in self.score_array[:-1]:
            score += self.get_frame_score(frame)
            frame += 1
        self.frame = frame
        self.score = score

    def score(self):
        return int(self.score)

    def print(self):
        print(f"The Array is: {self.score_array}")  # printing the array


if __name__ == '__main__':
    print(f"this is not intended to be run Stand Alone({__file__})")
