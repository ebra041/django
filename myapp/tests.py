from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import AddCourseView, CourseDetailsView
from .models import Student, Course, Course_Join
from .forms import AddCourseForm

# Create your tests here.
class TestURL(SimpleTestCase):
    def test_add_url(self):
        url = reverse('addcourse')
        self.assertEquals(resolve(url).func.view_class, AddCourseView)
    
    def test_course_url(self):
        url = reverse('course', args=[1])
        self.assertEquals(resolve(url).func.view_class, CourseDetailsView)

class TestViews(TestCase):
    def test_addcourse_view(self):
        url = reverse('addcourse')
        client = Client()
        Course.objects.create(cname='cp', cduration = 10)
        response = client.post(url, {'cname':'flutter', 'cduration': 15})
        course2 = Course.objects.get(id=2)
        self.assertEquals(course2.cname, 'flutter')
        response2 = client.get(url)
        self.assertEquals(response2.status_code, 200)
        self.assertTemplateUsed(response2, 'addcourse.html')

class TestModels(TestCase):
    def test_course_join(self):
        student1 = Student.objects.create(fname='ibrahim', sname = 'zomorod')
        course1 = Course.objects.create(cname='cp', cduration = 10)
        course_join1 = Course_Join.objects.create(sid=student1, cid=course1)
        self.assertEquals(course_join1.__str__(),'ibrahimzomorodcp')

class TestForm(SimpleTestCase):
    def form_valid(self):
        form = AddCourseForm(data={'cname':'java', 'cduration':10})
        self.assertTrue(form.is_valid())