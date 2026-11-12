from collections import defaultdict,deque
import heapq
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # tid,timestamp,uid
        self.users = defaultdict(set) # uid,follwers
        self.history = defaultdict(deque)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[tweetId] = (self.count, userId)
        if len(self.history[userId]) > 10:
            self.history[userId].append((self.count,tweetId))
            self.history[userId].popleft()
        else:
            self.history[userId].append((self.count,tweetId))
        self.count+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        results = []
        followers = self.users[userId] | {userId}
        for f in followers:
            if self.history[f]:
                idx = len(self.history[f]) - 1
                post = self.history[f][idx]
                h.append((-post[0],post[1],f,idx))
        heapq.heapify(h)

        while h and len(results) < 10:
            post = heapq.heappop(h)
            results.append(post[1])
            if post[3] > 0:
                next_post = self.history[post[2]][post[3]-1]
                heapq.heappush(h,(-next_post[0],next_post[1],post[2],post[3]-1))

        return list(results)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)  
        