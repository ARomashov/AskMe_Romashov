from urllib.request import Request

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage


QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(1, 30)
]

AUTH_USER =  {
        'login' : 'valera228',
        'email' : 'valera228@mail.ru',
        'nickname' : 'Valera',
        'avatar' : '/img/user_logo.png'
    }


ANSWERS = [
    {
        'answer': f'Answer {i}',
        'user_avatar': '/img/user_logo.png'
    } for i in range(1, 4)
]

TAGS = [f'Tag {i}' for i in range(1, 4)]

def paginate(objects_list, request, per_page=10):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, per_page)
    try:
        page = paginator.page(page_num)
    except InvalidPage:
        raise Http404("Страница не найдена")
    return page

def index(request):
    page = paginate(QUESTIONS, request, 10)
    return render(
        request, 'index.html', context={'questions': page.object_list, 'tags': TAGS, 'page_obj': page})

def hot(request):
    hot_questions = QUESTIONS[::-1]
    page = paginate(hot_questions, request, 10)
    return render(
        request, 'hot.html', context={'questions': page.object_list, 'tags': TAGS, 'page_obj': page})

def tag(request, tag_name):
    page = paginate(QUESTIONS, request, 5)
    return render(
        request, 'tag.html', context={'questions': page.object_list, 'tag':tag_name, 'tags': TAGS, 'page_obj': page})

def question(request, question_id):
    question = QUESTIONS[question_id-1]
    return render(
        request, 'question.html', context={'question': question, 'answers': ANSWERS, 'tags': TAGS})

def login(request):
    return render(
        request, 'login.html')

def signup(request):
    return render(
        request, 'signup.html')

def ask(request):
    return render(
        request, 'ask.html')

def settings(request):
    return render(
        request, 'settings.html', context={'user': AUTH_USER}
    )

def err404(request):
    return HttpResponse('Error 404')