# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView

from .models import identities

# Create your views here.


class HomeView(TemplateView):
    template_name='home.html'

class Info(ListView):
    model = identities
    template_name = 'ipmac.html'
    context_object_name = "objects"
