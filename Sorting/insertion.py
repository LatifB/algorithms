class InsertionSort():

	
	def __init__(self, array):
		self.__array = array
		self.__sorted_array = self.__insertion_sort(self.__array)


	def __insertion_sort(self, arr):
		
		for i in range(1, len(arr)):

			while arr[i] < arr[i-1]:

				arr[i], arr[i-1] = arr[i-1], arr[i]

		return arr


	def sorted(self):
		return self.__sorted_array


sort = InsertionSort([64, 34, 25, 12, 22, 91, 90])
print(sort.sorted())