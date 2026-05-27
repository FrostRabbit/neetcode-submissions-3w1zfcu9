class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l=0;
        int r=nums.size()-1;
        while(l<=r){
            if(nums[l]==val){
                nums[l] = nums[r];
                r--;
                continue;
            }
            l++;
        }
        return l;
    }
};