'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder. Consider the range to be from 1 to 10 (both
inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.
Example:
Input Queue: 13983, 10080, 7113, 2520, 2500 (front rear)
Output Queue: 10080, 2520 (front-rear)'''
def num(queue):
    div_q= []
    for num in queue:
        if all(num % i == 0 for i in range(1, 11)):
            div_q.append(num)
    return div_q
input_queue = [13983, 10080, 7113, 2520, 2500]
output_queue = num(input_queue)
print(output_queue)
