/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *result = (int *)calloc(2, sizeof(int));
    bool bFound = false;
    for(int i=0; i<numsSize && !bFound; i++){
        for(int j=i+1; j<numsSize; j++){
            if(i == j)
                continue;
            if(nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                bFound = true;
                break;
            }
                
        }
    }
    *returnSize = (bFound) ? 2 : 0;
    return result;
}
