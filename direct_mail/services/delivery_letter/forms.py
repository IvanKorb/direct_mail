from django import forms

from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        exclude = ['total_price']

    def save(self, commit=True):
        total_number = 0
        for audience in self.cleaned_data['audience']:
            total_number += audience.number
        total_price = self.instance.delivery_type.price * total_number
        self.instance.total_price = total_price
        return super().save(commit=True)
