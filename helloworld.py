#!/usr/bin/env python3
#Filename:hellworld.py

'''
	print "helloworld"  in screen

'''

def hello(name):
	print("hello world {0}".format(name))


if __name__=="__main__":
	name = input('please input your name:')
	hello(name)
