from hashlib import new
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Chapter, Sister, Pnm, Nickname_Request
from django.views.generic import ListView
from . forms import Nickname_RequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# Define the home view

#####################################
############## Chapter ##############
#####################################

class ChapterCreate(LoginRequiredMixin, CreateView):
    model = Chapter
    fields = ['name', 'chapter_school', 'city_state', 'original_founding_date']


class ChapterUpdate(LoginRequiredMixin, UpdateView):
    model = Chapter
    fields = '__all__'


class ChapterList(LoginRequiredMixin, ListView):
    model = Chapter

#####################################
############## Sister ###############
#####################################


class SisterCreate(LoginRequiredMixin, CreateView):
    model = Sister
    fields = '__all__'


class SisterUpdate(LoginRequiredMixin, UpdateView):
    model = Sister
    fields = '__all__'


class SisterList(LoginRequiredMixin, ListView):
    model = Sister


#####################################
################ PNM ################
#####################################


class PnmCreate(LoginRequiredMixin, CreateView):
    model = Pnm
    fields = '__all__'


class PnmUpdate(LoginRequiredMixin, UpdateView):
    model = Pnm
    fields = '__all__'


class PnmList(LoginRequiredMixin, ListView):
    model = Pnm


#####################################
######### Nickname_Request ##########
#####################################


class Nickname_RequestUpdate(LoginRequiredMixin, UpdateView):
    model = Nickname_Request
    fields = '__all__'


class Nickname_RequestDetail(LoginRequiredMixin, DetailView):
    model = Nickname_Request
    fields = '__all__'


class Nickname_RequestList(LoginRequiredMixin, ListView):
    model = Nickname_Request

#####################################
#####################################
#####################################


@login_required
def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    sisters_within_chapter = Sister.objects.filter(chapter_id=chapter_id)
    try:
        pnms_within_chapter = Pnm.objects.filter(chapter_id=chapter_id)
    except:
        pnms_within_chapter = None
    return render(request, 'chapters/detail.html', {
        'chapter': chapter,
        'sisters': sisters_within_chapter,
        'pnms': pnms_within_chapter
    })


@login_required
def sister_detail(request, sister_id):
    sister = Sister.objects.get(id=sister_id)

    try:
        little = Sister.objects.get(big_sister=sister_id)
    except:
        little = None

    try:
        pnm_little = Pnm.objects.filter(big_sister=sister_id)
    except:
        pnm_little = None

    return render(request, 'sisters/detail.html', {
        'sister': sister,
        'little': little,
        'pnm': pnm_little
    })


@login_required
def pnm_detail(request, pnm_id):
    pnm = Pnm.objects.get(id=pnm_id)
    try:
        nicknames_requested_for_pnm = Nickname_Request.objects.filter(
            pnm_id=pnm_id)
    except:
        nicknames_requested_for_pnm = None
    return render(request, 'pnms/detail.html', {
        'pnm': pnm,
        'nickname_requests': nicknames_requested_for_pnm
    })


@login_required
def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    sisters_within_chapter = Sister.objects.filter(chapter_id=chapter_id)
    try:
        pnms_within_chapter = Pnm.objects.filter(chapter_id=chapter_id)
    except:
        pnms_within_chapter = None
    return render(request, 'chapters/detail.html', {
        'chapter': chapter,
        'sisters': sisters_within_chapter,
        'pnms': pnms_within_chapter
    })


@login_required
def pnm_index(request):
    pnm = Pnm.objects.all()
    nickname_requests = Nickname_Request.objects.all()
    return render(request, 'pnms/index.html', {
        'pnm': pnm,
        'nickname_requests': nickname_requests
    })


@login_required
def nickname_request_create(request, pnm_id, *msg):
    pnm = Pnm.objects.get(id=pnm_id)
    nickname_request_form = Nickname_RequestForm()
    return render(request, 'nickname_requests/create.html', {
        'pnm': pnm,
        'form': nickname_request_form,
        'msg': msg,
    })


def more_than_three_nickname_requests(pnm_id):
    if len(Nickname_Request.objects.filter(pnm_id=pnm_id)) >= 3:
        return True


def check_nickname_against_roster(name):
    if Sister.objects.filter(nickname=name):
        return True
        # elif Sister.objects.filter(nickname=new_nickname_request.name.lower()) or Sister.objects.filter(nickname=new_nickname_request.name.upper()) or Sister.objects.filter(nickname=new_nickname_request.name.title()):
        #     return nickname_request_create(request, pnm_id, "cannot request a nickname already in use with different letter casing")
        # elif ('0' or '1' or '3' or '9' in new_nickname_request.name):
        #     if Sister.objects.filter(nickname=new_nickname_request.name.replace('0', 'o')):
        #         return nickname_request_create(request, pnm_id, "request is similar to a nickname already in use")


@login_required
def add_nickname_request(request, pnm_id, sister_id):
    form = Nickname_RequestForm(request.POST)
    if form.is_valid():
        new_nickname_request = form.save(commit=False)
        if more_than_three_nickname_requests(pnm_id):
            return nickname_request_create(request, pnm_id, "The max allowance for nickname reservations per PNM is 3")
        if check_nickname_against_roster(new_nickname_request.name):
            return nickname_request_create(request, pnm_id, "nickname request is similar to nicknames in our directory")
        else:
            new_nickname_request.pnm_id = pnm_id
            new_nickname_request.requestor_id = sister_id
            new_nickname_request.nickname_approval_status = 'RE'
            new_nickname_request.save()
            return redirect(f'/pnms/{pnm_id}')
