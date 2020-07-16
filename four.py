import math

class point:
    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def cal_dis(self, otherpoint):
        return math.sqrt(
            (self.x - otherpoint.x)**2
            + (self.y - otherpoint.y)**2
            )

point1 = point()
point2 = point()

point1.reset()
point2.move(5, 0)
print(point2.cal_dis(point1))

point1.move(3, 4)
print(point1.cal_dis(point2))
print(point1.cal_dis(point1))
