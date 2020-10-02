class RecursiveBubbleSort():


	def __init__(self, array):
		self.__array = array
		self.__sorted_array = self.__recursive_bubble(self.__array)


	def __recursive_bubble(self, arr, index=1):

		for i in range(0, len(arr)-index):

			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

		if index < len(arr):
			return self.__recursive_bubble(arr, index+1)
		else:
			return arr

	def sorted(self):
		return self.__sorted_array

		
sort = RecursiveBubbleSort([64, 34, 25, 12, 22, 11, 90])

print(sort.sorted())
