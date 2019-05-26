from django.conf.urls import url

from . import views

#define url`s schemes for learning_logs

urlpatterns = [
        #Home page
        url(r'^$', views.index, name='index'),
        #Output all themes
        url(r'^topics/$', views.topics, name='topics'),
        #Output one topic and all entries 
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        #Page for adding new topic
        url(r'^new_topic/$', views.new_topic, name='new_topic'),
        #Page for adding new entry
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
        #Page for editing entries
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, 
            name='edit_entry'),
        ]
