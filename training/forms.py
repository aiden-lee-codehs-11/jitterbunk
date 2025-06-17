from django import forms

class ResourceForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    notion_link = forms.CharField(
        label="Notion Link",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    training_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-input'
        }),
        input_formats=['%Y-%m-%d %H:%M:%S'],
        label='Date of Training'
    )
    team = forms.CharField(
        label="Team",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
