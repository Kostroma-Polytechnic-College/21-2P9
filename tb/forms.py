from django.forms import ModelForm as MF, TextInput
from tb.models import TelegramUser

class TelegramUserForm(MF):
    class Meta:
        model = TelegramUser
        fields = ('external_id', 'name')
        widgets = {'name': TextInput}