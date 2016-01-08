#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Lista pessoas mais ligadas a você no Facebook
#
# ins3ct, Jun 2015
# Ago 2015 - Corrigido algumas modificações feitas pelo facebook
#
 
import urllib2, os, random, time
 
qtd   = 1000
limit = 50
lists = '"list":['
 
def procurar():
       
        f = open("profile.htm", "r")
        text = f.readline()
       
        while 1:
                if text.find(lists) != -1:
                        return text
                else:
                        text = f.readline()
 
        return False
 
def filtrar(num):
        i = 0
        lista = []
        text = procurar()
        if text:       
                if len(text) <= 1:
                        print "Nada encontrado..."
                else:
                        profiles = text.split('"list":[')[1].split("]")[0].replace("-", "\n").replace(",", "\n").replace('"', "\n").split()
                        for x in profiles:
                                if i < num:
                                        if len(x) < 5:
                                                continue
                                        else:
                                                lista.append(x)
                                        i += 1
                                else:
                                        break
                        return lista
        else:
                print "O programa falhou."
                exit()
 
def profile():
        num = 1
        owned = []
        lista = filtrar(qtd)
        for x in lista:
                if num <= limit:
                        url  = "http://m.facebook.com/profile.php?id=" + x
                        page = urllib2.urlopen(url)
                        data = page.read()
                        nome = data.split("<title>")[1].split("</title>")[0]
                        if nome.find("Facebook") != -1:
                                continue
                        elif nome.find("de segurança") != -1:
                                print "%.2d - http://www." % num + url.split("m.")[1]
                                num += 1
                                continue
                        else:
                                if nome not in owned:
                                        print "%.2d" % num, "-", nome#, "\nPerfil: ", "http://www." + url.split("m.")[1], "\n"
                                        owned.append(nome)
                                        num += 1
                else:
                        break
        print "\nFIM DA LISTA.\n"
 
def wait(min):
        for x in range(min * 10):
                os.system("clear")
                load = "Carregando"
                print load, random.choice(["\\", "-", "/"]), "\n", str(random.randrange(1000)) + "%", "[" + "#" * x + "]"
                #print load[random.randrange(len(load)):] + load[:random.randrange(len(load))]
                time.sleep(0.05)
 
 
wait(2)
time.sleep(2)
os.system("reset")
print "Amigos que mais visitaram seu perfil:\n"
profile()
