from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Activity, Brand, Article, Tag

# Create your views here.
class HomeView(View):
    template_name = "frontend/home.html"

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class NewsIndexView(View):
    template_name = "frontend/news/index.html"

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['q'] = q = request.GET.get('q', '')
        brand_id = request.GET.getlist('brand_id', '')
        intent = request.GET.getlist('intent_name', '')
        ctx['brands'] = Brand.objects.all()
        ctx['intents'] = Activity.objects.exclude(intent='None').all().values('intent').distinct()

        activities = Activity.objects.all()

        brand_id = [_ for _ in brand_id if _ != 'all']
        if brand_id and len(brand_id) > 0:
            activities = activities.filter(brand__id__in=brand_id)

        intent = [_ for _ in intent if _ != 'all']
        if intent and len(intent) > 0:
            activities = activities.filter(intent__in=intent)

        if q:
            activities = activities.filter(brand__name__contains=q)

        activities = activities.order_by('create_time')
        paginator = Paginator(activities, 15)
        page = request.GET.get('page', 0)
        if page == 0:
            page = 1
        ctx['current_page'] = int(page)
        activities = paginator.get_page(page)
        ctx['activities'] = activities
        ctx['paginator'] = paginator
        ctx['page_name'] = 'news-index'
        ctx['brand_id'] = [int(_) for _ in brand_id]
        ctx['intent_names'] = intent

        return render(request, self.template_name, ctx)

class NewsShowView(View):
    template_name = "frontend/news/show.html"

    def get(self, request, id):
        ctx = {}
        activity = Activity.objects.filter(id=id).first()
        ctx["activity"] = activity
        ctx["brand"] = activity.brand
        ctx["articles"] = activity.articles()[:5]

        brand = activity.brand
        ctx["brand"] = {}
        ctx["brand"]["name"] = brand.name
        ctx["brand"]["figure"] = [brand.total_popularity_score,brand.total_figure_score,brand.total_market_score,brand.total_innovation_score,brand.total_capital_score]
        return render(request, self.template_name, ctx)

class ArticlesShowView(View):
    template_name = "frontend/articles/show.html"

    def get(self, request, id):
        ctx = {}
        articles = Article.objects.exclude(id=id).all()[:5]
        ctx["articles"] = articles
        article = Article.objects.filter(id=id).first()
        ctx["article"] = article
        brand = Brand.objects.first()
        ctx["brand"] = {}
        ctx["brand"]["obj"] = brand
        ctx["brand"]["name"] = brand.name
        ctx["brand"]["figure"] = [brand.total_popularity_score,brand.total_figure_score,brand.total_market_score,brand.total_innovation_score,brand.total_capital_score]
        return render(request, self.template_name, ctx)

class BrandShowView(View):
    template_name = "frontend/brand/show.html"

    def get(self, request, id):
        ctx = {}
        brand = Brand.objects.filter(id=id).first()
        ctx["brand_obj"] = brand

        articles = Article.objects.all()[:5]
        ctx["articles"] = articles
        ctx["brand"] = {}
        ctx["brand"]["name"] = brand.name
        ctx["brand"]["figure"] = [brand.total_popularity_score,brand.total_figure_score,brand.total_market_score,brand.total_innovation_score,brand.total_capital_score]
        activities = Activity.objects.exclude(intent='None').all().order_by('create_time')

        paginator = Paginator(activities, 15)
        page = request.GET.get('page', 0)
        if page == 0:
            page = 1
        ctx['current_page'] = int(page)
        activities = paginator.get_page(page)
        ctx['activities'] = activities
        ctx['paginator'] = paginator
        ctx['page_name'] = 'brand-show'
        return render(request, self.template_name, ctx)


def articles_list(request):
    data = {
        'data': [],
    }
    return JsonResponse(data)
