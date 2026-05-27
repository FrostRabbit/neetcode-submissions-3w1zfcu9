class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int w=0,b=0;
        int l=0,r=0;
        int res=INT_MAX;
        while(r<blocks.length()){
            if(blocks[r]=='W'){
                w++;
            }else{
                b++;
            }

            if(r-l+1<k){
                r++;
                continue;
            }
            res = min(res,w);
            if(blocks[l]=='W'){
                w--;
            }else{
                b--;
            }
            
            r++;
            l++;
        }
        return res;
    }
};