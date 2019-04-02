from django.conf.urls import url

from . import views

#define url`s schemes for learning_logs

urlpatterns = [
        #Home page
        url(r'^$', views.index, name='index')
        ]
