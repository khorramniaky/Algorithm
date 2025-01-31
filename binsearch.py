#This code about binary search and has o(log n) time complexity

arr1 = [12,34,56,87,122,134,545,565,987]

def Binsearch(arr, item):
	#set left and right corner of array
	left = 0
	right = len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		guess = arr[mid] #midlle of array
		if guess == item:
			return mid
		if guess < item:
			left = mid + 1
		else:
			right = mid - 1
	return None 


#example 
print(Binsearch(arr1,565))



