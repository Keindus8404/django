from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer  # Assuming you have a model named Question in models.py
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page_number = request.GET.get('page', 1)  # ← 기본값 1 지정 중요
    questions = Question.objects.order_by('-created_at')
    paginator = Paginator(questions, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'board/index.html', {
        'page_obj': page_obj,
        'questions': page_obj.object_list
    })

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)  # 특정 질문을 가져옵니다.
    question = get_object_or_404(Question, id=question_id)  # 질문이 없으면 404 에러를 반환합니다.
    return render(request, 'board/detail.html', {'question': question})

def create_answer(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    Answer(question=question, content = request.POST['content']).save()  # 답변을 저장합니다.
    return redirect('board:question_detail', question_id=question.id)  # 질문 상세 페이지로 리다이렉트

def create_question(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        Question(subject=subject, content=content).save()        
        return redirect('board:question_list')
    return render(request, 'board/create_question.html')

# 임시로 Question 객체를 100개 생성하는 뷰
def test(request):
    for i in range(100):
        Question(subject=f'질문 {i+1}', content=f'질문 내용 {i+1}').save()
    return HttpResponse('100개의 질문이 생성되었습니다.')