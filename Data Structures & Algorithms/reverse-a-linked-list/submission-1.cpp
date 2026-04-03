/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * current = head;
        ListNode * head2;
        vector<int> reversed;
        ListNode * result = nullptr;

        if(current == NULL){
            return current;
        }
        while(current!= NULL){
            reversed.push_back(current->val);
            current = current->next;
        }
        result = new ListNode;
        head2 = result;
        for(int i = reversed.size()-1; i>=0 ; i--){
            result->val = reversed[i];
            if(i!=0){
                result->next = new ListNode;
                result = result->next;
            }
        }
        return head2;
    }
};
