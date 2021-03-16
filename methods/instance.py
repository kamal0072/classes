class Page():
    def __init__(self):
        #inctance variable
        self.name="kunal"




    def page_type(self,roll):
        self.roll=roll
        print("Instnance variable Page:",self.name)
        print("instance variable",self.name)
        print("Inctance variable with parameter:",self.roll)
    
x=Page()
x.page_type(100)