from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Symbol


def index(request):
	price_list = Symbol.objects.all()
	template = loader.get_template('stocks/index.html')
	context = RequestContext(request, {
		'price_list': price_list,
		})
	return HttpResponse(template.render(context))
