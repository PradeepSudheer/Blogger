from django.shortcuts import render


# Create your views here.
def matches(request):
    return render(request, 'Matches/matchpage.html')
