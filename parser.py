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
setup_download_dir()

def get_links():
	with open(sys.argv[1]) as openedfile:
		for line in openedfile:
			filename = ''.join(line.rstrip("\n").split('/')[-1:])
			print("[%s] Downloading %s -> %s", filename, line)
			urllib.request.urlretrieve(line, filename)
	openedfile.close()

setup_download_dir()
get_links()