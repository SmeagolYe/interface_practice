class Restaurant:
    first_name = "hello"
    last_name = "world"
    sex = "girl"

    def describe_user(self):
        print("first_name:{}\nlast_name:{}\nsex:{}\n".format(self.first_name, self.last_name, self.sex))

    def greet_user(self):
        print("你好{}".format(self.first_name + self.last_name))

user = Restaurant()
user.describe_user()
user.greet_user()
print("%o" % 20)