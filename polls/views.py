from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , login
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from polls.models import Team
global slovar

@csrf_exempt
def main(request):
    if request.user.is_authenticated:
        return redirect('/menu/')
    else:
        return (render(request,'index.html'))
@csrf_exempt
def enter(request):
    if request.user.is_authenticated:
        return redirect('/menu/')
    else:
        return (render(request, 'login.html'))
@csrf_exempt
def auth(request):
    pasw = request.POST.get('pass')
    usr = request.POST.get('name')
    if pasw and usr:
        user = authenticate(username=usr, password=pasw)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/menu/')
            else:
                return redirect('/accounts/logout/')
        else:
            return redirect('/accounts/logout/')
def register(request):
    if request.user.is_authenticated:
        return redirect('/menu/')
    else:
        return (render(request, 'registration.html'))
@csrf_exempt
def check(request):
    password = request.POST.get('password')
    password2 = request.POST.get('pswd')
    username = request.POST.get('username')
    telegram = request.POST.get('telegram')
    users = User.objects.all()
    print(password,password2,username,telegram)
    s = True
    if users:
        for usr in users:
            if usr.username == username:
                s = False
    if password and password2 and password == password2 and username and telegram and len(username) >= 4 and len(password) >= 6 and s:
        user = User.objects.create_user(username, telegram, password)
        user.save()
        return redirect('/accounts/logout/')
    else:
        return redirect('/register-page/')
@csrf_exempt
def menu(request):
    if request.user.is_authenticated:
        add = request.POST.get('addTeam')
        nav = request.POST.get('nav')
        if add:
            return redirect('/addteam/')
        if nav:
            global spisok
            nav = nav.replace(' ','')
            a = nav.split('#')
            spisok = []
            for q in a:
                if q in spisok:
                    pass
                else:
                    spisok.append(q)
            return redirect('/algoritm-page/')
        exit = request.POST.get('exit')
        if exit:
            logout(request)
            return redirect('/accounts/logout/')
        return (render(request,'Main.html', context = {'username' : request.user.username,'telegram':request.user.email}))
    else:
        return redirect('/accounts/logout/')
def algoritm(request):
    global slovar
    slovar = {}
    if request.user.is_authenticated:
        data = Team.objects.all()
        for item in data:
            kek = item.tech
            spisok2 = []
            e = kek.split('#')
            for w in e:
                if w in spisok2:
                    pass
                else:
                    spisok2.append(w)
            print(spisok2)
            for a in spisok:
                for b in spisok2:
                    if a == b:
                         if item in slovar:
                             slovar[item] += 1
                         else:
                             slovar[item] = 1
        return redirect('/search-page/')
    else:
        return redirect('/accounts/logout/')

def search(request):
    global slovar
    if request.user.is_authenticated:
        back = request.POST.get('back')
        if back:
            return redirect('/menu/')
        l = sorted(slovar.items(), key=lambda x: x[1], reverse=True)
        qwerty = []
        for g in l:
            qwerty.append(g[0])
        print(qwerty)
        teams = Team.objects.all()
        return (render(request,'search.html', context = {'teams':qwerty}))
    else:
        return redirect('/accounts/logout/')

def team(request):
    if request.user.is_authenticated:
        telegram = request.POST.get('telegram')
        count = request.POST.get('count')
        tech = request.POST.get('tech')
        teamname = request.POST.get('teamname')
        idea = request.POST.get('idea')
        print(count,tech,teamname,idea)
        if count and int(count) <= 100 and telegram and tech and len(tech) <= 40 and teamname and len(teamname) <= 20 and len(teamname) >= 4 and idea and len(idea) <= 40:
            tech = tech.replace(' ', '')
            team = Team(count=count,tech=tech,teamname=teamname,idea=idea, telegram = telegram)
            team.save()
            return redirect('/menu/')
        return(render(request,'addteam.html'))
    else:
        return redirect('/accounts/logout/')