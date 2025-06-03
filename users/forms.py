from allauth.account.forms import SignupForm, LoginForm
from django.forms.fields import BooleanField


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full rounded-lg bg-gray-700 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
            

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field, BooleanField):
                css_class = ''
            else:
                css_class = 'color-black w-full rounded-lg bg-gray-700 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            field.widget.attrs.update({
                'class': css_class
            })
