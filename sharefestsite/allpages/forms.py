from django import forms

class EmailForm(forms.Form):
    Emails = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(self):
        return self.Email
    