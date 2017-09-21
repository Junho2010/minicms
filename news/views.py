# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Column,Article

def index(request):
    columns = Column.objects.all()
    return render(request,'index.html', {'columns':columns})

def column_detail(request,pk,column_slug):
    column = Column.objects.get(pk=pk)
    return render(request, 'news/column.html', {'column':column})

def article_detail(request,pk,article_slug):
    article = Article.objects.get(pk=pk)
    return render(request,'news/article.html', {'article':article})
