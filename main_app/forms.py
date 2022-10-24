from django.forms import ModelForm
from .models import Sister, Chapter, Nickname_Request


class Nickname_RequestForm(ModelForm):
    class Meta:
        model = Nickname_Request
        fields = ['name', 'nickname_meaning']
