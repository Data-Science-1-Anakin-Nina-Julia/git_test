###random change here 
def assignment(new_list, i, old_list, j):
    '''
    Change entry of new_list at position i to entry from old_list at position j
    '''
    new_list[i] = old_list[j]  #reassginment


def merge_sort(list_to_sort_by_merge):
    '''
    Sortes the list_to_sort_by_merge with the merge-sort algorithm recursively
    '''

    if (len(list_to_sort_by_merge) > 1):
        mid_position = len(list_to_sort_by_merge) // 2 #compute middle position (with rounding)
        left_list = list_to_sort_by_merge[:mid_position] #left half of list_to_sort_by_merge
        right_list = list_to_sort_by_merge[mid_position:] #right half of list_to_sort_by_merge

        #sort left and right half recursively
        merge_sort(left_list) #recursive function call for left half
        merge_sort(right_list) #recursive function call for right half

        #set indices
        left_index = 0  #index for left_list
        right_index = 0     #index for right_list
        new_index = 0   #index for 'new' list (i.e. overwriting of list_to_sort_by_merge)

        #if left and right index has not reached end of the list respectively
        while left_index < len(left_list) and right_index < len(right_list):
    new_index += 1

        #above while ready -> one list (left_list or right_lift) 'finished' ie. index at most right mid_position
        #check what list index not at the end and fill entries of new list up with remaining entries

        #left_index not at right position of left_list?
        while left_index < len(left_list):
            assignment(list_to_sort_by_merge, new_index, left_list, left_index)
            left_list += 1
            new_index += 1

        #right_index not at right position of right_list?
        while right_index < len(right_list):
            assignment(list_to_sort_by_merge, new_index, right_list, right_index)
            right_index += 1
            new_index += 1

#plot list entries before and after sorting
import matplotlib.pyplot as plt

#create list
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.bar(x, my_list)
plt.x_label('Position in der Liste')
plt.y_label('Eintrag in der Liste')
plt.title('Liste ohne Änderung')
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.bar(x, my_list)
plt.x_label('Position in der Liste')
plt.y_label('Eintrag in der Liste')
plt.title('Liste sortiert')
plt.show()
