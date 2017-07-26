no = int(input())
n = no+1
n = str(n)
n = list(n)
num1 = n[:3]
num2 = n[3:]
num1 = [int(x) for x in num1]
sum1 = sum(num1)
num2 = [int(x) for x in num2]
sum2 = sum(num2)
if sum1 > sum2:
	diff = sum1 - sum2
	num_selected = num2
elif sum2 > sum1:
	diff = sum2 - sum1
	num_selected = num1
else:
	diff = 0
i = 2
while i>=0 and diff > 0:
	if num_selected[i]+diff <= 9:
		num_selected[i] = num_selected[i]+diff
		break
	else:
		adder = 9 - num_selected[i]
		num_selected[i]+= 9 - num_selected[i]
		diff = diff - adder
		print(":::",diff)
		i-=1
print(num1)
print(num2)
