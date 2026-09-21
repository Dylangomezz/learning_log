from django.shortcuts import render

def index(request):
    """"Pagina principal do Learning_log"""
    return render(request, 'learning_logs/index.html')