from django import forms




class FeedbackForms(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )

    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Rating'
            }
        )
    )

    feedback = forms.CharField(
        label="Enter Your Feedbacks",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your Feedbacks '
            }
        )
    )



