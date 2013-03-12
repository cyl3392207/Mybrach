from django.forms import BaseForm

class RegisterForm(BaseForm):
    pass

class LoginForm(BaseForm):
    pass

class ProfileForm(BaseForm):
    pass

class ForgetPasswordForm(BaseForm):
    pass

class ResetPasswordForm(BaseForm):
    pass

from django.contrib.auth.forms import *
