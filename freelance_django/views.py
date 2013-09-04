from django.views.generic.base import TemplateView, View
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import PortfolioItem, ContentItem

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

class ContentView(TemplateView):
	template_name = "content_item.html"

	def get_context_data(self, slug, **kwargs):
		context = super(ContentView, self).get_context_data(**kwargs)
		context['content'] = get_object_or_404(ContentItem, slug=slug)
		return context

class ContentListView(ListView):
	model = ContentItem
	queryset = ContentItem.objects.filter(is_blog=True)
	template_name = "content_list.html"
	context_object_name = "content_list"
	paginate_by = 10
