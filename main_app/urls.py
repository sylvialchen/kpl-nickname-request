from django.urls import path
from . import views
from . views import SisterList, ChapterList, PnmList, Nickname_RequestList

urlpatterns = [

    # Lists
    path('sisters/', SisterList.as_view(), name='sister_index'),
    path('chapters/', ChapterList.as_view(), name='chapter_index'),
    path('pnms/', PnmList.as_view(), name='pnm_index'),
    path('nickname_requests/', Nickname_RequestList.as_view(),
         name='nickname_request_index'),

    # Create
    path('sisters/create/', views.SisterCreate.as_view(), name='sister_create'),
    path('chapters/create/', views.ChapterCreate.as_view(), name='chapter_create'),
    path('pnms/create/', views.PnmCreate.as_view(), name='pnm_create'),
    path('nickname_requests/create/', views.Nickname_RequestCreate.as_view(),
         name='nickname_request_create'),

    # Update
    path('sisters/<int:pk>/update/',
         views.SisterUpdate.as_view(), name='sister_update'),
    path('chapters/<int:pk>/update/',
         views.ChapterUpdate.as_view(), name='chapter_update'),
    path('pnms/<int:pk>/update/',
         views.PnmUpdate.as_view(), name='pnm_update'),
    path('nickname_requests/<int:pk>/update/',
         views.ChapterUpdate.as_view(), name='nickname_request_update'),


    # Detail
    path('chapters/<int:chapter_id>/',
         views.chapter_detail, name='chapter_detail'),
    path('sisters/<int:sister_id>/',
         views.sister_detail, name='sister_detail'),
    path('pnms/<int:pk>/', views.PnmDetail.as_view(), name='pnm_detail'),
    path('nickname_requests/<int:pk>/',
         views.Nickname_RequestDetail.as_view(), name='nickname_request_detail'),
]
