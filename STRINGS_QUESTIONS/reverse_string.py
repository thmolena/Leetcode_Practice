def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    # split the string
    # concatenate from the end

    words_list = split(s)
    # can use words_list.reverse()
    req_rever = ""
    for i in range(len(words_list) - 1, -1, -1):
        req_rever += words_list[i]
        if i != 0:
            req_rever += " "
    return req_rever

def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
        """
    num_to_swap = len(s) // 2
    y = len(s) - 1

    for i in range(num_to_swap):
        temp = s[i]
        s[i] = s[y - i]
        s[y - i] = temp
    return s

def reverseVowels(self, s: str) -> str:
    # use the two pointers approach
    i = 0
    j = len(s)-1
    ls = list(s)
    print(ls)
    vowels = "aeiouAEIOU"
    while i <=j:
        print(i)
        if ls[i] in vowels:
            if ls[j] in vowels:
                ls[i],ls[j] = ls[j],ls[i]
                print("i",i)
                i+=1
                j-=1
            else:
                j -= 1
        else:
            i += 1
    new_string = ""
    for i in ls:
        new_string += i
    return new_string
