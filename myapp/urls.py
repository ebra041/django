from django.urls import path
from .views import AddCourseView, CourseListView, CourseDetailsView, SearchCourseView, CourseRedirectView,  CourseListTemplate
from .views import EditCourseView, CourseListCreate

urlpatterns = [
    #path('members/', views.members, name = 'members'),
    path('add/', AddCourseView.as_view(), name = 'addcourse'),
    path('courses/', CourseListView.as_view(), name ='courses'),
    path('course/<int:pk>', CourseDetailsView.as_view(),name='course'),
    path('coursesearch/<str:cname>', SearchCourseView.as_view() ,name='coursesearch'),
    path('redirect/<int:pk>', CourseRedirectView.as_view(), name = 'redirect'),
    path('templatecourses/', CourseListTemplate.as_view(), name ='coursestemplate'),
    path('editcourse/<int:pk>', EditCourseView.as_view(),name='editcourse'),
    path('courses/api/', CourseListCreate.as_view()),
]
