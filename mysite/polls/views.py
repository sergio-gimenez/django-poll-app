from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(
        request,
        "polls/index.html",
        context
    )
    # The context is a dictionary mapping template variable names to
    # Python objects.

    # The render() function takes the request object as its first argument, a
    # template name as its second argument and a dictionary as its optional
    # third argument. It returns an HttpResponse object of the given template
    # rendered with the given context.


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
