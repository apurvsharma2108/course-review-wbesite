from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=('name','site','type','price','rating','description','realse_Date','image')
