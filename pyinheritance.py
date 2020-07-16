class poy:
    __width = None
    __height = None
    def set_values(self, width, height):
        self.__width = width
        self.__height = height
    def get_width(self):
        return __width
    def get_height(self):
        return __height

class rec(poy):
    def area(self):
        return (self.get_width() * self.get_height())

class poly(poy):
    def area(self):
        return (3*self.get_width() * self.get_height())

rect = rec()
tri = poly()

rect.set_values(50,30)
tri.set_values(85,60)

print(rect.area())
print(tri.area())