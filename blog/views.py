from django.shortcuts import render, redirect
from .forms import SkuterForm

# Create your views here.

def home(request):
    return render(request, "index.html")

def skuter_qosh(request):
    if request.method == "POST":
        form = SkuterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Saqlangach, kerak bo'lsa boshqa sahifaga yo'naltirish:
            return redirect('skuter_list')  # skuter_list nomli URL bo'lsa ishlaydi; aks holda o'zgartiring
    else:
        form = SkuterForm()
    return render(request, 'skuterqosh.html', {'form': form})
