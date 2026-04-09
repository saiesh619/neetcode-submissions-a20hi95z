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
      ListNode *start = head ;
        ListNode *nxt ;
        ListNode *current = NULL;
        ListNode *prev = NULL;
        if(start){
           current  = start->next ;
           prev = start;
        }
        while(current!= NULL){
        if(current){
            nxt  = current->next;
        }
        current->next = prev  ;
        prev = current ;
        current = nxt ;
            
        }
        if(head){
        head->next = NULL ;
        cout<<head->val ;
        }
        head = prev ;
        // cout<<prev->val ;
        // cout<<head->next->val ;
        return head ;
    }
};
