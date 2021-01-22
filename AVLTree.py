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
		self.height = 1

class AVLTree(object):
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
		root = self.updateHeight(root)
		root = self.checkDiference(root,word)
		return root

	def updateHeight(self,root):
		heightL = 0
		heightR = 0
		if root.L != None:
			heightL = root.L.height
		if root.R != None:
			heightR = root.R.height
		root.height = 1 + max(heightL,heightR)
		return root

	def diference(self,rootL,rootR):
		heightL = 0
		heightR = 0
		if rootL != None:
			heightL = rootL.height
		if rootR != None:
			heightR = rootR.height
		return heightL - heightR

	def checkDiference(self,root,insertedWord):
		if self.diference(root.L,root.R) > 1: 
			if insertedWord < root.L.word:
				root = self.rightRotation(root) 
			elif root.L.word < insertedWord :
				root = self.leftRightRotation(root)
		elif self.diference(root.L,root.R) < -1: 
			if insertedWord < root.R.word:
				root = self.rightLeftRotation(root)
			elif root.R.word < insertedWord:
				root = self.leftRotation(root) 
		return root 

	def leftRotation(self,root):
		global rotCounter
		rotCounter+=1
		child = root.R
		root.R = child.L
		child.L = root
		root = self.updateHeight(root)
		return self.updateHeight(child)

	def rightRotation(self,root):
		global rotCounter
		rotCounter+=1
		child=root.L
		root.L = child.R
		child.R = root
		root = self.updateHeight(root)
		return self.updateHeight(child)

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
		print("{}{}\t{}".format(root.word,spaces,root.line)) 
