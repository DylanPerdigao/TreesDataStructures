#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
import sys
import os
import re
import time
import random

class Node(object):
	def __init__(self, word, line):
		self.word = word
		self.line = [line]
		self.right = None

class LinkedList(object):
	def insert(self, root, word, line):
		if root == None:
			return Node(word,line)
		elif root.word < word:
			root.right = self.insert(root.right,word,line)
		elif root.word > word:
			aux = root
			root = Node(word,line)
			root.right = aux
		else:
			if line not in root.line:
				root.line.append(line)
		return root

	def search(self,root,word):
		if root == None:
			return None
		elif root.word < word:
			return self.search(root.right,word)
		elif root.word > word:
			return None
		else:
			return root
            
def readText(src,LL,root):
	with open(src,'r',encoding="utf-8") as f:
		i=0
		for line in f:
			newLine = re.sub('[(),;.""'']','',line)
			for word in newLine.upper().split():
				root=LL.insert(root,word,i)
			i+=1
	return LL,root

def showLines(instructions,LL,root):
	if len(instructions)==2:
		r = LL.search(root,instructions[1])
		if r == None:
			sys.stdout.write("-1\n")
		else:
			i=0
			for l in r.line:
				if instructions[0] != None:
					i+=1
					if i < len(r.line):
						sys.stdout.write(str(l)+" ")
					else:
						sys.stdout.write(str(l)+"\n")

def showAssoc(instructions,LL,root):
	if root != None and len(instructions)==3 and instructions[2].isnumeric():
		target = instructions[1]
		lineNumber = int(instructions[2])
		r = LL.search(root,target)
		if r != None and lineNumber in r.line:
			if instructions[0] != None:
				sys.stdout.write("ENCONTRADA.\n")
		else:
			if instructions[0] != None:
				sys.stdout.write("NAO ENCONTRADA.\n")

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


def stats_LinkedList(PATH,textName,iterLINHAS,iterASSOC,iterations):
	print(" ▶︎ LinkedList:")
	null = None
	instructions = list()
	root = None
	LL = LinkedList()
	instructions.append(None)
	for i in range(iterations):
		root = None
		LL = LinkedList()
		times = list()
		t = time.process_time()
		LL,root = readText(PATH+textName,LL,root)
		times.append(time.process_time()-t)
	print("\tAVERAGE INSERT TIME: {}".format(sum(times)*1000/len(times)))
	for i in range(iterations):
		words,null = selectRandomWords(PATH+textName,iterLINHAS)
		times = list()
		t = time.process_time()
		for word in words:
			if len(instructions) == 1:
				instructions.append(word)
			else:
				instructions[1] = word
			showLines(instructions, LL, root)
		times.append(time.process_time()-t)	
	print("\tAVERAGE LINHAS TIME: {}".format(sum(times)*1000/len(times)))
	for i in range(iterations):
		words,line = selectRandomWords(PATH+textName,iterASSOC)
		times = list()
		t = time.process_time()
		for word in words:
			if len(instructions) == 2:
				instructions[1] = word
				instructions.append(str(line))
			else:
				instructions[1] = word
			showAssoc(instructions, LL, root)
		times.append(time.process_time()-t)
	print("\tAVERAGE ASSOC TIME: {}\n".format(sum(times)*1000/len(times)))

