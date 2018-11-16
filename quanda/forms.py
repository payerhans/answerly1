from django import forms
from django.contrib.auth import get_user_model

from quanda.models import Question, Answer

class QuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True
        #d=get_user_model().
    )
    class Meta:
        model = Question
        fields = ['title', 'question', 'user', ]

class AnswerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True
    )

    question = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Question.objects.all(),
        disabled=True
    )

    class Meta:
        model=Answer
        fields = ['answer', 'user', 'question', ]