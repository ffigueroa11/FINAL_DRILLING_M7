from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm


def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio_list.html', {'laboratorios': laboratorios})


def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio_form.html', {'form': form})


def laboratorio_edit(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio_form.html', {'form': form})


def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_list')
    return render(request, 'laboratorio_confirm_delete.html', {'laboratorio': laboratorio})


def laboratorio_detail(request, pk):

    laboratorio = get_object_or_404(Laboratorio, pk=pk)


    return render(request, 'laboratorio_detail.html', {'laboratorio': laboratorio})