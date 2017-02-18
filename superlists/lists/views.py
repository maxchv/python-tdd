from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def home_page(request):
    new_item = request.POST.get('item_text', '')
    if request.method == 'POST':
        item = Item.objects.create(text=new_item)
        item.save()

    return render(request, 'home.html', {
        'new_item_text': new_item,
    })
