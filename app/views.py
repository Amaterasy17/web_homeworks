from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

questions = [
    {'id': i, 'title': f'question # {i}', 'Author': f'NickName # {i}', 'Likes': i + i * i, 'DisLikes': i, 'rating': i * i} 
    for i in range(50)
]

answers = [
    {'id': i, 'title': f'answer # {i}','Author': f'NickName # {i}', 'Likes': i + i * i, 'DisLikes': i, 'rating': i * i}
    for i in range(20)
]

quest = {
    i: {'id': i, 'title': f'question # {i}', 'Author': f'NickName # {i}','Likes': i + i * i, 'DisLikes': i, 'rating': i * i}
    for i in range(50)
}



def index(request):
        question = pagination(questions, request)
        return render(request,'index.html',{
        'questions': question,
        'nick': question,
        'title': 'New questions',
        })

        

def login(request):
    return render(request,'login.html',{
        'title': 'Log in',
    })


def question(request, gid):
    question = quest.get(gid)
    answer = pagination(answers,request)
    return render(request,'one_question.html',{
        'questions': answer,
        'question': question,
        'nick': question,
        'answers': answer,
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


def settings(request, gid):
    return render(request,'settings.html',{
    'title': 'Settings',
    })


def pagination(object_list, request, count_pages = 5):
    page = request.GET.get('page')
    all_pages = Paginator(object_list, count_pages)

    try:
        content = all_pages.page(page) 
    except PageNotAnInteger:
        content = all_pages.page(1)
    except EmptyPage:
        content = pages.page(all_pages.num_pages)
    return content
    

