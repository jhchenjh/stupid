# 23 Jan, 2020
# Runtime: 116 ms, faster than 5.47% of Python online submissions for Add Two Numbers.
# Memory Usage: 12 MB, less than 5.88% of Python online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        num1 = 0
        num2 = 0
        while l1 is not None:
            mul = 10**i
            num1 = num1 + l1.val*mul
            l1 = l1.next
            i = i+1
        i = 0
        while l2 is not None:
            mul = 10**i
            num2 = num2 + l2.val*mul
            l2 = l2.next
            i = i+1
        ans = num1 + num2
        print(num1, num2, ans)
        result = ListNode(ans%10)
        new_node = result
        while ans/10!=0:
            ans = ans/10
            new_node.next = ListNode(ans%10)
            new_node = new_node.next
        return result

# 23 Jan, 2020
# Runtime: 104 ms, faster than 5.47% of Python online submissions for Add Two Numbers.
# Memory Usage: 11.8 MB, less than 80.88% of Python online submissions for Add Two Numbers.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        new_node = result
        carry = 0
        add = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                add = add + l1.val
                l1 = l1.next
            if l2 is not None:
                add = add + l2.val
                l2 = l2.next
            add = add + carry
            new_node.next = ListNode(add%10)
            if add/10!=0:
                carry = add/10
            else:
                carry = 0
            add = 0
            new_node = new_node.next
        if carry!=0:
            new_node.next = ListNode(carry)
        return result.next
