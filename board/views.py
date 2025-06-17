from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question  # Assuming you have a model named Question in models.py


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-created_at')  # 모든 질문을 가져옵니다.
    return render(request, 'board/index.html', {'questions': questions})

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)  # 특정 질문을 가져옵니다.
    question = get_object_or_404(Question, id=question_id)  # 질문이 없으면 404 에러를 반환합니다.
    return render(request, 'board/detail.html', {'question': question})