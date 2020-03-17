from django.shortcuts import render
from django.views.generic import ListView
from .models import Case
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class Cases(CreateView):
    model = Case
    fields = ['confirmed']
    success_url = reverse_lazy('tracker:index')
    template_name = "tracker/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases_confirmed"] = len(Case.objects.filter(confirmed__exact=True))
        context["cases_suspect"] = len(Case.objects.filter(confirmed__exact=False))
        return context
