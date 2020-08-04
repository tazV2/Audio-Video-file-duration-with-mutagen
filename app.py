import os
from mutagen.mp4 import MP4

all_files = os.listdir()


for i in all_files:
	mp4 = 'mp4'
	if os.path.abspath(i).endswith(mp4):
		detalis = MP4(os.path.abspath(i))
		print(f"Duration of {i} is {detalis.info.length/60} mins")
