#https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    slow = node
    fast = node.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next

    return count
