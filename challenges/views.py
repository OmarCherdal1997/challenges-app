from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
""" monthly_challenges = {
    'january': 'This Challenge is From January',
    'february': 'This Challenge is From February',
    'march': 'This Challenge is From March',
    'april': 'This Challenge is From April',
    'may': 'This Challenge is From May',
    'june': 'This Challenge is From June',
    'july': 'This Challenge is From July'
} """
challenges = {'january': 'Geeks', 'february': 'for', 'march': 'geeks'}
# Create your views here.
def index (request):
    list_items = ""
    months= list(challenges.keys())
    for month in months:
        capitalized_month= month.capitalize()
        redirect_path = reverse( "monthly_challenges_path",args=[month])
        list_items+=f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>"
        
    return HttpResponse(f"<ul>{list_items}</ul>")

def monthly_challenges_numbers (reauest,month):
    months= list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound ("Month number is not correct")
    redirected_month = months[month-1]
    redirect_path = reverse( "monthly_challenges_path",args=[redirected_month])
    return HttpResponseRedirect(redirect_path)

    

def monthly_challenges(request, month):
    try:
       return HttpResponse(f"<h1>{challenges[month]}</h1>")
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")