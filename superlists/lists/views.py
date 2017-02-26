from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item


def home_page(request):
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST.get('item_text', ''))
        item.save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
