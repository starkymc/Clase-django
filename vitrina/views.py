from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from vitrina.models import Books

# Create your views here.

class BookList(ListView):
    model = Books
    template_name = 'booklist.html'

class BootstrapEj(View):
   def get(self,request):
        return render(request, 'ejemplo_bootstrap.html')
    
