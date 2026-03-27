from django.shortcuts import render, get_object_or_404
from .models import Message
from items.models import Item

def chat_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    receiver = item.user   # 👈 item owner

    messages = Message.objects.filter(item=item)

    if request.method == "POST":
        msg = request.POST.get("message")

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            item=item,
            message=msg
        )

    return render(request, "chat.html", {
        "messages": messages,
        "item": item
    })