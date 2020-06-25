from firebase_admin import auth
from flask import session, request
import requests, json, argparse, os


class User():



    def __init__(self):
        self.uid = None
        self.uname = None
        self.email = None


    def create_user(self, uemail, upassword, uname):
        try:
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

    def logout_user(self):
        session.pop('email')
        session.pop('uid')
        session.pop('uname')

        print('LOGGED OUT')

    def login_user(self, email, password, return_secure_token: bool = True, msg=None):
        FIREBASE_WEB_API_KEY = "AIzaSyAopjFhQL0sG7DqIZpxSOf1NyE5pgK5Y7Y" # SET AS ON ENVIRON VARIABLE
        rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        message = {
            'INVALID_EMAIL' : 'Your have not submitted an appropriate email',
            'INVALID_PASSWORD' : 'The password you have entered is not correct',
            'EMAIL_NOT_FOUND' : 'Your email does not exist in our database'
        }   

        payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token})

        r = requests.post(rest_api_url,
                        params={"key": FIREBASE_WEB_API_KEY},
                        data=payload)
        user = r.json()

        if 'error' in user:
            msg = message[user['error']['message']]

        else:
            session['email'] = user['email']
            session['uid'] = user['localId']
            session['uname'] = user['displayName']

        return msg

        

