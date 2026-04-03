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
    bool hasCycle(ListNode* head) {
        ListNode * current = head;
        vector<ListNode*> elements;
        while(current!=NULL){
            for(int i = 0; i<elements.size(); i++){
                for(int i2 = 0; i2<elements.size(); i2++){
                    if(elements[i]==elements[i2] && i!=i2){
                        return true;
                    }
                }
            }
            elements.push_back(current);
            current = current->next;
        }

        return false;
    }
};
