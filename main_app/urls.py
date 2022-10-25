from django.urls import path
from . import views
from . views import SisterList, ChapterList, Nickname_RequestList, PnmList

urlpatterns = [

    # Lists
    path('sisters/', SisterList.as_view(), name='sister_index'),
    path('chapters/', ChapterList.as_view(), name='chapter_index'),
    path('pnms/', PnmList.as_view(), name='pnm_index'),
    path('nickname_requests/', Nickname_RequestList.as_view(),
         name='nickname_request_index'),

    #     path('nickname_requests/', views.nickname_request_index,
    #          name='nickname_request_index'),

    # Create
    path('sisters/create/', views.SisterCreate.as_view(), name='sister_create'),
    path('chapters/create/', views.ChapterCreate.as_view(), name='chapter_create'),
    path('pnms/create/', views.PnmCreate.as_view(), name='pnm_create'),
    path('pnms/nickname_requests/create/<int:pnm_id>', views.nickname_request_create,
         name='nickname_request_create'),
    path('pnms/nickname_requests/create/<int:pnm_id>/<int:sister_id>', views.add_nickname_request,
         name='add_nickname_request'),


    # Update
    path('sisters/<int:pk>/update/',
         views.SisterUpdate.as_view(), name='sister_update'),
    path('chapters/<int:pk>/update/',
         views.ChapterUpdate.as_view(), name='chapter_update'),
    path('pnms/<int:pk>/update/',
         views.PnmUpdate.as_view(), name='pnm_update'),
    path('nickname_requests/<int:nr_id>/approve/',
         views.nickname_request_approve, name='nickname_request_update'),
    path('nickname_requests/<int:nr_id>/queue/',
         views.nickname_request_queue, name='nickname_request_queue'),
    path('nickname_requests/<int:nr_id>/deny/',
         views.nickname_request_deny, name='nickname_request_deny'),



    # Detail
    path('chapters/<int:chapter_id>/',
         views.chapter_detail, name='chapter_detail'),
    path('sisters/<int:sister_id>/',
         views.sister_detail, name='sister_detail'),
    path('pnms/<int:pnm_id>/', views.pnm_detail, name='pnm_detail'),
    path('nickname_requests/<int:pk>/',
         views.Nickname_RequestDetail.as_view(), name='nickname_request_detail'),
]
