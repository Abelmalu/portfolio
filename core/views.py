from django.shortcuts import render,redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
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
    return render(request, 'core/base_layout.html', context)