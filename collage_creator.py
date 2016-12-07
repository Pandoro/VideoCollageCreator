#!/usr/bin/python

import json
import cv2
import numpy as np
import sys
from os import listdir
from os.path import isfile, join


print('Creating video based on: {}'.format(sys.argv[1]))
file = open(sys.argv[1])
json_data = json.load(file)
file.close()

output_size = (json_data['output_h'],json_data['output_w'])
output_folder = json_data['output_folder']
output_fname = json_data['output_fname']
background_color = json_data['background_color']


frames = []
for f in json_data['frames']:
	frames.append(f)

def get_files(fname, folder, start, stop,rate):
	files = []
	for i in range(start, stop, rate):
		f = join(folder, fname.format(i))
		if isfile(f):
			files.append(f)
	return files

#Parse all the frame setups and lists
frame_crops = []
frame_resizes = []
frame_positions = []
frame_loop = []

file_lists = []
for f in frames:
	frame_positions.append(f['position'])

	frame_crops.append(f.get('crop',None))
	frame_resizes.append(f.get('resize',None))
	frame_loop.append(f.get('loop',False))

	file_lists.append(get_files(f['fname'], f['folder'], f['start'], f['end'], f['frame_rate']))


#For each folder, check if the same amount of files, or it is set to loop
file_counts = [len(f) for f in file_lists]
max_count = np.max(file_counts)
loop_counters = [0]*len(frames)


if not np.asarray(frame_loop).all():
	#Check if those that don't loop  have the same size. Also adapt the max_count to this.
	m = np.unique(np.asarray(file_counts)[np.asarray([not l for l in frame_loop])])
	if len(m) > 1:
		raise Exception('Folders have different file numbers, or they are not set to loop!\n' + '\n'.join(['{} counts: {}'.format(f['folder'], l if not lo else 'loop') for f, l, lo in zip(frames, file_counts, frame_loop)]))
	else:
		max_count=m[0]



for i in range(max_count):
	fname = join(output_folder, output_fname.format(i))
	output = (np.ones(output_size)[...,None]*np.asarray(background_color)[None,None]).astype(np.uint8)
	for f in range(len(frames)):
		#load image
		im = cv2.imread(file_lists[f][loop_counters[f]])

		#crop
		c = frame_crops[f]
		if c is not None:
			im = im[c[0]:c[1], c[2]:c[3], :]

		#resize
		s = frame_resizes[f]
		if s is not None:
			im = cv2.resize(im, tuple(s[::-1]))

		#write
		h, w, _ = im.shape
		p = frame_positions[f]
		output[p[0]:p[0]+h, p[1]:p[1]+w, :] = im

		#Keep track of loop counters
		loop_counters[f] +=1
		if loop_counters[f] >= file_counts[f]:
			loop_counters[f] = 0

	cv2.imwrite(fname.format(i),output)





