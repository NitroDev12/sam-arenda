from django.shortcuts import render, redirect
from .models import Skuter
from .forms import SkuterForm

def home(request):
    skuterlars = Skuter.objects.all()
    return render(request, 'index.html', {'skuterlars': skuterlars})


def skuter_qosh(request):
    if request.method == "POST":
        form = SkuterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # ← endi skuter_list emas, index
    else:
        form = SkuterForm()
    return render(request, 'skuterqosh.html', {'form': form})
