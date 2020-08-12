# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Delete a Node

"""

UPER:
U: 
    >
P:
E:
R:

"""

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):

    cur = head
    count = 0

    while cur is not None:
        print(cur.data)
        
        

        cur = cur.next
        count += 1 