from django import forms
from .models import Quiz
from .models import Question, Option

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']  



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'text']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']
