#!/usr/bin/python3
import sys
import os
from pathlib import Path 
import readline
import urllib.request

def setup_download_dir():
	download_dir = Path('Downloaded')
	if not download_dir.exists():
		download_dir.mkdir()
	return download_dir

def get_links():
	count = 0
	num_lines = sum(1 for line in open(sys.argv[1]))
	with open(sys.argv[1]) as openedfile:
		for line in openedfile:
			url = ''.join(line.rstrip(" \n"))
			filename = url.split('/')[-1]
			print("Download %s of %s" % (count, num_lines))
			urllib.request.urlretrieve(url, 'Downloaded/'+filename)
			count+=1
	openedfile.close()



def main():
	setup_download_dir()
	get_links()



if __name__ == '__main__':
	main()