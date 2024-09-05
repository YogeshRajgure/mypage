from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
monthly_challenges = {
    "january": "Strictly Vegan",
    "february": "20 kms per day",
    "march": "Strictly Vegan",
    "april": "20 kms per day",
    "may": "Strictly Vegan",
    "june": "20 kms per day",
    "july": "Strictly Vegan",
    "august": "20 kms per day",
    "september": "Strictly Vegan",
    "october": "20 kms per day",
    "november": "Strictly Vegan",
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months,
    }) # HttpResponse(responseData)


def monthly_challenge_by_num(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_path = reverse("month-challenge", args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()
        # return HttpResponseNotFound("Not Valid Input")


def monthly_challenge(request, month):
    try:
        challengeText = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challengeText,
            "month": month,
        })
    except:
        raise Http404()
        # return HttpResponseNotFound("<h1>Invalid Response</h1>")

    