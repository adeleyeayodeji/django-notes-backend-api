from django.urls import path
from . import views

urlpatterns = [
    #note list
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    #note delete
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="note-delete"),
]
