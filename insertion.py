class Qsort:
	def __init__(self):
		self.count = 0
	def swap(self,b,c,d):
		t = b[c]
		b[c] = b[d]
		b[d] = t
		return b
	def partition(self,a,s,e):
		pivot=e
		pindex=s
		for i in range(s,e):
			if a[i]<=a[pivot]:
				self.swap(a,i,pindex)
				self.count+=1
				pindex+=1
		self.count+=1
		self.swap(a,pindex,pivot)
		return pindex

	def qsort(self,a,s,e):
		if s<e:
			pIndex=self.partition(a,s,e)
			self.qsort(a, s, pIndex-1)
			self.qsort(a, pIndex+1, e)
		return self.count


class Insertion:
    def __init__(self):
        self.count=0
    def insertion(self,a):
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while j>=0 and a[j]>key:
                self.count+=1
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
        return self.count


n = int(input())
arr = list(map(int,input().split(' ')))
arr2 = arr[:]
quick = Qsort()
insert = Insertion()
print(insert.insertion(arr)-quick.qsort(arr2,0,n-1))


