from TargetApi import Api

api = Api.Api('http://api.dailyperfect.com', 'YOURKEY')

# add content item
item = {'keywords': 'python, snake', 'title': 'Python', 'content': 'Python is a programming language that lets you work more quickly and integrate your systems more effectively'}
api.Item.modify('python', item)

# retrieve item from TargetApi and show the result
print api.Item.get('python')


# create a new person
person = {'name': 'John Doe', 'interests': 'cooking, Python'}
api.Person.modify('testperson', person)

# list all persons
print api.Person.list()


print api.Person.recommendations('testperson')

api.Item.delete('python')
api.Person.delete('testperson')


