from django.shortcuts import render , redirect
from item.models import items,categories
from .forms import SignUpForm
# Create your views here.
def index(request):
    items_ = items.objects.filter(is_sold = False)[0:6]
    print(f"Items:{items}")
    categories_ = categories.objects.all()
    return render(request,'core/index.html',{
        'categories':categories_,
        'items':items_
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request,'core/signup.html',{
        'form':form
    })