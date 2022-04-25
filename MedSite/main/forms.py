from django.forms import ModelForm

from main.models import User


class ArticleForm(ModelForm):

    class Meta:
        model = User
        fields = ['name', 'surname', 'password']

        # def clean_title(self):
        #     return self.cleaned_data.get('name').upper()

