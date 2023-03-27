'''Given two queues, one integer queue and another character KELP eue, write a python program to merge them to form a sing queue. Follow the below rules for merging: Merge elements at the same position starting with the integer
queue.If one of the queues has more elements than the other, add all the additional elements at the end of the output queue. Note: max_size of the merged queue should be the sum of the size of both the queues. 1

For example
Input
queuel: 3,6,8
queue2: b,y,u,t,r,o
Output 3,b,6,y,8,u,t,r,o
'''
def merge_queues(queue1, queue2):
    len1 = len(queue1)
    len2 = len(queue2)
    m_queue = []
    for i in range(min(len1, len2)):
        m_queue.append(queue1[i])
        m_queue.append(queue2[i])
    if len1 > len2:
        m_queue += queue1[len2:]
    elif len2 > len1:
        m_queue += queue2[len1:]
    return m_queue
queue1 = [3, 6, 8]
queue2 = ['b', 'y', 'u', 't', 'r', 'o']
m_queue = merge_queues(queue1, queue2)
print(m_queue)
