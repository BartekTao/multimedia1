import winsound

for note in [65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 124]:
	winsound.Beep(int(note), 500)