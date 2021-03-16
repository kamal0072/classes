class Post():
    def __init__(self):
        self.name='kumar'
        self.roll=101
        self.address='delhi'
    

    def song(self):
        print("instance variable",self.name)
        print("instance variable",self.roll)
        print("instance variable",self.address)
x=Post()
y=Post()
print(x.name)
print(id(x.name))

print(id(x.roll))
print(id(x.address))
print("--------------")
print(y.name)
print(y.roll)
print(y.address)
