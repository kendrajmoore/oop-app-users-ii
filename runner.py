from User import FreeUser 
from User import PremiumUser
from User import User

# def __init__(self, name, email, id, license_num):
kendra = FreeUser("kendra", "kendra@test.org", 12, 22)
Andrew = PremiumUser("Andrew", "andrew@test.org", 13, 23)

kendra.add_post()
kendra.add_post()
kendra.add_post()
User.print_user_post(12)
# print(kendra)
print(Andrew)