class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(int i = 0; i<nums.size(); i++){
            for (int i2 = 0; i2<nums.size(); i2++){
                if(nums[i] == nums[i2] && i != i2){
                    return true;
                }
            }
        }
        return false;
    }
};