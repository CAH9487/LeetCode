#include <stdio.h>
#include <limits.h>

// Runtime: 28 ms, faster than 19.38% of C online submissions
// Memory Usage: 6.2 MB, less than 42.38% of C online submissions
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int idx_1 = -1;
    int idx_2 = -1;
    int idx_target = (nums1Size + nums2Size + 1) / 2;
    int is_odd = (nums1Size + nums2Size) % 2;
    int n1, n2;
    double result = -1;
    //printf("idx_target = %d\n", idx_target);
    //printf("is_odd = %d\n", is_odd);
    while (idx_1 < nums1Size - 1 || idx_2 < nums2Size - 1) {
        n1 = n2 = INT_MAX;
        if (idx_1 + 1 < nums1Size) {
            n1 = nums1[idx_1 + 1];
        }
        if (idx_2 + 1 < nums2Size) {
            n2 = nums2[idx_2 + 1];
        }
        if (n1 > 0 && n1 < n2) {
            idx_target--;
            idx_1++;
            //printf("n1 = %d\n", n1);
            if (idx_target <= 0) {
                result = n1;
                break;
            }
        }
        else {
            idx_target--;
            idx_2++;
            //printf("n2 = %d\n", n2);
            if (idx_target <= 0) {
                result = n2;
                break;
            }
        }
    }
    if (!is_odd) {
        //printf("idx_1 = %d, idx_2 = %d\n", idx_1, idx_2);
        idx_1++;
        idx_2++;
        if (idx_1 < nums1Size && idx_2 < nums2Size) {
            n1 = nums1[idx_1];
            n2 = nums2[idx_2];
            //printf("result += %d\n", (n1 < n2) ? n1 : n2);
            result += (n1 < n2) ? n1 : n2;
            result /= 2;
        }
        else {
            //printf("result += %d\n", (idx_1 < nums1Size) ? nums1[idx_1] : nums2[idx_2]);
            result += (idx_1 < nums1Size) ? nums1[idx_1] : nums2[idx_2];
            result /= 2;
        }
    }
    return result;
}

int main()
{
    int n1[] = { 2 };
    int n2[] = {};
    int size1 = sizeof(n1) / sizeof(int);
    int size2 = sizeof(n2) / sizeof(int);
    printf("%lf\n", findMedianSortedArrays(n1, size1, n2, size2));
    return 0;
}

