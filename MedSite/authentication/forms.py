from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class NewUserForm(UserCreationForm):

    name = forms.CharField(required=True, help_text='Required: Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    surname = forms.CharField(required=True, help_text='Required: Surname',
                                widget=(forms.TextInput(attrs={'class': 'form-control'})))
    # phone_number = forms.CharField(required=True, help_text='Required: Phone Number',
    #                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(required=True, help_text='Required: Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_('Just Enter the same password, for confirmation'))

    class Meta(UserCreationForm.Meta):
        User = get_user_model()
        model = User
        exclude = ['username',]
        fields = ['name', 'surname', "email", "password1", "password2",
                  # "phone_number"
                  ]

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


