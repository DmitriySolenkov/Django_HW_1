from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Это главная страница моего проекта Django</h1><p>А тут какой-то контент</p>')


def about(request):
    return HttpResponse('<h1>Обо мне</h1><h2>Имя: Дмитрий</h2> <h2>Возраст: 26</h2><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum quis et ratione sunt quasi non soluta laborum unde, sint perspiciatis odio laboriosam ex impedit ut accusamus quod architecto eos quos dolorem ipsa. Deleniti ad qui error unde adipiscimagni delectus, vero soluta consequatur fugit? Obcaecati dolorem quam quas qui sed.</p>')
