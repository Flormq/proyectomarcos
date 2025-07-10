
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    cantidad_total = productos.count()
    return render(request, 'productos/lista.html', {
        'productos': productos,
        'cantidad_total': cantidad_total
    })
