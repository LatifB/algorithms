def merge_sort(arr):

    if len(arr) > 1:

        mid_point = len(arr) // 2

        L = arr[mid_point:]
        R = arr[:mid_point]

        L = merge_sort(L)
        R = merge_sort(R)

        L_iter = iter(L)
        R_iter = iter(R)

        temp_arr = []

        for i in range(min(len(R), len(L))):
            r = next(R_iter)
            l = next(L_iter)

            if r < l:
                temp_arr.append(r)
                try:
                    r = next(R_iter)
                except:
                    try:
                        while True:
                            temp_arr.append(l)
							try:
								l = next(L_iter)
							except:
								pass
                    except:
                        pass
                    break

            else:
                temp_arr.append(l)
                try:
                    l = next(L_iter)
                except:
                    try:
                        while True:
                            temp_arr.append(r)
							try:
	                            r = next(R_iter)
							except:
								pass
                    except:
                        pass
                    break

        return temp_arr

    return arr


arr = [64, 34, 25, 12, 22, 91, 90]

print(merge_sort(arr))

"""
You say you're Muslim, you say you're Rasta
Say you don't eat pork, don't eat pussy
Liar
"""
