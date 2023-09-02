from django import forms
from .models import PracticeModel

# class PracticeForm(forms.Form):
#     user_name = forms.CharField(required=True)
#     user_age = forms.IntegerField(required=False) 

class PracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeModel
        fields = '__all__'
        labels = {
            "user_name": "Name",
            "user_age": "Age",
            "user_image": "Image"
        }
        error_messages = {
            "user_name": {
                "required": "Your name  must not be empty!",
                "max_length": "Please write a shorter name!"
            }
        }
