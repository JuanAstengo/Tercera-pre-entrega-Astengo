from django.shortcuts import render, redirect # type: ignore
from .forms import UsuarioForm, LibroForm, PrestamoForm, BusquedaLibroForm
from .models import Libro

def index(request):
    return render(request, 'biblioteca/index.html')

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'biblioteca/agregar_usuario.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})

def agregar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/agregar_prestamo.html', {'form': form})

def buscar_libro(request):
    form = BusquedaLibroForm(request.GET or None)
    if form.is_valid():
        libro = form.cleaned_data.get('libro')
        if libro:
            libros = Libro.objects.filter(id=libro.id)
        else:
            libros = Libro.objects.all()
    else:
        libros = Libro.objects.all()

    return render(request, 'biblioteca/buscar_libro.html', {'form': form, 'libros': libros})
