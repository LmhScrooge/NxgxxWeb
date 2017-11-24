from django.shortcuts import render
from news.models import Article
# Create your views here.
def homepage(request):
    latest_Article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'article_list':latest_Article_list
    }
    return render(request,'homepage/homeindex.html',context)