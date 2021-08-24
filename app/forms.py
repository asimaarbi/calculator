from django.forms import ModelForm, forms
from django.forms import PasswordInput
from app.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': PasswordInput
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")

        if len(password) < 8:
            raise forms.ValidationError(
                "Password length must be greater than or equal to 8"
            )