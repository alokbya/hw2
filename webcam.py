
#!/usr/bin/env python3


import requests
from PIL import Image
from io import StringIO, BytesIO
from threading import Thread, Lock
from time import sleep, time


class Webcam:
	def __init__(self, url='http://webcam.oregonstate.edu/cam/mu/live/live.jpg'):
		self.url = url

		self.callback = None
		self.callback_wait = 1

		self.callback_thread = Thread(target=self._callback_servicer)

	def __del__(self):
		self.running = False
		self.callback_thread.join()

	def _callback_servicer(self):
		while self.running:
			start_time = time()
			try:
				self.callback(self.grab_image())
			except:
				pass

			while time() - start_time < self.callback_wait:
				sleep(0.01)

	def start(self):
		self.running = True
		self.callback_thread.start()

	def stop(self):
		self.running = False
		self.callback_thread.join()

	def grab_image(self):
		response = requests.get(self.url)
		return Image.open(BytesIO(response.content))

	def register_callback(self, callback, frequency):
		self.callback = callback
		self.callback_wait = 1 / frequency


def callback(image):
	print('I am a callback')



if __name__ == '__main__':
	w = Webcam()
	w.register_callback(callback, 1)
	w.start()
	input('Hit Enter to Stop')


	w.stop()
