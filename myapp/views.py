from datetime import datetime
from re import template
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from datetime import datetime
from dateutil.relativedelta import relativedelta
from myapp.forms import InputForm, AlumnoForm, ProfesorForm

class index_view(View):
    template = 'index.html'

    def get(self, request):
        context = {}
        context['name'] = 'Gian'
        return render(request, self.template , context)

    def post(self, request):
        return HttpResponse('Soy POST de index_view')

class vista1(View):
    template_get = 'vista1.html'

    def get(self, request):
        fecha_nacimiento = datetime.strptime("24/7/2000", "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        

        #context = {}
        #context['name'] = 'Gian'
        #context["edad"] = edad.years

        context = {
            'name': 'Gian',
            'edad': edad.years
        }

        return render(request, self.template_get, context)


class vista2(View):
    template_get = 'vista2.html'

    def get(self, request):
        lista = [1,2,3,4,5]
        context = {
            'name': 'Gian',
            'list': lista
        }

        return render(request, self.template_get, context)


class form_view(View):
    template_get = 'form.html'
    template_post = 'Hola soy POST de form_view'

    def get(self,request):
        formulario = InputForm()
        context = {'form': formulario}


        return render(request, self.template_get, context)

    def post(self, request):
        form = InputForm(request.POST)
        if form.is_valid():
            #Cleaned_data convierte el dato input html a string
            #request.session['aula'] = str(form.cleaned_data['aula'])
            request.session['hora_entrada'] = str(form.cleaned_data['hora_entrada'])

            return redirect('aula_view', aula=form.cleaned_data['aula'])
            #return HttpResponse('Enviaste el aula ' + form.cleaned_data['aula'] + 
            #' y la hora ' + str(form.cleaned_data['hora_entrada']))


class aula_view(View):
    def get(self, request, aula):
        hora = request.session['hora_entrada']
        return HttpResponse(f'El salon es : {aula},  y la hora es {hora}')


class formAlum(View):
    template_get = 'formAlum.html'

    def get(self,request):
        formulario = AlumnoForm()
        context = {'form': formulario}

        return render(request, self.template_get, context)

    def post(self, request):
        form = AlumnoForm(request.POST)
        if form.is_valid():
            request.session['apellido'] = form.cleaned_data['last_name']
            request.session['aula'] = str(form.cleaned_data['id_aula'])

            return redirect('showAlum', nalumno=form.cleaned_data['first_name'])


class showAlum(View):
    def get(self, request, nalumno):
        apellido = request.session['apellido']
        aula = request.session['aula']
        return HttpResponse(f'El alumno es: {nalumno} {apellido} y su aula es {aula}')


class formProf(View):
    template_get = 'formProf.html'

    def get(self,request):
        formulario = ProfesorForm()
        context = {'form': formulario}

        return render(request, self.template_get, context)

    def post(self, request):
        form = ProfesorForm(request.POST)
        if form.is_valid():
            request.session['apellido'] = form.cleaned_data['last_name']
            request.session['salario'] = str(form.cleaned_data['salario'])

            return redirect('showProf', nombre=form.cleaned_data['first_name'])


class showProf(View):
    def get(self, request, nombre):
        apellido = request.session['apellido']
        salario = request.session['salario']
        return HttpResponse(f'El profesor es: {nombre} {apellido} y su salario es {salario}')

            