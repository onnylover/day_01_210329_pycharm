from class_test.Point import Point


class ColorPoint(Point):
    def __init__(self, color, x, y):
        super().__init__(x,y)
        self.color = color

    def draw(self):
        print(f"x={self.x} y={self.y} 에 {self.color}점을 그렸습니다.")