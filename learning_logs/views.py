from django.shortcuts import render

def index(request):
    '''Home page of learning log app.'''
    return render(request, 'learning_logs/index.html')

# Create your views here.
