from  django import forms
from .models import  RegistrationModel
from .models import ApplicationformModel

class RegistrationForm(forms.ModelForm):
      gen=(("Male","male"),("Female","female"))
      years=[x for x in range(1987,2022)]
      date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years=years))
      gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
      password=forms.CharField(widget=forms.PasswordInput)
      class Meta:
          model=RegistrationModel
          fields='__all__'

class ApplicationForm(forms.ModelForm):
    gen = (("Male", "male"), ("Female", "female"))
    quali=(("Bca","bca"),("Mca","mca"))
    years = [x for x in range(1987, 2021)]
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=years))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
    qualification=forms.ChoiceField(choices=quali)
    class Meta:
        model=ApplicationformModel
        fields='__all__'



