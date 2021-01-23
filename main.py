#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
import re
import sys
import os
from LinkedList import *
from AVLTree import *
from RBTree import *
from SplayTree import *


def readText(src,tree,root):
	if tree:
		with open(src,'r',encoding="utf-8") as f:
			i=0
			for line in f:
				newLine = re.sub('[(),;.""'']','',line)
				for word in newLine.upper().split():
					root=tree.insert(root,word,i)
				i+=1
		return tree,root
	else:
		text = list()
		words = list()
		with open(src,'r',encoding="utf-8") as f:
			lines = f.readlines()
		for line in lines:
			newLine = re.sub('[(),;.""'']','',line).upper().split()
			for w in newLine:
				text.append(w)
				if w not in words:
					words.append(w)
		return len(text), len(words)

def showLines(instructions,tree,root):
	if len(instructions)==2:
		root = tree.search(root,instructions[1])
		if root == None or root.word != instructions[1]:
			sys.stdout.write("-1\n")
		else:
			i=0
			for l in root.line:
				if instructions[0] != None:
					i+=1
					if i < len(root.line):
						sys.stdout.write(str(l)+" ")
					else:
						sys.stdout.write(str(l)+"\n")
	return root

def showAssoc(instructions,tree,root):
	if root != None and len(instructions)==3 and instructions[2].isnumeric():
		target = instructions[1]
		lineNumber = int(instructions[2])
		root = tree.search(root,target)
		if root != None and lineNumber in root.line:
			if instructions[0] != None:
				sys.stdout.write("ENCONTRADA.\n")
		else:
			if instructions[0] != None:
				sys.stdout.write("NAO ENCONTRADA.\n")
	return root

def selectRandomWords(src,n):
	words = list()
	line = list()
	with open(src,'r',encoding="utf-8") as f:
		lines = f.readlines()
	for i in range(n):
		k = str()
		while k == '\n' or k == '':
			k = random.choice(lines)
		line = re.sub('[(),;.""'']','',k).upper().split()
		word = random.choice(line)
		words.append(word)
	return words,random.randint(0,len(lines))


if __name__=='__main__':
	############################
	########CONFIGURATION#######
	############################
	sys.setrecursionlimit(100000)
	PATH = "tests/"
	iterLINHAS = 1
	iterASSOC = 1
	iterations = 1
	#############################
	global rotCounter
	filesNames = list()
	with os.scandir(PATH) as files:
		for f in files:
			filesNames.append(f.name)
		filesNames.sort()
	for text in filesNames:
		totalText,totalWords = readText(PATH+text,None,None)
		print("===========TEXT {}===========".format(text[-5]))
		print("Total Words/Distinct Words:\t{}/{}\n".format(totalText,totalWords))
		#Test Each Tree
		stats_LinkedList(PATH,text,iterLINHAS,iterASSOC,iterations)
		stats_AVLTree(PATH,text,iterLINHAS,iterASSOC,iterations)
		stats_RBTree(PATH,text,iterLINHAS,iterASSOC,iterations)
		stats_SplayTree(PATH,text,iterLINHAS,iterASSOC,iterations)
	


