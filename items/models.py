from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('lost', 'Lost'),
    ('found', 'Found'),
)

CATEGORY_CHOICES = (
    ('electronics', 'Electronics'),
    ('clothes', 'Clothes'),
    ('stationary', 'Stationary'),
    ('others', 'Others'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items/')  # MEDIA_ROOT/items/
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='others')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_matching_items(self):
        """
        Returns a list of matching items (opposite status, same category, same title)
        Each item in list has a unique room_name to prevent duplicate chat rooms
        """
        opposite_status = 'found' if self.status == 'lost' else 'lost'
        matches = Item.objects.filter(
            status=opposite_status,
            category=self.category,
            title__iexact=self.title  # case-insensitive match
        ).exclude(user=self.user)

        result = []
        for match in matches:
            room_name = f"match_{min(self.id, match.id)}_{max(self.id, match.id)}"
            result.append(
                type('obj', (object,), {'room_name': room_name, 'title': match.title})()
            )
        return result