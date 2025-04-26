from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError('We only accept notes about Django!')
        return title