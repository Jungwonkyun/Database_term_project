from django.contrib.auth.hashers import make_password

from access.models import CustomUser
from test_util.util import generateRandStr
from settings.models import Privacy


# Valid user account fields
valid_uname = "appTester01"
valid_pass = "s3cureP@ssword054!"
valid_email = "apptester@foodlog.com"


def create_default_valid_user():
    username = valid_uname
    email = valid_email
    password = valid_pass
    user = CustomUser.objects.create_user(username, email, password)
    generatePrivacySetting(user)
    return user


def create_random_valid_user():
    username = generateRandStr(10)
    email = f'{generateRandStr(5)}@abc.com'
    password = generateRandStr(12)
    user = CustomUser.objects.create_user(username, email, password)
    generatePrivacySetting(user)
    return user


def create_user(username: str, password: str = '', fname: str = '', lname: str = '',
                email: str = '', save=False):
    """
    Create a user with the given `username`, and optional `password`,
    first name `fname`, last name `lname`, and `email`.
    These parameters are optional for testing purposes.
    """
    user = CustomUser(username=username, email=email, password=make_password(password),
                      first_name=fname, last_name=lname)

    if save:
        user.save()
        generatePrivacySetting(user)
    return user


def generatePrivacySetting(user: CustomUser):
    privacy_setting = Privacy(user=user)
    privacy_setting.save()
