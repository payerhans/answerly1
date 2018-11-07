from django import forms
from django.contrib.auth import get_user_model

from quanda.models import Question

class QuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects,
        disabled=True
        #d=get_user_model().
    )
    class Meta:
        model = Question
        fields = ['title', 'question', 'user', ]