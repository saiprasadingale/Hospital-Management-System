from django.shortcuts import render, redirect, get_object_or_404
from .forms import HospitalForm
from .models import Hospital


def add(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showurl')
    else:
        form = HospitalForm()

    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)


def show(request):
    data = Hospital.objects.all()
    template_name = 'show.html'
    context = {'data': data}
    return render(request, template_name, context)


def update(request, id):
    obj = get_object_or_404(Hospital, id=id)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showurl')
    else:
        form = HospitalForm(instance=obj)

    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)



def delete(request, id):
    obj = get_object_or_404(Hospital, id=id)
    obj.delete()
    return redirect('showurl')
