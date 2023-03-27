'''Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
The first element in listi should be merged with last element in list2, second element in list1 should be merged with second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other list should be kept as it is in the merged list. Sample Input
listi-['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa'] list2-['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
Expected Output
"An apple a day keeps the doctor away"
'''


list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

new_list = []
for i in range(len(list1)):
    if list1[i] is None:
        new_list.append(list2[-(i+1)])
    elif list2[-(i+1)] is None:
        new_list.append(list1[i])
    else:
        new_list.append(list1[i] + list2[-(i+1)])

merged_str = ' '.join(new_list)
print(merged_str)
