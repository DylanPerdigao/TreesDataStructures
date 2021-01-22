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
 