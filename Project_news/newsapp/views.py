from django.shortcuts import render
from django.http import HttpResponse
from newsapp import models
from django.db.models import Q
# Create your views here.

def general(request):
	data = models.Top_headline.objects.filter(category='general').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def business(request):
	data = models.Top_headline.objects.filter(category='business').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def entertainment(request):
	data = models.Top_headline.objects.filter(category='entertainment').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def health(request):
	data = models.Top_headline.objects.filter(category='health').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def science(request):
	data = models.Top_headline.objects.filter(category='science').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def sports(request):
	data = models.Top_headline.objects.filter(category='sports').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def technology(request):
	data = models.Top_headline.objects.filter(category='technology').order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)


def searchNews(request):
	# create empty queryset object
	mq = Q()

	for i in request.GET.get('q').split():
		mq = mq | Q(title__icontains=i) | Q(description__icontains=i) | Q(source_name__icontains=i)

	data = models.Top_headline.objects.filter(mq).order_by('-publishedAt')[:30]
	context = {'data': data, 'search_query':request.GET.get('q')}
	return render(request, 'newsapp/news_base.html', context)


def newsSource(request):
	mq = Q()
	source = models.Top_headline.objects.values('source_name').distinct()
	
	for i in range(source.count()):
		mq = mq | Q(name__iexact=source[i]['source_name'])

	data = models.NewsSource.objects.filter(mq).order_by('name')
	context = {'data': data,}
	return render(request, 'newsapp/news_source.html', context)


def searchSource(request):
	query = request.GET.get('q')
	data = models.Top_headline.objects.filter(Q(source_name__icontains=query)
		).order_by('-publishedAt')[:30]
	context = {'data': data, 'search_query': query}
	return render(request, 'newsapp/news_base.html', context)


def youtubeNews(request):
	data = models.Top_headline.objects.filter(Q(source_name='Youtube.com')
		).order_by('-publishedAt')[:30]
	context = {'data': data}
	return render(request, 'newsapp/news_base.html', context)

def about(request):
	return render(request, 'newsapp/about.html')
