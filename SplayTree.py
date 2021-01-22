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

class SplayTree(object):
	def insert(self, root, word, line):
		if root == None:
			return Node(word,line)
		elif word < root.word:
			root.L = self.insert(root.L,word,line)
		elif root.word < word:
			root.R = self.insert(root.R,word,line)
		else:
			if line not in root.line:
				root.line.append(line)
		root = self.splaying(root,word)
		return root

	def search(self,root,word):
		if root == None:
			return None
		elif word < root.word:
			root.L = self.search(root.L,word)
		elif root.word < word:
			root.R = self.search(root.R,word)
		root = self.splaying(root,word)
		return root

	def splaying(self,root,insertedWord):
		if root.L != None and insertedWord < root.word:
			root = self.rightRotation(root)
		elif root.R != None and root.word < insertedWord:
			root = self.leftRotation(root)
		return root


	def leftRotation(self,root):
		global rotCounter
		rotCounter+=1
		child = root.R
		root.R = child.L
		child.L = root
		return child

	def rightRotation(self,root):
		global rotCounter
		rotCounter+=1
		child=root.L
		root.L = child.R
		child.R = root
		return child
    
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
		print("{}{}\t{}".format(root.word,spaces,root.line)) 
