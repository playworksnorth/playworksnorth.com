from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label=_('Name'))
    email = forms.EmailField(label=_('Email'))
    message = forms.CharField(widget=forms.Textarea, max_length=4000, label=_('Message'))
    # Honeypot: styled off-screen in CSS, so only bots that fill every field see
    # it. Named and labeled to avoid matching any browser autofill heuristic
    # (a field named "company" got silently autofilled from saved address
    # profiles, tripping this for real visitors).
    hp_field = forms.CharField(
        required=False,
        label='Leave this field blank',
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'tabindex': '-1'}),
    )

    def clean_hp_field(self):
        value = self.cleaned_data.get('hp_field')
        if value:
            raise forms.ValidationError('spam')
        return value
