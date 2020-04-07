from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

questions = [
    {'id': i, 'title': f'question # {i}'}
    for i in range(5)
]

answers = [
    {'id': i, 'title': f'answer # {i}'}
    for i in range(3)
]

quest = {
    i: {'id': i, 'title': f'question # {i}'}
    for i in range(5)
}



def index(request):
    return render(request,'index.html',{
        'questions': questions,
        'title': 'New questions',
    })

def login(request):
    return render(request,'login.html',{
        'title': 'Log in',
    })


def question(request, gid):
    question = quest.get(gid)
    return render(request,'one_question.html',{
        'question': question,
        'answers': answers,
        'title': f'Question # {gid}',
    })

def sign_up(request):
    return render(request,'sign_up.html',{
    'title': 'Registration',
    })


def ask(request):
    return render(request,'ask.html',{
    'title': 'Ask me',
    })


def settings(request):
    return render(request,'settings.html',{
    'title': 'Settings',
    })