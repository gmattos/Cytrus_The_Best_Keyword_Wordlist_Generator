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

temp = "temp.txt"
f = open(temp, "w")

outp = "MR_R3T_PW_Gen.txt"
f2 = open(outp, "w")

cw = 0
cutd = 0
nwords = []
eql = ""
a = 10000
for word in map(''.join, itertools.permutations(words, r=wn)):
	cw = cw+1
	print(cw)
	sys.stdout.write("\033[F") #back to previous line
	sys.stdout.write("\033[K") #clear line
	if len(word) <= maxi:
		w2 = word
		w2 = w2.strip()
		n_w2 = w2 #title change
		f2.write(n_w2 + '\n')
		n_w2 = w2.lower() #lower change
		f2.write(n_w2 + '\n')
		n_w2 = w2.upper() #upper change
		f2.write(n_w2 + '\n')
					
	else:
				#Permutations, slicing of the big ones
		z = mini
		
		while z <= maxi:
		
			word2 = word[:z]
						
			tmp = clnw(words, word2)
			word2 = fixw(tmp,word2,z)
			
			f = open(temp, "a")	
			z = z+1
			
			wn = wn-1
			w = word2
			w = w.strip()
			n_w = w #title change
			f.write(n_w + '\n')
			n_w = w.lower() #lower change
			f.write(n_w + '\n')
			n_w = w.upper() #upper change
			f.write(n_w + '\n')
			
	if cw == a:
		tw = 0
		f.close()
		f = open(temp, "r")
		for vcb in f:
			if len(vcb)-1 >= mini:
				nwords.append(vcb)
		nwords = sorted((set(nwords)))
		nwords.sort(key=len, reverse=True)
		a = a+a
		open(temp, 'w').close()
		f2 = open(outp, 'a')
		for item in nwords:
			f2.write(item)
			tw = tw+1
		nwords = []
		open(temp, 'w').close()
	

if cw < a:
	tw = 0
	f = open(temp, "r")
	for vcb2 in f:
		if len(vcb2)-1 >= mini:
			nwords.append(vcb2)
	nwords = sorted((set(nwords)))
	nwords.sort(key=len, reverse=True)
	for item2 in nwords:
		f2.write(item2)
		tw = tw+1
	
f2.close()

os.remove("temp.txt")
print('\n' + "Finished at " + time.strftime("%H:%M:%S") + " - " + time.strftime("%d/%m/%Y"))
print()
print("\n Combinations Proccessed: " + str(cw*(maxi-mini)))

print("\n Total Results of Slicing and Verification Methods: " + str(tw))

print("\n With UPPERED lowered and Titled words: " + str(tw*3))
