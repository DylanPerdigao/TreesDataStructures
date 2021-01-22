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
		self.L = None
		self.R = None
		self.parent = None
		self.isRED = True

class RBTree(object):
	def insertWithBlackRoot(self,root, word, line):
		root = self.insert(root,word,line)
		root.isRED = False
		return root

	def insert(self, root, word, line):
		if root == None:
			return Node(word,line)
		elif word < root.word:
			root.L = self.insert(root.L,word,line)
			root.L.parent = root
		elif root.word < word:
			root.R = self.insert(root.R,word,line)
			root.R.parent = root
		else:
			if line not in root.line:
				root.line.append(line)
		root = self.checkColors(root,word)
		return root

	def checkColors(self,root,insertedWord):
		#PAI VERMELHO A ESQUERDA E TIO PRETO A DIREITA (OU INEXISTENTE)
		if root.L != None and root.L.isRED and (root.R == None or root.R.isRED == False):
			#CASO ESQUERDO-ESQUERDO
			if insertedWord < root.L.word:
				if root.L.L != None and root.L.L.isRED:
					root = self.rightRotation(root)
			#CASO ESQUERDO-DIREITO
			elif root.L.word < insertedWord:
				if root.L.R != None and root.L.R.isRED:
					root = self.leftRightRotation(root)
		#PAI VERMELHO A DIREITA E TIO PRETO A ESQUERDA (OU INEXISTENTE)
		elif root.R != None and root.R.isRED and (root.L == None or root.L.isRED == False):
			#CASO DIREITO-ESQUERDO
			if insertedWord < root.R.word:
				if root.R.L != None and root.R.L.isRED:
					root = self.rightLeftRotation(root)
			#CASO DIREITO-DIREITO
			elif root.R.word < insertedWord:
				if root.R.R != None and root.R.R.isRED:
					root = self.leftRotation(root)
		#CASO PAI E TIO VERMELHOS E AVO PRETO
		elif root.R != None and root.L != None and root.L.isRED != None:
			if root.isRED == False and root.L.isRED and root.R.isRED:
				root.isRED = True
				root.R.isRED = False
				root.L.isRED = False
		return root

	def leftRotation(self,root):
		global rotCounter
		rotCounter+=1
		child = root.R
		root.R = child.L
		child.L = root
		child.isRED = root.isRED
		root.isRED = True
		return child

	def rightRotation(self,root):
		global rotCounter
		rotCounter+=1
		child=root.L
		root.L = child.R
		child.R = root
		child.isRED = root.isRED
		root.isRED = True
		return child


	def leftRightRotation(self,root):
		root.L = self.leftRotation(root.L) 
		return self.rightRotation(root) 
	
	def rightLeftRotation(self,root):
		root.R = self.rightRotation(root.R) 
		return self.leftRotation(root) 

	def search(self,root,word):
		if root == None:
			return None
		elif root.word < word:
			return self.search(root.R,word)
		elif root.word > word:
			return self.search(root.L,word)
		else:
			return root
    
	def printPreOrder(self, root):
		if root == None: 
			return None
		else:
			self.printText(root)
			self.printPreOrder(root.L) 
			self.printPreOrder(root.R) 

	def printPostOrder(self, root):
		if root == None: 
			return None
		else:
			self.printPostOrder(root.L) 
			self.printPostOrder(root.R) 
			self.printText(root)
    
	def printInOrder(self, root):
		if root == None: 
			return None
		else:
			self.printInOrder(root.L) 
			self.printText(root)
			self.printInOrder(root.R) 
	
	def printText(self,root):
		spaces=""
		for _ in range(len(root.word),20):
			spaces+=" "
		if root.isRED:
			print("{}{}🟥\t{}".format(root.word,spaces,root.line)) 
		else:
			print("{}{}⬛️\t{}".format(root.word,spaces,root.line)) 

def getInstructions():
    instructions = input().upper().split()
    instruction = ""
    if len(instructions)>0:
        instruction = instructions[0]
    return instructions,instruction

def getText(tree,root):
	line = input()
	i=0
	while(line.upper() != 'FIM.'):
		newLine = re.sub('[(),;.""'']','',line)
		for word in newLine.upper().split():
			root=tree.insertWithBlackRoot(root,word,i)
		i+=1
		line = input()
	sys.stdout.write("GUARDADO.\n") 
	return tree, root

