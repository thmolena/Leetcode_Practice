bool isPalindrome(ListNode* head) {
        ListNode * curr = head;
        if (head == NULL){
            return true;
        }
        // if(curr->next == NULL){
        //     return true;
        // }
        stack <int> myStack;

        while (curr != NULL){
            myStack.push(curr->val);
            curr = curr->next;
        }
        while(myStack.empty() == false){
            if (head->val == myStack.top()){
                head = head->next;
                myStack.pop();
            }
            else{
                return false;
            }
        }
        return true;
    }