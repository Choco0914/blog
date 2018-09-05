from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
"""
post_list라는 함수(def)를 만들어 요청(request) 을 인자로 넘겨받아 render 메서드를
호출한다. 이 함수는 호출하여 받은(return) blog/post_list 템플릿을 보여준다
"""
