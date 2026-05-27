class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> m;
        vector<int> res;
        for(int num:nums1){
            m[num] =1;
        }
        for(int num:nums2){
            if(m[num]==1){
                res.push_back(num);
                m[num] = 0;
            }
        }
        return res;
    }
};