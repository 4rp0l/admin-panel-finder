#!/usr/bin/env python

banner = ''' SMART ADMIN PANEL FINDER
_______      ___________  ___________
|      \\    |          | |          |
|       \\   |          | |          |
|    |   \\  |    ______| |   _______|
|         | |          | |          |
|  _______| |          | |          |
|         | |          | |          |
|         | |______    | |   _______|
|    |   /  |          | |          |
|       /   |          | |          |
|______/    |__________| |__________|

'''
team    = '--==++||Bangladesh Security ExploiterZ||++==--'
group   = '          fb.com/groups/..............'
dev     = '--==++|| Coded By Tonmoy Ahmed Dhrubo ||++==--' 
contact = '    Contact :: fb.com/tonmoyahmed.dhrubo'

import requests
import multiprocessing as MP
import time
import argparse
import os
import sys
from string import strip

def screen_clear():
	try:
		os.system('clear')
	except:
		os.system('cls')

def Banner():
	print banner
	time.sleep(0.5)
	print team
	time.sleep(0.5)
	print group
	time.sleep(0.5)
	print dev
	time.sleep(0.5)
	print contact
	time.sleep(0.5)


class URLMaker:

	#This Class joins domain name and latter path extension easily .

	def __init__(self , domain = None, path = None):
		self.domain  = domain
		self.path    = path
		self.f_domain= list() #List of final domains (f_ means final)
		self.f_path  = list() #List of final paths
		self.URLs    = list() #List of final full URLs


	def RemHTTP(self, strng):           #Now removing protocol signs  

		strng = strip(strng)
		if strng.startswith('http'):
			try:
				strng = strng.replace('http://','')
			except:
				strng = strng.replace('https://','')
		return strng


	def RemSlash(self, strng):          #Function to remove front slash from starting and ending
		strng = strip(strng)
		if strng.startswith('/'):
			strng = strng.replace('/','')
		if strng.endswith('/'):
			strng = strng.replace('/','')
		return strng


	def GetDomain(self):

		if os.path.isfile(self.domain):  # If it is a file containing domains 
			with open(self.domain) as f:
				for each in f:
					if each != '\n':     # Checks whether any line has only blank newline character
						each = self.RemHTTP(each)
						each = self.RemSlash(each)
						self.f_domain.append(each)

		elif type(self.domain)== list:   # Or just a list of domains
			for each in self.domain:
				each = self.RemHTTP(each)
				each = self.RemSlash(each)
				self.f_domain.append(each)

		elif type(self.domain)== str:    # Or just a single domain
			self.domain = self.RemHTTP(self.domain)
			self.domain = self.RemSlash(self.domain)
			self.f_domain.append(self.domain)


	def GetPath(self):                   # If it is a file containing paths

		if os.path.isfile(self.path):
			with open(self.path) as f:
				for each in f:
					if each != '\n':     # Checks whether any line has only blank newline character
						each = self.RemSlash(each)
						self.f_path.append(each)

		elif type(self.path) == list:
			for each in self.path:
				each = self.RemSlash(each)
				self.f_path.append(each)

		elif type(self.path) == str:
			self.path = self.RemSlash(self.path)
			self.f_path.append(self.path)

	def Join(self):
		self.GetDomain()
		self.GetPath()
		for domain in self.f_domain:     # Creating sites for every domain
			for path in self.f_path:     # Creating sites for every path for each domain
				tmp = 'http://' + domain + '/' + path
				self.URLs.append(tmp)
		return self.URLs



def Request(site):
	try:
		r = requests.get(site , timeout = 10)
		print site + '>> ' + r.status_code
		if r.status_code != 404:
			return site
	except:
		pass
		print '[!] Check your internet connection'

def main():
	screen_clear()
	Banner()
	print '\n' * 1
	target    = raw_input('Type your target    >')
	filename  = raw_input('Filename of paths   >')
	threads   = raw_input('How many threads?   >')
	ext       = raw_input('Script used in site >')
	if not filename:     # Defining default file containing pathlist
		filename = 'path.txt'
	if not threads:      # Defining default number of threads (actually processes)
		threads = 10
	if not ext:          # Defining default extension of language used in the site
		ext = 'php'
	raw_input('Hit ENTER if you want to proceed .....')
	threads = int(threads)
	urls = URLMaker(domain = target, path = filename)  # Using URLMaker class to make urls from domain and pathlist
	urls = urls.Join()
	f_urls =[ i.replace('\x25EXT\x25',ext) for i in urls] # Replaceing %EXT% with provided extension
	pool = MP.Pool(threads)   # Instantiated a pool class from multiprocessing module for process number
	found= pool.map(Request, f_urls)   # Getting lists of results from pool class 
	print ''
	print '[+] Found  %s ' % len(found)
	print ''
	for each in found:
		print each
	for each in f_urls:
		print each

if __name__ == '__main__':
	main()
