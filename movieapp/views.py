import urllib.parse
from  urllib.request import urlopen
import json
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView) # vaated mida kasutame
from django.conf import settings
from .models import * # kõik mudelid
from django.urls import reverse_lazy
# Create your views here.


class HomeView(TemplateView):
    template_name = "movieapp/index.html"


class SearchView(TemplateView):
    template_name = "movieapp/search.html"

class SearchResultView(ListView):
    template_name = "movieapp/search_result.html"
    model = Country
    table = None

    def get_queryset(self):
        object_list =[]
        query = self.request.GET.get("search_phrase")
        self.table = self.request.GET.get("choose_table")

        if self.table == "country_valik":
           object_list = Country.objects.filter(common__icontains=query)

        elif self.table == "movie_valik":
            value = urllib.parse.quote(query)
            search = "s=" + value
            result = "&".join([settings.OMDB_URL, search])
            print(result) # näita url konsoolis
            response = urlopen(result)
            data = json.loads(response.read())
            if data["Response"] == "True":
                for obj in data["Search"]:
                    object_list.append(obj)
                    Movie.objects.get_or_create(title=obj["Title"], year=obj["Year"],
                                                imdbid=obj["imdbID"], type=obj["Type"], poster=obj["Poster"])


        return object_list # tagastab otsingu tulemuse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["choose_table"] = self.table
        return context

class CountryListView(ListView):
    model = Country
    # päringud common alt sorteeritakse
    queryset = Country.objects.order_by("common")
    context_object_name = "countries"
    paginate_by = 10  # mitu rida lehel kuvab

class CountryDetailView(DetailView):
    model = Country

class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.order_by("title")
    context_object_name = "movies"
    paginate_by = 10

class MovieDetailView(DetailView):
    model = Movie