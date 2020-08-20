class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        bool bFound = false;
        for(int i = 0; i < nums.size() && !bFound; i++){
            for(int j = i+1; j < nums.size(); j++){
                if(i == j)
                    continue;
                if(nums[i] + nums[j] == target){
                    result.push_back(i);
                    result.push_back(j);
                    bFound = true;
                    break;
                }
            }
        }
        return result;
    }
};
