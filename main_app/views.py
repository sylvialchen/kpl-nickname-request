from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Chapter, Sister, Pnm, Nickname_Request
from django.views.generic import ListView

# from .forms import SisterForm
# Create your views here.


# Define the home view

#####################################
############## Chapter ##############
#####################################

class ChapterCreate(CreateView):
    model = Chapter
    fields = ['name', 'chapter_school', 'city_state', 'original_founding_date']


class ChapterUpdate(UpdateView):
    model = Chapter
    fields = '__all__'


class ChapterDetail(DetailView):
    model = Chapter
    template_name = 'chapters/detail.html'


class ChapterList(ListView):
    model = Chapter

#####################################
############## Sister ###############
#####################################


class SisterCreate(CreateView):
    model = Sister
    fields = '__all__'


class SisterUpdate(UpdateView):
    model = Sister
    fields = '__all__'


class SisterList(ListView):
    model = Sister


#####################################
################ PNM ################
#####################################


class PnmCreate(CreateView):
    model = Pnm
    fields = '__all__'


class PnmUpdate(UpdateView):
    model = Pnm
    fields = '__all__'


class PnmDetail(DetailView):
    model = Pnm
    fields = '__all__'


class PnmList(ListView):
    model = Pnm


#####################################
######### Nickname_Request ##########
#####################################

class Nickname_RequestCreate(CreateView):
    model = Nickname_Request
    fields = ['name', 'nickname_meaning', 'pnm']


class Nickname_RequestUpdate(UpdateView):
    model = Nickname_Request
    fields = ['name', 'nickname_meaning', 'pnm']


class Nickname_RequestDetail(DetailView):
    model = Nickname_Request
    fields = '__all__'


class Nickname_RequestList(ListView):
    model = Nickname_Request
