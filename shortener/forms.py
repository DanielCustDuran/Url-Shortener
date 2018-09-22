from django import forms

from .validators import validate_url, validate_dot_com

class  SubmitUrlForm(forms.Form):
    """docstring for  SubmitUrlForm."""
    url = forms.CharField(label = 'Submit URL', validators = [validate_url, validate_dot_com])
