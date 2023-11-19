from django import forms
from .models import Course, Student, Course_Join

class AddCourseForm(forms.ModelForm):

    class Meta:
      
        model = Course
        fields = ('cname','cduration',)
