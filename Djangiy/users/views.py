from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm
from blog.models import Post
from django.conf import settings


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-id')[:5]

    return render(request, 'index.html', {'posts': posts})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        contex = {
            'form': form
        }
        return render(request, self.template_name, contex)

