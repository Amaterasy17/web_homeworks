from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

tags = [
    {'id': i,'tag': f'tag{i}'}
    for i in range(5)
] 

questions = [
    {'id': i, 'title': f'question # {i}', 'Author': f'NickName # {i}', 'Likes': i + i * i, 'DisLikes': i, 'rating': i * i,
     'tags': random.choices(tags, k=random.randint(1,2))  } 
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
        'tags': tags,
        'content': question,
        'questions': question,
        'nick': question,
        'title': 'New questions',
        })

        

def login(request):
    return render(request,'login.html',{
        'tags': tags,
        'title': 'Log in',
    })


def question(request, gid):
    question = quest.get(gid)
    answer = pagination(answers,request)
    return render(request,'one_question.html',{
        'tags': tags,
        'content': answer,
        'question': question,
        'nick': question,
        'answers': answer,
        'title': f'Question # {gid}',
    })

def sign_up(request):
    return render(request,'sign_up.html',{
    'tags': tags,
    'title': 'Registration',
    })


def ask(request):
    return render(request,'ask.html',{
     'tags': tags,
    'title': 'Ask me',
    })


def settings(request):
    return render(request,'settings.html',{
    'tags': tags,
    'title': 'Settings',
    })



     

def hot(request):
        questions.sort(key=lambda x: x["rating"])
        questions.reverse()
        question = pagination(questions, request)
        return render(request,'index.html',{
        'tags': tags,
        'content': question,
        'questions': question,
        'nick': question,
        'title': 'New questions',
        })




def tag(request, cur_tag):
    question = pagination(list(filter(lambda x: cur_tag in x['tags'][0]['tag'], questions)),request)
    return render(request,'index.html',{
        'tags': tags,
        'content': question,
        'questions': question,
        'nick': question,
        'title': 'New questions',
        })

def pagination(object_list, request, count_pages = 5):
    page = request.GET.get('page')
    all_pages = Paginator(object_list, count_pages)

    try:
        content = all_pages.page(page) 
    except PageNotAnInteger:
        content = all_pages.page(1)
    except EmptyPage:
        content = all_pages.page(all_pages.num_pages)
    return content