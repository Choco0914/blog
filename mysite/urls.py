from django.contrib import admin
from django.urls import path, re_path, include

from django.contrib.auth import views as auth_views
# 정규식을 이욯가ㅣ 위해 re_path를 임포트하고 다른 url을 참조하기위해 include를
# 임포트 해 왔다
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),

    # User login page
    re_path(r'^accounts/login/$',
     auth_views.LoginView.as_view(template_name='registration/login.html'),
     name='login'),

    # User logout page
    re_path(r'^accounts/logout/$',
     auth_views.LogoutView.as_view(template_name=
     'registration/logged_out.html'),
     name='logout', kwargs={'next_page': '/'},)
]
"""
파이썬에서 정규 표현식을 작성할 때는 항상 문자열 앞에 r을 붙인다. 이는 파이썬에게는
별 의미가 없지만, 파이썬에게 문자열에 특수 문자를 있다는 것을 알려준다
"""
