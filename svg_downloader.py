import sys
import os
import requests

def getFileName(url):
	filename = os.path.basename(url)
	filename_with_underscores = filename.replace('-', '_')
	path_parts = url.split('/')
	category = path_parts[-2]
	return f"{category}__{filename_with_underscores}"

def getUrlsFromFile(urls, file):
	with open(file, 'r') as file:
		for line in file:
			urls.append(line.strip())

def main(urls, location):
	for url in urls:
		response = requests.get(url)

		filename = os.path.basename(url).replace('-', '_')

		with open(f'{location}/{getFileName(url)}', 'w') as file:
			file.write(response.text)

if __name__ == '__main__':
	flag_url = False
	flag_UrlInFile = False
	flag_location = False

	urls = []
	location = './'
	file = ''

	if len(sys.argv) > 1: 
		for arg in sys.argv:

			if arg == '-url' and file == '':
				flag_url = True
				flag_UrlInFile = False
				flag_location = False
				continue

			if arg == '-file' and len(urls) == 0:
				flag_url = False
				flag_UrlInFile = True
				flag_location = False
				continue

			if arg == '-location':
				flag_url = False
				flag_UrlInFile = False
				flag_location = True
				continue

			if flag_url:
				urls.append(arg)

			if flag_UrlInFile:
				file = arg
				getUrlsFromFile(urls, file)

			if flag_location: location = arg

	main(urls, location)
