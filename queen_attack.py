size,obs = map(int,input().split(' '))
q_r,q_c = map(int,input().split(' '))
mat = [[0 for i in range(size)] for j in range(size)]
mat[q_r-1][q_c-1] = 9
for _ in range(obs):
	ob_x,ob_y = map(int,input().split(' '))
	mat[ob_x-1][ob_y-1] = 1
mat= mat[::-1]
print(mat)



