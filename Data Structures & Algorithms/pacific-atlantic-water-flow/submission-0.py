class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        mp = set()
        ma = set()
        st = []
        res = []
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(heights)
        cols = len(heights[0])
        for i in range(cols):
            st.append((0,i,heights[0][i]))
            mp.add((0,i))
        for i in range(rows):
            st.append((i,0,heights[i][0]))
            mp.add((i,0))
        while st:
            r,c,z = st.pop()
            for i,j in dirs:
                x,y = r+i,c+j
                if (x,y) in mp or x < 0 or y<0 or x >=rows or y >= cols \
                or heights[x][y] < z:
                    continue
                mp.add((x,y))
                st.append((x,y,heights[x][y]))
                
        for i in range(cols):
            st.append((rows-1,i,heights[rows-1][i]))
            ma.add((rows-1,i))
        for i in range(rows):
            st.append((i,cols-1,heights[i][cols-1]))
            ma.add((i,cols-1))

        while st:
            r,c,z = st.pop()
            for i,j in dirs:
                x,y = r+i,c+j
                if (x,y) in ma or x < 0 or y<0 or x >=rows or y >= cols \
                or heights[x][y] < z:
                    continue
                ma.add((x,y))
                st.append((x,y,heights[x][y]))         

        for i in range(rows):
            for j in range(cols):
                if (i,j) in mp and (i,j) in ma:
                    res.append([i,j])
        return res