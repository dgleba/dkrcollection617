from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Notes", api.NotesViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("hedgedoc/Notes/", views.NotesListView.as_view(), name="hedgedoc_Notes_list"),
    path("hedgedoc/Notes/create/", views.NotesCreateView.as_view(), name="hedgedoc_Notes_create"),
    path("hedgedoc/Notes/detail/<int:pk>/", views.NotesDetailView.as_view(), name="hedgedoc_Notes_detail"),
    path("hedgedoc/Notes/update/<int:pk>/", views.NotesUpdateView.as_view(), name="hedgedoc_Notes_update"),
    path("hedgedoc/Notes/delete/<int:pk>/", views.NotesDeleteView.as_view(), name="hedgedoc_Notes_delete"),

)