def getExampleText(tree,root):
	texto = list()
	texto.append("Dizem-nos os arautos que ser comediante é uma profissão de alto risco,")
	texto.append("pois o sucesso que suscita ser o humorista eleito da corte pode ser tão")
	texto.append("intenso e inebriante quanto o seu desgaste vertiginosamente rápido. Não")
	texto.append("será certamente este o caso de Ricardo Araújo Pereira.")
	texto.append("RAP é um corredor de fundo. Começou em 1997 a colaborar com as Produções")
	texto.append("Fictícias — à época a maior fábrica de escrita e produção de humor —,")
	texto.append("onde entrou logo pela porta grande, a escrever sketches para Herman José,")
	texto.append("outro grande comediante e um dos seus maiores ídolos. Tinha então 23 anos.")
	texto.append("Seis anos depois, na SIC Radical, deu a cara como protagonista do “Gato")
	texto.append("Fedorento” e tornou-se rapidamente na incontornável referência do humor")
	texto.append("contemporâneo nacional.")
	i=0
	for line in texto:
		newLine = re.sub('[(),;.“”]','',line)
		for word in newLine.upper().split():
			root=tree.insertWithBlackRoot(root,word,i)
		i+=1
	sys.stdout.write("GUARDADO.\n") 
	return tree,root

def readText(src,tree,root):
	with open(src,'r',encoding="utf-8") as f:
		i=0
		for line in f:
			newLine = re.sub('[(),;.""'']','',line)
			for word in newLine.upper().split():
				root=tree.insertWithBlackRoot(root,word,i)
			i+=1
	return tree,root

def showLines(instructions,tree,root):
	if len(instructions)==2:
		r = tree.search(root,instructions[1])
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

def showAssoc(instructions,tree,root):
	if root != None and len(instructions)==3 and instructions[2].isnumeric():
		target = instructions[1]
		lineNumber = int(instructions[2])
		r = tree.search(root,target)
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


if __name__=='__main__':
	############################
	########CONFIGURATION#######
	############################
	sys.setrecursionlimit(100000)
	AUTO = True
	PATH = "resources/"
	iterLINHAS = 50
	iterASSOC = 50
	iterASSOC_D = 500
	iterations = 200
	#############################
	global rotCounter
	rotCounter=0
	null = None
	instruction = None
	instructions = list()
	root = None
	tree = RBTree()
	if AUTO:
		instructions.append(None)
		filesNames = list()
		with os.scandir(PATH) as files:
			for f in files:
				filesNames.append(f.name)
		filesNames.sort()
		for textName in filesNames:
			print("🔻🔻🔻🔻🔻")
			print("TEXTO {}".format(textName[-5]))
			for i in range(iterations):
				root = None
				tree = RBTree()
				rotCounter = 0
				times = list()
				t = time.process_time()
				tree,root = readText(PATH+textName,tree,root)
				times.append(time.process_time()-t)
			print("\tAVERAGE INSERT TIME: {}\tROTATIONS: {}".format(sum(times)*1000/len(times),rotCounter))
			for i in range(iterations):
				words,null = selectRandomWords(PATH+textName,iterLINHAS)
				times = list()
				t = time.process_time()
				for word in words:
					if len(instructions) == 1:
						instructions.append(word)
					else:
						instructions[1] = word
					showLines(instructions, tree, root)
				times.append(time.process_time()-t)	
			print("\tAVERAGE LINHAS TIME: {}".format(sum(times)*1000/len(times)))
			for i in range(iterations):
				if textName[-5] != "D":
					words,line = selectRandomWords(PATH+textName,iterASSOC)
				else:
					words,line = selectRandomWords(PATH+textName,iterASSOC_D)
				times = list()
				t = time.process_time()
				for word in words:
					if len(instructions) == 2:
						instructions[1] = word
						instructions.append(str(line))
					else:
						instructions[1] = word
					showAssoc(instructions, tree, root)
				times.append(time.process_time()-t)
			print("\tAVERAGE ASSOC TIME: {}\n🔺🔺🔺🔺🔺".format(sum(times)*1000/len(times)))
	else:
		while instruction != "TCHAU":
			instructions,instruction = getInstructions()
			if instruction == "TEXTO":
				root = None
				tree = RBTree()
				tree,root = getText(tree,root)
			elif instruction== "LINHAS":
				showLines(instructions, tree, root)
			elif instruction == "ASSOC":
				showAssoc(instructions, tree, root)