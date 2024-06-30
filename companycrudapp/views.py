from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from companycrudapp.models import Company


# Create your views here.
class CompanyListView(ListView):
    model = Company


class CompanyDetailView(DetailView):
    model = Company


class CompanyCreateView(CreateView):
    model = Company
    fields = ('companyname', 'ceo', 'headquarters', 'foundedyear','typeofcompany','primaryindustry')


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('companyname', 'ceo','typeofcompany','primaryindustry')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('home')
