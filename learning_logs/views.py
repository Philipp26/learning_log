from django.shortcuts import render
from .models import Topic
def index(request):
    '''Home page of learning log app.'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.oblects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

# Create your views here.
