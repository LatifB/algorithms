class SelectionSort():


	def __init__(self, array):
		self.__array = array
		self.__sorted_array = self.__selection_sort(self.__array)


	def __selection_sort(self, arr):
		
		for i in range(len(arr)-1):
			min_index = i+1

			for j in range(min_index+1, len(arr)):

				if arr[j] < arr[min_index]:
					min_index = j

			if arr[min_index] < arr[i]:
				arr[i], arr[min_index] = arr[min_index], arr[i]

		return arr

	def sorted(self):
		return self.__sorted_array

		
sort = SelectionSort([9,8,7,6,5,4,3,2,1])

print(sort.sorted())
