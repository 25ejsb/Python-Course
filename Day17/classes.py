class User:
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Always needs a self
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Eitan")

print(user1.id)
print(user1.username)

user2 = User("002", "Eitan2")

print(user2.id)
print(user2.username)

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)