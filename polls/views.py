from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, "polls/detail.html", {"question" : question})

def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question" : question,
                "error_message" : "You didn't select a choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))

def results(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, "polls/results.html", {"question" : question})
