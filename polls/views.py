from django.shortcuts import render
from django.template import loader
from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello,world.You're at the polls index.")
    latest_question_list = Question.objects.order_by('id')[:5]
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting at question %s." % question_id)
