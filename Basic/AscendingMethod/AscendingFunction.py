def ascending(ls):
	lst = list(ls)
	isAscending = True
	for i in range(0, len(lst)-1):
		if(lst[i] <= lst[i+1]):
			isAscending = True
		else:
			isAscending = False
			break
	if(isAscending):
		return True
	else:
		return False
