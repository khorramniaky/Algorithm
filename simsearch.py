# This code about the simple search has o(n) as linear time comlexity


arr2 = [12,34,56,87,122,134,545,565,987]

def Simsearch(arr, item):
	for i in range(len(arr)):
		if arr[i] == item:
			return i
	return None


#example 
print(Simsearch(arr2,56))	