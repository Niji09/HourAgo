from django.contrib import admin
from django.urls import path
from newsapp import views
#namespace
app_name = 'newsapp'

urlpatterns = [
    path('', views.general, name='general'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('health/', views.health, name='health'),
    path('science/', views.science, name='science'),
    path('sports/', views.sports, name='sports'),
    path('technology/', views.technology, name='technology'),
    path('search_result/', views.searchNews, name='search_result'),
    path('news_source/', views.newsSource, name='news_source'),
    path('search_source/', views.searchSource, name='search_source'),
    path('yt_news/', views.youtubeNews, name='yt_news'),
    path('about/', views.about, name='about'),
]