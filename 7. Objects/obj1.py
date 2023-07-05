class StarCookie:  # pascal casing
    milk = 0.1
    def __init__(self, color):
        self.color = color


# camel Case
# snake_case

starcookie = StarCookie('red')
print(starcookie.weight)

starcookie.weight = 15

# Setting a default value for an object

class YouTube:

    url = 'www.youtube.com/watch'
    def __init__(self, username = 0,subscriber = 0, subscriptions = 0):
        self.username = username
        self.subscriber = subscriber

    def subscribe(self, user):
        self.subscriber += user




user1 = YouTube('Gaurav')
user1.subscriber = 100
user2 = YouTube('Smriti')
user2
user1.__dict__
YouTube.__dict__
user1.url = 'www.google.com/youtube'


user2.url

YouTube.url = 'http://www.google.com/youtube1'

user2.url

# Methods 


class Robot:
    def enter_charge(self):
        self.battery_level += 1



# Lets redo the entire class thing


class Youtube:
    def __init__(self, username, subscribers = 0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1


user1 = Youtube('Gaurav')
user2 = Youtube('Smriti')

user1.subscribers
user2.subscribers
user1.subscriptions
user2.subscriptions

user1.subscribe(user2)
user2.subscribe(user1)


