'''
Downloads the NASA's "Image of the Day" using the feedparser module.
The image is shown in the console, and can optionally be saved to the camera roll, using the photos module.
'''

import feedparser
import urllib
from PIL import Image
import photos
import dialogs

def main():
	feed = feedparser.parse('http://nasa.gov/rss/dyn/lg_image_of_the_day.rss')
	latest = feed['entries'][0]
	title = latest['title']
	description = latest['summary']
	print '%s\n\n%s' % (title, description)
	links = latest['links']
	image_url = None
	for link in links:
		if link.get('type').startswith('image'):
			image_url = link.get('href')
	if image_url:
		urllib.urlretrieve(image_url, 'ImageOfTheDay.jpg')
		img = Image.open('ImageOfTheDay.jpg')
		img.show()
		dialogs.alert('Save to Camera Roll?', title, 'Save')
		photos.save_image(img)
		dialogs.hud_alert('Image Saved')

if __name__ == '__main__':
	main()