from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Item
from .forms import ItemForm


# Create your views here.
def home(request):
    return HttpResponse("Home")

def index(request):
    item_list = Item.objects.all()

    item_name = request.GET.get("item_name")
    if( item_name != "") and (item_name is not None):
        item_list = item_list.filter(item_name__icontains=item_name)
    
    paginator = Paginator(item_list, 3)
    page = request.GET.get("page")
    item_list = paginator.get_page(page)
    
    context = {
        "item_list": item_list,
    }
    
    return render(request, "item/index.html", context)

def item(request):
    return HttpResponse("item view")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context = {
        "item": item,
    }

    return render(request, "item/detail.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("item:index")
    
    context ={
        "form": form
    }
    
    return render(request, "item/item-form.html", context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("item:index")
    
    context = {
        "form": form,
        "item": item,
    }
    
    return render(request, "item/item-form.html", context)

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == "POST":
        item.delete()
        return redirect("item:index")
    
    context = {
        "item": item,
    }
    
    return render(request, "item/delete-item.html", context)