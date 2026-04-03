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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* resList;
//Why this code also give infinite time loop?
    //    if(list1!=NULL && list2!=NULL){
    //        if(list1->val >= list2->val){
    //            resList = list2;
    //        }else{
    //            resList = list1;
    //        }
    //    }else{
    //        if(list1==NULL){
    //            resList = list2;
    //        }else if(list2 = NULL){
    //            resList = list1;
    //        }else{
    //            return NULL;
    //        }
    //    }
        ListNode* head = resList;
    //why when I reassign ListNode* resList to other value, the first value is always 0 anyway?
        while(list1!=NULL && list2!=NULL){
            cout<<list1->val<<" : "<<list2->val<<" : "<<resList->val<<endl;
            if(list1->val>=list2->val){
                resList->next = list2;
                resList = resList->next;
                if(list2->next!=NULL){
                    list2 = list2->next;
                    
                }else{
                    resList->next = list1;
                    resList = resList->next;
                    cout<<4;
                    break;
                }
            }else{
                resList->next = list1;
                resList = resList->next;
                if(list1->next!=NULL){
                    list1 = list1->next;
 //                     //Why this code caused infinite time loop?
 //                   if(list1->val>=list2->val){
 //                       resList->next = list2;
 //                       resList = resList->next;
 //                   }else{
 //                       resList->next = list1;
 //                       resList = resList->next;
//                  }
                }else{
                    resList->next = list2;
                    resList = resList->next;
                    cout<<5;
                    break;
                }
            }
        }
        if(list1==NULL){
            resList->next = list2;
            cout<<1;
        }
        if(list2==NULL){
            resList->next = list1;
            cout<<2;
        }
        
        return head->next;
    }
};
