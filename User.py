# your improved User class goes here
class User:

    all_users = {}
    post = []

    def __init__(self, name, email, id, license_num):

    
        self._name = name
        self._id = id
        self._email = email
        self._license_num = license_num
        self._posts = []
        User.all_users[self.id] = self


    def __repr__(self):
        return f"Name: {self.name} has this id: {self.id} with this email: {self.email} and this license: {self.license_num}."
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def email(self):
        return self._email
    
    @property
    def license_num(self):
        return self._license_num
      
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @id.setter
    def id(self, new_id):
        self._id = new_id

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @license_num.setter
    def license_num(self, new_license_num):
        self._license_num = new_license_num

    @classmethod
    def add_user(cls):
        name = input("Enter the user's name: ")
        email = name + "@school.org"
        id = int(input("Enter the user's id: "))
        license_num = int(input("Enter the user's license: "))
        return cls(name, email, id, license_num)

    @staticmethod
    def view_all_users():
        for user in User.all_users.values():
            print(user)


    @staticmethod
    def print_user_post(id):
        user = User.all_users.get(id)
        if user:
            for post in user._posts:
                print(post)
        else:
            print(f"No user with that id: {id}")

    def add_post(self):
        new_post = input("Please enter the post information")
        self._posts.append(new_post)
        User.post.append(new_post)
        print(f"New post added for user")


class PremiumUser(User):
    def __init__(self, name, email, id, license_num):
        super().__init__(name, email, id, license_num)
    


class FreeUser(User):
    def __init__(self, name, email, id, license_num):
        super().__init__(name, email, id, license_num)

    def add_post(self):
        if len(self._posts) == 2:
            print("You have exceeded your allowed number of post. Upgrade to preminum")
            exit()
        else:
            new_post = input("Post info")

    
    
# user1 = User("kendra", "kendra@school.org", 1, 12)

# user2 = User("mark", "mark@school.org", 2, 22)

# user3 = User("david", "david@school.org", 3, 33)


# print(user1.add_user_post())
# print(User.view_all_users())
# # print(User.add_user_post())
# # print(User.add_user_post())
# # print(User.add_user_post())
# print(User.print_user_post(1))
# # print(User.print_user_post())
