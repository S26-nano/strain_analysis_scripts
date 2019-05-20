def remove_hot_pixels(data):
	data[359,106]=0
	data[45,293]=0
	data[164,311]=0
	return data
