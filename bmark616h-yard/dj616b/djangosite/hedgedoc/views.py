from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class NotesListView(generic.ListView):
    model = models.Notes
    form_class = forms.NotesForm


class NotesCreateView(generic.CreateView):
    model = models.Notes
    form_class = forms.NotesForm


class NotesDetailView(generic.DetailView):
    model = models.Notes
    form_class = forms.NotesForm


class NotesUpdateView(generic.UpdateView):
    model = models.Notes
    form_class = forms.NotesForm
    pk_url_kwarg = "pk"


class NotesDeleteView(generic.DeleteView):
    model = models.Notes
    success_url = reverse_lazy("hedgedoc_Notes_list")
