from django.shortcuts import render, HttpResponse
from app.models import Post

# Create your views here.


def home(request):
    texts= Post.objects.all()
    return render(request, "home.html",{'texts': texts})


def detail(request, slug):

    q = Post.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {

        'post': q
    }
    return render(request, 'details.html', context)