import random
import copy

class Hat:
    def __init__(self, **kwargs):
        assert len(kwargs) >= 1
        self.contents = []
        for key, value in kwargs.items():
            for v in range(value):
                self.contents.append(key)
                
    def draw(self, number):
        n = min(number, len(self.contents))
        balls = [self.contents.pop(random.randrange(len(self.contents))) for i in range(n)] 
        return balls
                
                
def experiment(hat:Hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    for i in range(num_experiments):
        new = copy.deepcopy(hat)
        balls = new.draw(num_balls_drawn)
        corrects = 0
        for key, value in expected_balls.items():
            if balls.count(key) >= value:
                corrects += 1
        if corrects == len(expected_balls.keys()):
            probability += 1
    return probability/num_experiments


if __name__ == "__main__":
    hat = Hat(blue=3,red=2,green=6)
    actual = experiment(hat=hat,
                        expected_balls={"blue":2,"green":1},
                        num_balls_drawn=4,
                        num_experiments=1000)
    print(actual)