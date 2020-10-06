/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *result_head, *pr, *pr_prev;
    struct ListNode *p1 = l1;
    struct ListNode *p2 = l2;
    bool carry = false;
    result_head = pr = (struct ListNode*)malloc(sizeof(struct ListNode));
    while(p1 || p2){
        int v = 0;
        if(p1){
            v += p1->val;
            p1 = p1->next;
        }
        if(p2){
            v += p2->val;
            p2 = p2->next;
        }
        if(carry){
            v++;
            carry = false;
        }
        if(v >= 10){
            carry = true;
            v -= 10;
        }
        pr->val = v;
        pr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        pr_prev = pr;
        pr = pr->next;
        pr->next = NULL;
    }
    if(carry){
        pr->val = 1;
        pr->next = NULL;
    }
    else{
        free(pr);
        pr_prev->next = NULL;
    }
    
    return result_head;
}
