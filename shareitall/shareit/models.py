from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ForumPost(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()  # Add this field if it's missing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line

    def __str__(self):
        return self.title

class Comment(models.Model):
    forum_post = models.ForeignKey('ForumPost', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()  # Make sure this field exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.forum_post.title}"


class ProductListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='listings/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_phone_number = models.CharField(max_length=15, default='0000000000')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='M-Pesa')  # Payment method like M-Pesa or PayPal
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} - {self.amount} KES"