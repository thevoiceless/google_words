#!/usr/bin/env python

'''
Made in response to http://www.reddit.com/r/Android/comments/1u2npt/i_was_snooping_around_the_voice_search_app_and_it/
Iterates through a word list (/usr/share/dict/words in this case) and checks if Google has an mp3 for it.
'''

import httplib
import urlparse

URL = 'https://ssl.gstatic.com/dictionary/static/sounds/de/0/'

# http://stackoverflow.com/a/2486412/1693087
# http://pythonadventures.wordpress.com/2010/10/17/check-if-url-exists/
def exists(url):
	# Get elements 1 and 2 (host and path) from the parsed URL
	host, path = urlparse.urlparse(url)[1:3]
	conn = httplib.HTTPConnection(host)
	# Make HEAD request (instead of GET)
	conn.request('HEAD', path)
	response = conn.getresponse()
	conn.close()
	return response.status == 200

# Number of valid words
count = 0
# Number of checked words (used as a progress indicator when running)
iterations = 0

with open('/usr/share/dict/words', 'r') as f, open('valid.txt', 'w') as out:
	for word in f:
		# Ignore the possessive forms of words just to trim down the total number
		if "'s" in word:
			continue
		elif exists(URL + word.strip() + '.mp3'):
			count += 1
			out.write(URL + word.strip() + '.mp3\n')
		iterations += 1
		print iterations

print count