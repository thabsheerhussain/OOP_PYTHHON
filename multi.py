class baseclass:
     int base_num=0

     def base(self):
         print("this is base class")
         self.base_num += 1

class leftclass:

    int left_num = 0

    def left(self):
        baseclass.base(self)
        print("this is left")
        self.left_num += 1

class rightclass:

    int right_num = 0

    def right(self):
        baseclass.base(self)
        print("this is right")
        self.right_num += 1

class subclass(rightclass,leftclass):
    int sub_num = 0

    def sub(self):
        leftclass.left(self)
        rightclass.right(self)
        print("this is  sub class")
        self.sub_num += 1
