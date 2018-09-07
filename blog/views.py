from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
"""
post_list라는 함수(def)를 만들어 요청(request) 을 인자로 넘겨받아 render 메서드를
호출한다. 이 함수는 호출하여 받은(return) blog/post_list 템플릿을 보여준다
"""
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
