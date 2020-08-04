from django import forms
from .models import New_reqModel



class New_reqForm(forms.ModelForm):
    years = [x for x in range(2015,2022)]
    registratin_start_from = forms.DateField(widget=forms.SelectDateWidget(years=years))
    last_day_apply=forms.DateField(widget=forms.SelectDateWidget(years=years))

    class Meta:
        model=New_reqModel
        fields="__all__"



