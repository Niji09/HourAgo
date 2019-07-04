from django import template
from datetime import datetime
from django.utils.html import mark_safe

#register object
register = template.Library()

# sencond way : decorator
@register.filter(name='nicedate')
def nicedate(value):
	"""
	This function will change the given date and replace it with nice readable date format. 
	"""
	date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
	return date

@register.filter(name='startswith')
def startswith(content):
	"""
	This function will if text starts with "[[getSimpleString(data.title)]]" string and 
	return boolean value
	"""
	comapre_str = "[[getSimpleString(data.title)]]"
	if content.startswith(comapre_str):
		return False
	else:
		return True

@register.filter(name='videoid')
def videoid(url):
	"""
	This function will cut the youtube video id from youtube url
	"""
	vid_id = url[url.find('=')+1:]
	return vid_id

@register.filter(name='rmdigit')
def rmdigit(content):
	"""
	This function will cut the contents last digits.
	"""
	return content[:len(content)-15]


@register.filter(name='rmsource')
def rmsource(title):
	"""
	This function will cut the contents last digits.
	"""
	return title[:title.rfind('-')]


@register.filter(name='htmlconvert')
def htmlconvert(text):
	"""
	This function will encode html element in html text.
	"""
	return mark_safe(text)

@register.filter(name='percetage')
def percetage(score):
	"""
	This function convert simple score into percetage score
	"""
	return float(score)/8*100