from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TypeListView(TemplateView):
    template_name = "delivery_letter/type_list.html"
