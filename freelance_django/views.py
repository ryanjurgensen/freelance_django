from django.views.generic.base import TemplateView, View
from .models import *

class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['portfolio_items'] = PortfolioItem.objects.all()[:6]
		context['total_portfolio_count'] = PortfolioItem.objects.count() - 6
		return context

class PortfolioView(TemplateView):
	template_name = "portfolio.html"

	def get_context_data(self, **kwargs):
		context = super(PortfolioView, self).get_context_data(**kwargs)
		context['portfolio_items'] = PortfolioItem.objects.all()
		return context
