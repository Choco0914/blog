from django.urls import re_path
from . import views
# urls.py가 있는 폴더안에 views를 사용하기위해 임포트해왔다
urlpatterns = [
    re_path(r'^$', views.post_list, name = 'post_list'),
# 위의 정규 표현식은 ^에서 시작해 $로 끝나는지 매칭한다, 즉 문자열이 아무것도 없는
# 경우만 매칭하겠다는 뜻이다
# 마지막 부분인 name = 'post_list' 는 URL에 이름을 붙인 것으로 뷰를 식별한다
# 뷰의 이름이 같을 수도 완전히 다를 수도 있다 이름을 붙인 URl은 프로젝트 후반에
# 다시 사용될거다 URL에 고유한 이름을 붙여, 외우고 부르기 쉽게 만들어야 한다
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
# ^post/(?p<pk>\d+)/$에서 ^은 "시작"을 뜻한다
# post/란 URL이 post 문자를 포함해야 한다는 것을 말한다
# (?p<pk>\d+)는 조금 까다롭다 이 정규표현식은 장고가 pk 변수에 모든 값을 넣어 뷰로
# 정송하겠다는 뜻이다 \d 는 문자를 제외한 숫자 0부터 9중, 한 가지 숫자만 올 수 있다는
# 것을 말한다 +는 하나 또는 그 이상의 숫자가 올 수 있다.
# 따라서 http://127.0.0.1:8000/post/ 라고 하면 post/다음에 숫자가 없으므로
# 해당 사항이 아니지만, http://127.0.0.1:8000/post/1234567890/ 은 완벽하게
# 매칭된다
# /은 다음에 /가 한 번 더 와야 한다는 의미이다
# $는 "마지막"을 뜻한다 그 뒤로는 더는 문자가 오면 안 된다.
#
# 브라우저에 http://127.0.0.1:8000/post/5라고 입력하면, 장고는 post_detail 뷰를
# 찾아 매개변수 pk가 5인 값을 찾아 뷰로 전달한다.

# pk는 primary key의 약자로, 장고에서 많이 사용되는 변수명이다 변수명은 내가 원하는
# 것으로 변경 할 수 있다. (변수명에 공백문자는 사용할 수 없으며 소문자와 _ 를
# 사용 할수 있음을 주의하자)예를 들어, (?p<pk>\d+) 변수를 post_id로 바꾸면,
# 정규표현식 도 (?p<post_id>\d+) 으로 바뀌게 된다
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]
