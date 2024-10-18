from django.urls import path
from .views import *

urlpatterns = [
    path('rv/',registration_view, name='registration_url'),
    path('srv/',show_registration_view, name='show_registration_view_url'),
    path('uv/<str:nm>/',update_view,name='update_view_url'),
    path('dv/<str:nm>/',delete_view,name='delete_view_url'),

    path('vrv/',voter_registration_view, name='voter_registration_url'),
    path('vsvrv/',voter_show_registration_view, name='voter_show_registration_view_url'),
    path('vuv/<str:nm>/',voter_update_view, name='voter_update_view_url'),
    path('vdv/<str:nm>/',voter_delete_view, name='voter_delete_view_url'),


    path('vf/',voter_view,name='voter_view_url'),
    path('mvf/',voteing_view,name='voteing_view_url'),
    path('vc/',votingcomplete_view,name='votingcomplete_view_url'),
    path('scv/',showcompletedvote_view,name='showcompletedvote_view_url'),
    path('uscv/',update_completedvote_view,name='update_completedvote_view_url'),
    path('sr/',show_result_view,name='show_result_view_url'),
    path('urv/',update_result_view,name='update_result_view_url')

]