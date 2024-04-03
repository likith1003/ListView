from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View, FormView, ListView
# Create your views here.

def  insertschoolbyfbv(request):
   ESFO = SchoolForm()
   d = {'ESFO':ESFO}
   if request.method == 'POST':
      SFDO = SchoolForm(request.POST)
      if SFDO.is_valid():
         SFDO.save()
         return HttpResponse('School Created Successfully')
      return HttpResponse('Invalid Data')
   return render(request, 'insertschoolbyfbv.html', d)


class InsertSchoolByCBV(View):
   def get(self,request):
      ESFO = SchoolForm()
      d = {'ESFO':ESFO}
      return render(request, 'InsertSchoolByCBV.html', d)
   
   def post(self,request):
      SFDO = SchoolForm(request.POST)
      if SFDO.is_valid():
         SFDO.save()
         return HttpResponse('School Created Successfully using Class based views')
      return HttpResponse('Invalid Data')
   

class InsertSchoolBYFV(FormView):
   template_name = 'InsertSchoolBYFV.html'
   form_class = SchoolForm
   def form_valid(self, form):
      form.save()
      return HttpResponse('InsertSchoolBYFV is done')
   

def schoolslist(request):
   schools = School.objects.all()
   d = {'schools':schools}
   return render(request, 'schoolslist.html',d)



class School_list(ListView):
   model = School
   context_object_name = 'schools'
   # ordering = ['sprincipal']
   # template_name = 'schoolslist.html'

class School_list(ListView):
   model = Student
   context_object_name = 'schools'
   # ordering = ['sprincipal']
   template_name = 'schoolslist.html'