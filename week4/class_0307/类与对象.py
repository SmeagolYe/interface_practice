class BoyFriend:
    sex = "boy"
    height = 180

    def playBall(self):
        return "会打篮球"

    def cook(self, *args):
        dish_name = ''
        for item in args:
            dish_name += item
            dish_name += '、'
        print("会做饭，而且擅长做{}".format(dish_name))

    def coding(self, language="python3"):
        print("会写{}代码".format(language))

    def print_self(self):
        print("self:", self)

    @classmethod
    def hello(cls):
        print("hello")

    @staticmethod
    def world():
        print("world")

b = BoyFriend()
print(b.sex)
print(b.height)

b.coding()
b.cook("番茄鸡蛋", "糖醋排骨")
s = b.playBall()
print(s)
