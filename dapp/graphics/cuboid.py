def areacuboid():
	l = int(input("enter the length: "))
	b = int(input("enter the breadth: "))
	h = int(input("enter the height: "))
	area = 2*(l*b+b*h+l*h)
	return area