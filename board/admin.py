from django.contrib import admin

# Register your models here.
from .models import Question, Answer

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at', 'updated_at') # 리스트에 표시할 필드
    search_fields = ('subject', 'content') # 검색할 필드

admin.site.register(Question, QuestionAdmin) # Question 모델을 admin에 등록하고, QuestionAdmin 클래스를 사용하여 커스터마이징