from django.shortcuts import render

def battle(request):
    return render(request, 'battle/battle.html')
