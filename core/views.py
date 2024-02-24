from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            

            return redirect('core:home')

    context = {
        'form':form
    }
    return render(request, 'core/index.html', context)