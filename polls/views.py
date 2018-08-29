
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
from polls.models import Team, UserDesc, Zayavki
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
    info = request.POST.get('info')
    users = User.objects.all()
    s = True
    if users:
        for usr in users:
            if usr.username == username:
                s = False
    if password and password2 and password == password2 and username and telegram and len(username) >= 4 and len(password) >= 6 and s and info  and len(info)>30:
        user = User.objects.create_user(username, telegram, password)
        user.save()
        info = UserDesc(user = telegram,desc=info)
        info.save()
        return redirect('/accounts/logout/')
    else:
        return redirect('/register-page/')
@csrf_exempt
def menu(request):
    global slovar
    if request.user.is_authenticated:
        srch = request.POST.get('srch')
        lk = request.POST.get('lk')
        add = request.POST.get('addTeam')
        nav = request.POST.get('nav')
        if srch:
            slovar = {}
            return redirect('/search-page/')
        if lk:
            return redirect('/personal/')
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
            spisok2.remove('')
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
def perspage(request):
    if request.user.is_authenticated:
        mm = request.POST.get('mainmenu')
        if mm:
            return redirect('/menu/')
        data = []
        dann = Team.objects.all()
        for item in dann:
            if item.person == request.user.username:
                data.append(item)
        for item in dann:
            if request.POST.get(item.teamname):
                item.delete()
        i = 0
        zapr = {}
        allzay = Zayavki.objects.all()
        for zay in allzay:
            if zay.team in zapr:
                zapr[zay.team].append(zay.zayavki.split('!@#$'))
            else:
                zapr[zay.team] = []
                zapr[zay.team].append(zay.zayavki.split('!@#$'))
        for zap in zapr:
            zapp = zap
            k = 0
            for i in zapr[zap]:
                zapr[zap][k] = str(i)
                zapr[zap][k] = zapr[zap][k][:-2]
                zapr[zap][k] = zapr[zap][k][2:]
                k += 1
        zez = []
        j = 0
        if zapr[zapp]:
            for ne in zapr[zapp]:
                zez.append(ne.split(':'))
                i = 0
                for zzz in zez[j]:
                    if i == 0:
                        zez[j][i] = 'Телеграм для связи: ' + zez[j][i]
                    if i == 1:
                        zez[j][i] = 'Обо мне: ' + zez[j][i]
                    i += 1
                j += 1
        if zez:
            return (render(request,'lk.html',context = {'list': data,'zayav':zez}))
        else:
            return (render(request, 'lk.html', context={'list': data, 'zayav': ['Пока заявок нет']}))
    else:
        return redirect('/accounts/logout/')
def search(request):
    global slovar, itemm
    if request.user.is_authenticated:
        back = request.POST.get('back')
        items = Team.objects.all()
        for item in items:
            if request.POST.get(item.teamname):
                itemm = item
                return redirect('/full/')
        if back:
            return redirect('/menu/')
        if slovar:
            l = sorted(slovar.items(), key=lambda x: x[1], reverse=True)
            qwerty = []
            for g in l:
                qwerty.append(g[0])
            numb = []
            #for qw in qwerty:
                #numb.append(slovar[qwerty.index(qw)])
            return (render(request,'search.html', context = {'teams':qwerty}))
        else:
            teams = Team.objects.all()
            return (render(request, 'search.html', context={'teams': teams}))
    else:
        return redirect('/accounts/logout/')
def full(request):
    global itemm
    if request.user.is_authenticated:
        nazad = request.POST.get('naz')
        allobj = Team.objects.all()
        allInfo = UserDesc.objects.all()
        allzayv = Zayavki.objects.all()
        boole = False
        if allzayv:
            for zayvv in allzayv:
                if '!@#$' in zayvv.zayavki:
                    per = zayvv.zayavki.split('!@#$')
                    for zzz in per:
                        if zzz.split(':')[0] == request.user.email:
                            boole = True
                else:
                    if zayvv.zayavki.split(':')[0] == request.user.email:
                        boole = True
        if boole:
            pass
        else:
            for obj in allobj:
                if request.POST.get(request.user.username + ',' + obj.teamname):
                    zayv = ''
                    if int(obj.count) > 0:
                        for info in allInfo:
                            if info.user == request.user.email:
                                zayv += info.user + ': ' + info.desc + '!@#$'
                        zayv = zayv[:-5]
                        zay = Zayavki(team=obj,zayavki=zayv)
                        zay.save()
        if nazad:
            return redirect('/search-page/')
        return (render(request,'full.html',context={'object':itemm , 'tag':request.user.username+','+itemm.teamname}))
    else:
        return redirect('/accounts/logout/')
def team(request):
    if request.user.is_authenticated:
        telegram = request.POST.get('telegram')
        count = request.POST.get('count')
        tech = request.POST.get('tech')
        teamname = request.POST.get('teamname')
        idea = request.POST.get('idea')
        if count and int(count) <= 100 and telegram and tech and len(tech) <= 40 and teamname and len(teamname) <= 20 and len(teamname) >= 4 and idea and len(idea) <= 40:
            tech = tech.replace(' ', '')
            team = Team(count=count,tech=tech,teamname=teamname,idea=idea, telegram = telegram,person=request.user.username)
            team.save()
            return redirect('/menu/')
        return(render(request,'addteam.html'))
    else:
        return redirect('/accounts/logout/')
def panel(request):
    if request.user.is_authenticated:
        if request.user.has_perm('Superuser status'):
            dlt = request.POST.get('deleteall')
            if dlt:
                lol = Team.objects.all()
                kekk = Zayavki.objects.all()
                for obj in lol:
                    obj.delete()
                for usr in User.objects.all():
                    usr.delete()
                for k in kekk:
                    k.delete()
            return (render(request,'panel.html'))
        else:
            return HttpResponse('Ты не админ, сори')
    else:
        return redirect('/accounts/logout/')
