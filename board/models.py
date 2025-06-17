from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) # 질문 제목
    content = models.TextField() # 질문 내용
    created_at = models.DateTimeField(auto_now_add=True) # 질문 작성 시간
    updated_at = models.DateTimeField(auto_now=True) # 질문 수정 시간

    def __str__(self):
        return self.subject # 질문 제목을 문자열로 반환

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문과의 관계 설정
    content = models.TextField() # 답변 내용
    created_at = models.DateTimeField(auto_now_add=True) # 답변 작성 시간
    updated_at = models.DateTimeField(auto_now=True) # 답변 수정 시간

    def __str__(self):
        return f"Answer to {self.question.subject}" # 답변이 속한 질문 제목을 문자열로 반환