class BubbleSort():


	def __init__(self, array):
		self.__array = array
		self.__sorted_array = self.__bubble_sort(self.__array)


	def __bubble_sort(self, arr):

		for i in range(len(arr)-1):

			for j in range(i+1, len(arr)):

				if arr[i] > arr[j]:
					arr[i], arr[j] = arr[j], arr[i]

		return arr


	def sorted(self):
		return self.__sorted_array

		
sort = BubbleSort([9,8,7,6,5,4,3,2,1])

print(sort.sorted())

