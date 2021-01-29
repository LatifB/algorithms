class InsertionSort:

	def __init__(self, arr):
		self.__arr = arr
		self.__sorted_array = self.__insertion_sort(self.__arr)

	def __insertion_sort(self, arr):

		for i in range(1, len(arr)):

			for ii in range(0, i):
				
				if arr[i] < arr[ii]:
					# do i cheat if i use insert() ???
					arr.insert(ii, arr[i])
					del arr[i+1]
					break

		return arr

	def sorted(self):
		return self.__sorted_array

insertion_sort = InsertionSort([64, 34, 25, 12, 22, 91, 90])

print(insertion_sort.sorted())