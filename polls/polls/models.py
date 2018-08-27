from django.db import models
#class user(models.Model):
    #password = models.CharField(max_length=30,default='1234')
    #username = models.CharField(max_length=30,default='user')
    #telegram = models.CharField(max_length=30,default='user')
    #is_auth =  models.BooleanField()
    #def __str__ (self):
        #return 'Имя пользователя: ' + self.username + '  Telegram : ' + self.telegram
class Team(models.Model):
    count = models.CharField(max_length=10,default='2')
    tech = models.CharField(max_length=200,default='Technology')
    teamname = models.CharField(max_length=200, default='teamname')
    idea = models.CharField(max_length=500, default='idea')
    telegram = models.CharField(max_length=500, default='telega')
    person = models.CharField(max_length=100,default = 'user')
    def __str__ (self):
        return self.teamname + '/' + self.tech + '/' + self.teamname + '/' + self.idea + '/' + self.telegram + '/' + self.person
class Zayavki(models.Model):
    team = models.CharField(max_length=200, default='teamname')
    zayavki = models.CharField(max_length=10000,default='Пока заявок нет')
    def __str__ (self):
        return self.team + '/' + self.zayavki
class UserDesc(models.Model):
    user = models.CharField(max_length=200, default='user')
    desc = models.TextField(default = 'kek')
    def __str__ (self):
        return self.user + '/' + self.desc