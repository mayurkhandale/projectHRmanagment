from django import forms
from hradmin.models import AddEmployee
class Employeeform(forms.ModelForm):
    dis=(('devloper','Devloper'),('tester','Tester'),('manager','Manager'),('human resourse','Human Resourse'))
    disignation = forms.ChoiceField(choices=dis)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AddEmployee
        fields="__all__"

