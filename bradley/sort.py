# def bubble_sort(a_list):
#     for pass_num in range(len(a_list)-1, 0, -1):
#         for i in range(pass_num):
#             if a_list[i] > a_list[i+1]:
#                 temp = a_list[i]
#                 a_list[i] = a_list[i+1]
#                 a_list[i+1] = temp

# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# print(a_list)

# def short_bubble_sort(a_list):
#     exchanges = True
#     pass_num = len(a_list) - 1
#     while pass_num > 0 and exchanges:
#         exchanges = False
#         for i in range(pass_num):
#             if a_list[i] > a_list[i+1]:
#                 exchanges = True
#                 temp = a_list[i]
#                 a_list[i] = a_list[i+1]
#                 a_list[i+1] = temp
#         pass_num -= 1
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# short_bubble_sort(a_list)
# print(a_list)

# def selection_sort(a_list):
#     for fill_slot in range(len(a_list)-1, 0, -1):
#         pos_of_max = 0
#         for location in range(1, fill_slot+1):
#             if a_list[location] > a_list[pos_of_max]:
#                 pos_of_max = location
#
#         temp = a_list[fill_slot]
#         a_list[fill_slot] = a_list[pos_of_max]
#         a_list[pos_of_max] = temp
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selection_sort(a_list)
# print(a_list)

# def insertion_sort(a_list):
#     for index in range(1, len(a_list)):
#         current_value = a_list[index]
#         position = index
#         while position > 0 and a_list[position-1] > current_value:
#             a_list[position] = a_list[position-1]
#             position = position - 1
#         a_list[position] = current_value
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertion_sort(a_list)
# print(a_list)

# def merge_sort(a_list):
#     print("Splitting ", a_list)
#     if len(a_list) > 1:
#         mid = len(a_list) // 2
#         left_half = a_list[:mid]
#         right_half = a_list[mid:]
#
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i=0
#         j=0
#         k=0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 a_list[k] = left_half[i]
#                 i += 1
#             else:
#                 a_list[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_half):
#             a_list[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             a_list[k] = right_half[j]
#             j += 1
#             k += 1
#
#         print("Merging ", a_list)
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# merge_sort(a_list)
# print(a_list)

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point-1)
        quick_sort_helper(a_list, split_point+1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while (left_mark <= right_mark) and (a_list[left_mark] <= pivot_value):
            left_mark += 1
        while (a_list[right_mark] >= pivot_value) and (right_mark >= left_mark):
            right_mark -= 1

        if right_mark < left_mark:
            done = True

        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)
