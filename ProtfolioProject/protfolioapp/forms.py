from django import forms


class MailSendForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    to=forms.EmailField()
    message=forms.CharField(required=True,widget=forms.Textarea)