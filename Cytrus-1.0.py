#!/usr/bin/python
#!python3
# -*- coding: utf-8 -*-
#
#  Cytrus-1.0.py
#  
#  Copyright 2017 gmattos <gmattos@protonmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  
#  

import sys, os, time, itertools


def clnw(modelos, palavra):
	
	for a in modelos:
		
		palavra = palavra.replace(a, "")
		
	lx = palavra
	
	if lx != "":
		return lx 
	else: return ""	

def fixw(rst, plvr,total):
	if total == plvr.rfind(rst):
		return plvr
	else:
		st = plvr.rfind(rst)
		fn = len(plvr) -1
		
		plvrl = list(plvr)
		rstl = list(rst)
		
		while fn >= st:
			
			del plvrl[fn]
			 
			fn = fn-1
		fix = ''.join(plvrl)
		
		return fix
	
mini = sys.argv[1]
maxi = sys.argv[2]
if int(maxi) > 24:
	print(">>For secure, the max of range of string was setup as 24<<")
	print("Old value: " + maxi)
	maxi = 24

maxi = int(maxi)
mini = int(mini)	

words = sys.argv[3:]
words.sort()
words.sort(key=len, reverse=True)
print(words)
wn = len(words)
i=0

while i != wn:
	words[i] = words[i].title()
	i=i+1

print("Inserted Words: " + str(len(words)))
print("Started at " + time.strftime("%H:%M:%S") + " - " + time.strftime("%d/%m/%Y"))
print('\n' + "Loading... The job can delay several hours if more than 12 words as input! But the results will worth it =D")

outp = "t_Cytrus_WL.txt"
f2 = open(outp, "w")

cw = 0
pcw = 0
nwords = []
thnklr1 = []
thnklr2 = []
thnklr4 = []
thnklr5 = []
thnklr6 = []
c = 100 #verificar isso <><><><> (era o ==)
b = 0
#tw = 0
for word in map(''.join, itertools.permutations(words, r=wn)):
	cw = cw+1
	print(str(cw*(maxi-mini)))
	sys.stdout.write("\033[F") #back to previous line
	sys.stdout.write("\033[K") #clear line
	thnklr1 = []
	thnklr4 = []
	z = mini
	b = b+1
	while z <= maxi:
		
		thnklr1.append(word[:z])
		z = z+1
	thnklr3 = set(thnklr1).symmetric_difference(thnklr2)
	#print(thnklr1)
	#print("\n")
	#print(thnklr2)
	#print("\n")
	#print(thnklr3)
	#print("\n")
	#print(thnklr4)
	#print("\n")
	#print(thnklr5)
	#print("\n")
	#print(thnklr6)
	#print("\n")
	
	for word2 in thnklr3:
		
		#print(word2)					
		
		
		
		tmp = clnw(words, word2)
		word2 = fixw(tmp,word2,z)
		#abc="WanGuiVan"
		#if word2 == abc:
			#print("bazinga"+"\n")
		
		thnklr4.append(word2)
		
	thnklr6 = set(thnklr4).symmetric_difference(thnklr5)
		
	for word2 in thnklr6:
		
		
		
		if len(word2) >= mini:
		
			#z = z+1
			wn = wn-1
			w = word2
			w = w.strip()
			#if not(w in nwords):
				#print(w)
			n_w = w #title change
			nwords.append(n_w+"\n")
			n_w = w.lower() #lower change
			nwords.append(n_w+"\n")
			n_w = w.upper() #upper change
			nwords.append(n_w+"\n")
			pcw = pcw+1
			#b = pcw
			#print(pcw)
	#thnklr4.sort
	thnklr5 = list(thnklr4)
	
	thnklr2 = list(thnklr1)		
	#thnklr1 = [] não dá certo
	
	#print(nwords)
	#print(pcw)
	#print(c)
	#print(pcw)
	
	#==> O erro está abaixo
	
	if pcw < c:
	
		#nwords = sorted((set(nwords)))
	
		for item2 in nwords:
			f2.write(item2)
		nwords = []
	
	elif pcw >= c :
		#print("fuscao")
		#nwords = sorted((set(nwords)))
		c = pcw+c
		f2 = open(outp, 'a')
		for item in nwords:
			f2.write(item)
		nwords = []
		f2.close


	

f2.close()

nwords = []
	
print("\nSorting... Please Wait. ")
print("Started sorted at " + time.strftime("%H:%M:%S") + " - " + time.strftime("%d/%m/%Y"))
f2 = open(outp, "r")

fwords = []

for line in f2:
	fwords.append(line)
open(outp, 'w').close()
fwords = sorted((set(fwords)))
fwords.sort(key=len, reverse=True)


f2 = open(outp, 'a')

for fitem in fwords:
	f2.write(fitem)
	#tw = tw+1

f2.close()

print(pcw)
print('\n' + "Finished at " + time.strftime("%H:%M:%S") + " - " + time.strftime("%d/%m/%Y"))
print()
print("\n Combinations Proccessed: " + str(cw*(maxi-mini)))

print("\n Total Results after processing: " + str(pcw*3))
