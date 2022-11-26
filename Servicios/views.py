from django.shortcuts import render, HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.

def login(request):
    return render(request, 'Servicios/login.html')


def register(request):
    return render(request, 'Servicios/register.html')


def home(request):
    
    data = {
        'form': PostForm()
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Post creado"
        else:
            data["form"] = formulario

    return render(request, 'Servicios/home.html', data)

    
def listarPost(request):
        listarPost = Post.objects.all()
        return render(request, 'Servicios/deck.html', {'posts':listarPost})


def deck(request):
    return render(request, 'Servicios/deck.html')


def history(request):
    return render(request, 'Servicios/history.html')