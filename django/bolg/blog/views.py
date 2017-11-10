# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from . import models

from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def detail(request, article_id):
    detail = models.Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'detail': detail})


def edit(request, article_id):
    print str(article_id)
    if str(article_id) == '0':
        print 11111111111
        return render(request, 'edit.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'edit.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', 0)
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/blog/')
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return HttpResponseRedirect('/blog/')

