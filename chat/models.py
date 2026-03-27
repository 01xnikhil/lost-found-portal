from django.db import models

from django.contrib.auth.models import User
from items.models import Item   # 👈 LostFound ka model

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # 🔥 MAIN LINK
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)