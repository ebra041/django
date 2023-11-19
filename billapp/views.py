from django.shortcuts import render
from .models import Food, Bill, BillOrders
from .forms import FoodForm, AddFoodBillForm

# Create your views here.
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView,UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name='home.html'

class AddFoodView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Food
    form_class = FoodForm
    success_url = '/addfood'
    template_name = 'addfood.html'
    
class FoodListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model=Food
    template_name='foods.html'
    context_object_name='foods'
    paginate_by=2
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class FoodDetailsView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model=Food
    template_name='food.html'
    context_object_name='food'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class EditFoodView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Food
    form_class = FoodForm
    success_url = '/foods'
    template_name = 'addfood.html'
    
class DeleteFoodView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Food
    success_url = '/foods'
    template_name = 'foodconfirmdelete.html'

class AddBillView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Bill
    form_class = AddFoodBillForm
    success_url = '/addbill'
    template_name = 'addfoodtobill.html'
    
class UpdateBillView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Bill
    form_class = AddFoodBillForm
    success_url = '/addbill'
    template_name = 'addfoodtobill.html'
    
class BillDetailsView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model=Bill
    template_name='bill.html'
    context_object_name='bill'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        billid = self.get_object().pk
        context['foods'] = BillOrders.objects.filter(bill = billid)
        return context
    
class BillListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model=Bill
    template_name='bills.html'
    context_object_name='bills'
    paginate_by=2
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
