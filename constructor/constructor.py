# class Student():
#     def __init__(self):
#         self.name='kamal'
#         self.roll=101
#         self.city='suar'
#     def teacher(self):
#         self.name='budha'
# x=Student()
# print("This Is COnt Valiable:",x.name)

class Student():
    def __init__(self,id,roll=12):
        self.name='kamal'
        self.roll=101
        self.city='suar'

    def teacher(self):
        self.name='budha'
x=Student(100)
# print("This Is Const. Valiable:",x.name)
y=Student(12)
y.teacher()









