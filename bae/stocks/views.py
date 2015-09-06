from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Symbol

import PythonAlg

def index(request):
	price_list = Symbol.objects.all()
	price_list = PythonAlg.__init__
	template = loader.get_template('stocks/index.html')
	context = RequestContext(request, {
		'price_list': price_list,
		})
	return HttpResponse(template.render(context))

def detail(request, symbol):
	template = loader.get_template('stocks/detailz.html')
	context = RequestContext(request, {
		'symbol': symbol,
		})
	return HttpResponse(template.render(context))
