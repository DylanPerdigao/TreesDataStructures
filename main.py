#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
import re
import sys
import os
from LinkedList import *
from AVLTree import *
from RBTree import *
from SplayTree import *

def readText(src):
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


if __name__=='__main__':
	############################
	########CONFIGURATION#######
	############################
	PATH = "resources/"
	#############################
	filesNames = list()
	with os.scandir(PATH) as files:
		for f in files:
			filesNames.append(f.name)
		filesNames.sort()
	for text in filesNames:
		totalText,totalWords = readText(PATH+text)
		print("===========TEXT {}===========".format(text[-5]))
		print("Total Words/Distinct Words:\t{}/{}\n".format(totalText,totalWords))
	


