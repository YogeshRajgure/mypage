from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "20 kms per day",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    responseData = f"""
    <ul>
    {list_items}
    </ul>
    """
    return HttpResponse(responseData)

def monthly_challenge_by_num(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_path = reverse("month-challenge", args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Not Valid Input")

def monthly_challenge(request, month):
    try:
        challengeText = monthly_challenges[month]
        response_data = f"<h1><center>{challengeText}</center></h1>"
    except:
        return HttpResponseNotFound("Invalid Response")
    
    return HttpResponse(response_data)