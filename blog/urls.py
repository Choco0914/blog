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
]
