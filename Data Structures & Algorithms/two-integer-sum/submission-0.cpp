class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        for(int i = 0; i<nums.size(); i++){
            for(int i2 = 0; i2<nums.size(); i2++){
                if(i!=i2 && nums[i] + nums[i2] == target){
                    return {i, i2};
                }
            }
        }
    }
};
