from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.core.files.uploadedfile import UploadedFile

import Image
import os

IMAGE_SIZE = 600, 400

class ImageUploadHandler(TemporaryFileUploadHandler):
	def __init__( self, *args, **kwargs ):
		super(ImageUploadHandler, self).__init__(*args, **kwargs)

	def new_file(self, file_name, *args, **kwargs):
		super(ImageUploadHandler, self).new_file(file_name, *args, **kwargs)

	def receive_data_chunk(self, raw_data, start):
		super(ImageUploadHandler, self).receive_data_chunk(raw_data, start)

	def file_complete(self, file_size):
		self.file.seek(0)
		self.file.size = file_size

		path = self.file.temporary_file_path()
		try:
			im = Image.open( path )
			im.thumbnail(IMAGE_SIZE, Image.ANTIALIAS )

			im.save(path, "JPEG")

			self.file.size = os.path.getsize(path)

			return self.file
		except IOError:
			return self.file
