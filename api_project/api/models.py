from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
    

class author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    class Meta:
        permissions = [
            ("can_add_author", "Can add author"),
            ("can_change_author", "Can change author"),
            ("can_delete_author", "Can delete author"),
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['id', 'title', 'author', 'published_date', 'isbn']

# Settings for Django REST Framework
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },