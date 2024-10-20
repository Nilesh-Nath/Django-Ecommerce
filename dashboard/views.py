from django.shortcuts import render

# Create your views here.
from item.models import items
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items_ = items.objects.filter(created_by = request.user)
    
    return render(request,'dashboard/index.html',{
        'items':items_
    })