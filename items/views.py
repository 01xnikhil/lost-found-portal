# items/views.py
from django.shortcuts import render ,redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
# Agar home page ke liye same template use karna hai
def home(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'items': items})

# All Items page
def all_items(request):

    query = request.GET.get('q')

    if query:
        items = Item.objects.filter(title__icontains=query)
    else:
        items = Item.objects.all()

    context = {
        'items': items
    }

    return render(request, 'all_items.html', context)


@login_required(login_url='/login/')
def add_item(request):

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('/items/')
    else:
        form = ItemForm()

    return render(request, 'add_item.html', {'form': form})
