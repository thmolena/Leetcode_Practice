def isPalindrome(self, head: ListNode) -> bool:
    stack = []
    current = head
    secCurrent = head
    while current == None:
        return True

    while current:
        stack.append(current.val)
        current = current.next
    stackReversed = stack[::-1]

    return stack == stackReversed

