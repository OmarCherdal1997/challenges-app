from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

challenges = {'january': 'Geeks', 'february': 'for', 'march': 'geeks','april': 'Omar','may': None}
# Create your views here.
def index (request):
    list_items = ""
    months= list(challenges.keys())
    #challenge_template= render_to_string("challenges/challenge.html")
    return render(request,"challenges/index.html",{
        "months" : months
    })
    """ for month in months:
        capitalized_month= month.capitalize()
        redirect_path = reverse( "monthly_challenges_path",args=[month])
        list_items+=f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>" """
        
    return HttpResponse(list_items)

def monthly_challenges_numbers (reauest,month):
    months= list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound ("Month number is not correct")
    redirected_month = months[month-1]
    redirect_path = reverse( "monthly_challenges_path",args=[redirected_month])
    return HttpResponseRedirect(redirect_path)

    

def monthly_challenges(request, month):
    try:
       returned_text = challenges[month]
       return render(request,"challenges/challenge.html",{
        "month": month,
        "text" : returned_text
       }) #HttpResponse(f"<h1>{challenges[month]}</h1>")
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")