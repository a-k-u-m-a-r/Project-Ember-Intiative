from firebase_admin import auth
from flask import session

class User():

    def __init__(self):
        self.uid = None
        self.uname = None
        self.email = None


    def create_user(self, uemail, upassword, uname):
        try:
            auth.get_user_by_email(uname)
            auth.get_user_by_email(uemail)
            

        except auth._auth_utils.UserNotFoundError:

            user = auth.create_user(
                email=uemail,
                email_verified=False,
                password=upassword,
                display_name=uname,
                ) 
            session['email'] = user.email
            session['uid'] = user.uid
            session['uname'] = user.display_name

        except auth._auth_utils.EmailAlreadyExistsError:

            print("It exists!")