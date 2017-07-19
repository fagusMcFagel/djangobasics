# mysite\books\urls.py

from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^search/$', views.search)
    ## NOT NEEDED DUE TO UPDATED VIEW search(request) ##
    #url(r'^search-form/$', views.search_form),
]