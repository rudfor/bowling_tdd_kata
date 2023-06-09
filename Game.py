"""
Kata TDD example exploration for Bowling Scoring Example
"""


class Game:
    """
    Game Class
    """
    def __init__(self, score_array=None):
        """
        Initialization possible with provision of a bowling set of frames
        Defaulted to None also when provided with None explicitly
        :param score_array:
        """
        self.score = int(0)
        self.frame = 0
        self.score_array = []
        self.initiate_frames(score_array)
        self.update_score()

    def initiate_frames(self, score_array):
        if score_array is None:
            self.score_array = [[], [], [], [], [], [], [], [], [], []]
        else:
            self.score_array = score_array

        return_value = True
        if len(self.score_array) != 10:
            raise ValueError(f'Invalid Frame length: {len(score_array)}')
            exit(66)
        for i in self.score_array[:-1]:
            if self.score_array[i]
        #
        #     score += self.get_frame_score(frame)


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
        frame_score = sum(self.score_array[frame])
        if depth == 0:
            return 0
        elif Game.is_empty(frame_data=self.score_array[frame]):
            return frame_score
        elif Game.is_gutter(frame, frame_data=self.score_array[frame]):
            return frame_score
        elif Game.is_strike(frame, frame_data=self.score_array[frame]):
            frame_score += sum(self.score_array[frame + 1])
            if len(self.score_array[frame+1]) == 1:
                if len(self.score_array[frame+2]) != 0:
                    frame_score += self.score_array[frame + 2][0]

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
