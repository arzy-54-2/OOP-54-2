# __iter__() - возвращает сам итератор.
# __next__() - возвращает следующий элемент или вызывает StopIteration,
# если элементы закончились.


class Counter:

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            num = self.current
            self.current +=1
            return num
        else:
            raise StopIteration

# for i in Counter(5):
#     print(i)


def counter_up_to(limit):
    current = 0
    while current < limit:
        yield current
        current += 1


# for num in counter_up_to(5):
#     print(num)

#
# def return_num(list, index):
#     return list[index]

# O(n) – Линейная сложность

def find_element(lst, target):
    for i in lst:
        if target == i:
            return i
    return "Нету"

# print(find_element(tt, 5738))


#

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid +1
        else:
            right = mid - 1
    return "Нету"

# my_array = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(my_array, 13))

tt = [1,23,4,35,44,54,6,57,65,86,578,79,68,75]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# print(bubble_sort(tt))

# O(n)
def two_sum(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

arr = [3,3]
print(two_sum(arr, 6))

