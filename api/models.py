from django.db import models
from django.contrib.auth.models import User

# Note is a model that represents a note
# title is a field that stores the title of the note
# content is a field that stores the content of the note
# author is a field that stores the author of the note
# created_at is a field that stores the date and time the note was created
# updated_at is a field that stores the date and time the note was last updated
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # __str__ is a method that returns a string representation of the object
    def __str__(self):
        return self.title
