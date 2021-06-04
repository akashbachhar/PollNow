from django.shortcuts import render, get_object_or_404, redirect

from .models import QuestionModel
from .forms import QuestionForm


def index(request):
    context = QuestionModel.objects.all()
    return render(request, 'polls/index.html', {'context': context})


def vote(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)

    if request.method == 'POST':
        try:
            selected = request.POST['choice']
        except (KeyError, QuestionModel.DoesNotExist):
            return render(request, 'polls/vote.html', {'question': question})
        else:
            if selected == 'choice1':
                question.choice_vote1 += 1
            elif selected == 'choice2':
                question.choice_vote2 += 1
            elif selected == 'choice3':
                question.choice_vote3 += 1

            question.save()
            return redirect('results', question_id)
    else:
        return render(request, 'polls/vote.html', {'question': question})


def create(request):
    if request.method == 'POST':
        context = QuestionModel.objects.all()

        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'polls/index.html', {'context': context})
    else:
        form = QuestionForm()
        return render(request, 'polls/create.html', {'form': form})


def results(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    total_vote = question.choice_vote1 + question.choice_vote2 + question.choice_vote3

    if total_vote != 0:
        percentage_vote1 = (question.choice_vote1 * 100) / total_vote
        percentage_vote2 = (question.choice_vote2 * 100) / total_vote
        percentage_vote3 = (question.choice_vote3 * 100) / total_vote

    else:
        percentage_vote1 = 0
        percentage_vote2 = 0
        percentage_vote3 = 0

    return render(request, 'polls/results.html', {'question': question,
                                                  'total_vote': total_vote,
                                                  'percentage_vote1': percentage_vote1,
                                                  'percentage_vote2': percentage_vote2,
                                                  'percentage_vote3': percentage_vote3,
                                                  })
