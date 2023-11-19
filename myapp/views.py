from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course, Student, Course_Join
from .forms import AddCourseForm

from .serializers import CourseSerializer
from rest_framework import generics

from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView,UpdateView


# Create your views here.

class AddCourseView(CreateView):
    model = Course
    form_class = AddCourseForm
    success_url = 'courses/'
    template_name = 'addcourse.html'

class CourseListView(ListView):
    model=Course
    template_name='courses.html'
    context_object_name='courses'
    paginate_by=2
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class CourseDetailsView(DetailView):
    model=Course
    template_name='course.html'
    context_object_name='course'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courseid = self.get_object().pk
        students = Course_Join.objects.filter(cid=courseid)
        context['students'] = students
        return context
    
class SearchCourseView(ListView):
    model= Course
    template_name = 'coursesearch.html'
    context_object_name = 'courses'
    paginate_by=2

    def get_queryset(self, *args, **kwargs):
        return Course.objects.filter(cname__icontains = self.kwargs.get('cname'))
    
class CourseRedirectView(RedirectView):
    pattern_name='course'
    # url = 'http://fb.com'
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(**kwargs)
    
class CourseListTemplate(TemplateView):
    template_name='courses.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context
    
class EditCourseView(UpdateView):
    model = Course
    form_class = AddCourseForm
    success_url = 'courses/'
    template_name = 'addcourse.html'

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer