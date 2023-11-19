from django.contrib import admin
from django.urls import path,include
from .views import AddFoodView, AddBillView, HomeView, FoodListView, FoodDetailsView, EditFoodView, DeleteFoodView, UpdateBillView, BillDetailsView, BillListView
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, PwdChangeForm

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name="passwordchangeform.html",form_class=PwdChangeForm), name='passwordchange'),
    path('addfood', AddFoodView.as_view(), name ='addfood' ),
    path('foods', FoodListView.as_view(), name ='foods' ),
    path('food/<int:pk>', FoodDetailsView.as_view(), name ='food' ),
    path('editfood/<int:pk>', EditFoodView.as_view(), name ='editfood' ),
    path('deletefood/<int:pk>', DeleteFoodView.as_view(), name ='deletefood' ),
    path('addbill', AddBillView.as_view(), name ='addbill' ),
    path('editbill/<int:pk>', UpdateBillView.as_view(), name ='editbill' ),
    path('bill/<int:pk>', BillDetailsView.as_view(), name ='bill' ),
    path('bills', BillListView.as_view(), name ='bills' ),

]