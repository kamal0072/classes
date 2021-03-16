class Post():
    name='instagram'

    @classmethod
    def is_name(cls):
        print('CLass Method:',cls.name)

x=Post()
y=Post()
z=Post()
print("--------")
print('class var:',Post.name)
print("Object one:",x.name)
print("Object two:",y.name)
print("Object three:",z.name)
print("------")
Post.name='Youtube'
print('class var:',Post.name)
print("Object one:",x.name)
print("Object two:",y.name)
print("Object three:",z.name)
