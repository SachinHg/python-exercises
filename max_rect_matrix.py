def max_rect_area(A):
	stack = []
	max_area = 0
	area_with_tp =0
	i = 0
	while i < len(A):
		if len(stack) == 0 or A[stack[0]] <= A[i]:
			stack.insert(0,i)
			i+=1
		else:
			tp = stack.pop(0)
			if len(stack) == 0:
				area_with_tp = A[tp]*i
			else:
				area_with_tp = A[tp]*(i-tp-1)
			if area_with_tp > max_area:
				max_area = area_with_tp
	while len(stack)>0:
		tp = stack.pop(0)
		area_with_tp = A[tp]*(i-tp-1)
		if max_area < area_with_tp:
			max_area = area_with_tp
	area_with_tp = A[tp]*i
	if area_with_tp > max_area:
		max_area = area_with_tp
	return max_area

A = [2,1,2,3,1]
print(max_rect_area(A))