from django import forms


class ResourceForm(forms.Form):
    title = forms.CharField(label="title", max_length=200)
    notion_link = forms.CharField(label="notion_link", max_length=200)
    training_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%d %H:%M:%S'],
        label='date of training'
        )
    team = forms.CharField(label="team", max_length=200)
