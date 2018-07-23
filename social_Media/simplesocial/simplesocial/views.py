from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
	template_name='index.html'

class ThanksPage(TemplateView):
	template_name='thanks.html'

class TestPage(TemplateView):
	template_name = 'test.html'