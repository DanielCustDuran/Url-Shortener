from django import forms
from .validators import validate_url, validate_dot_com

class  SubmitUrlForm(forms.Form):
    """docstring for  SubmitUrlForm."""
    url = forms.CharField(
        label='Submit URL',
        widget=forms.TextInput(
            attrs={
            'id': 'url_id',
            'class': 'validate',
            'placeholder': 'Introduce an url',
            'type': 'text'}
        ),
        validators=[validate_url, validate_dot_com]
    )
