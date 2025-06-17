from django.urls import path
from . import views

# 네임 스페이스
# 사용할 때는 board:question_list 와 같이 사용합니다.

app_name = 'board'  # board 앱의 이름을 지정합니다. (선택 사항)
urlpatterns = [
    path('', views.index, name = 'question_list'),  # board 앱의 index 뷰를 기본 URL로 설정
    path('<int:question_id>/', views.detail, name='question_detail'),  # 질문 상세 페이지
    path('ask/create/<int:question_id>/',
         views.create_answer, name='create_answer'),  # 답변 생성 URL
    path('question/create/', views.create_question, name='create_question'),  # 질문 생성 URL
    path('test/', views.test, name='test'),  # 테스트용 URL
]