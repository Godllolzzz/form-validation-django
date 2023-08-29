from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name  must not be empty!",
#         "max_length": "Please write a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", max_value=5, min_value=1)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name  must not be empty!",
                "max_length": "Please write a shorter name!"
            }
        }
        # we can also use exclude for excluding a list of field of model