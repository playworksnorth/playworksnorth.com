from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label=_('Name'))
    email = forms.EmailField(label=_('Email'))
    message = forms.CharField(widget=forms.Textarea, max_length=4000, label=_('Message'))
    # Honeypot: styled off-screen in CSS, so only bots that fill every field see it.
    company = forms.CharField(required=False, label='Company website')

    def clean_company(self):
        value = self.cleaned_data.get('company')
        if value:
            raise forms.ValidationError('spam')
        return value
