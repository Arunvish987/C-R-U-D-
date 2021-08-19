from django.shortcuts import render, redirect
from . forms import UserForm
from . models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Create your views here.

class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = UserForm()
        stud = User.objects.all()
        context = {'std': stud, 'form':fm}
        return context

    def post(self, request):
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        return redirect('/')

class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        form = UserForm(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form':form})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return redirect('/')

class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()

        return super().get_redirect_url(*args, **kwargs)


