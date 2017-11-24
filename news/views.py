from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Article
# Create your views here.

def index(request):
    latest_Article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_Article_list': latest_Article_list,
    }
    return render(request,'news/index.html',context)

def detail(request,Article_id):
    article = get_object_or_404(Article,pk= Article_id)
    context = {'Article':article}
    return render(request,'news/detail.html',context)

def news(request):
    return render(request,'news/news.html')

def newspage(request,Page_num):
    one_page_data = 5   #每一页的文章数
    now_page = int(Page_num)    #当前页面
    all_nums = Article.objects.count()  #所有文章数
    last_nums = all_nums % one_page_data  # 最后一页的文章数量
    all_pages = int(all_nums / one_page_data)
    if last_nums != 0:
        all_pages += 1    #页面数
    #pageup = True
    #pagedown = True     #是否可以进行上一页/下一页操作
    if now_page == all_pages:
        #pagedown = False    #如果是第一页，则不能进行上一页操作；同理最后一页
        start_num = (all_pages - 1) * one_page_data
        end_num = all_nums
    elif now_page == 1:
        start_num = 0
        end_num = one_page_data
    else :
        start_num = (now_page - 1) * one_page_data
        end_num = start_num + one_page_data
    Article_list = Article.objects.order_by('-pub_date')[start_num:end_num]
    context = {
        'article_list':Article_list,
        'pageup':now_page-1,
        'pagedown':now_page+1,
        'all_page':all_pages,
        'now_page':now_page,
    }
    return render(request,'news/newspage.html',context)