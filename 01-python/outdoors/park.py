def draw_park(length = 5, width = 5):
	"""
	Print the park with specific length and width

	Parameters:

	Length (int) : the length of the park.
	Width (int) : the width of the park.

	Returns:
	No return.

	"""
	if length < 0 or width < 0:
		raise ValueError("Please input valid length and width")
	for _ in range (length):
		print()
		for _ in range (width):
			print("|-|", end = "")

	if length != 0:
		print()

