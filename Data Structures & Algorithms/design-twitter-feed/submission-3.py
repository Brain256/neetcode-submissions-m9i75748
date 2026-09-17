class Twitter:

    def __init__(self):

        self.follows = defaultdict(list)
        self.tweets = defaultdict(list)
        self.index = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.index += 1
        self.tweets[userId].append((-self.index, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        feed = []
        self.follow(userId, userId)

        res = []

        for uId in self.follows[userId]: 
            if self.tweets[uId]: 
                length = len(self.tweets[uId])-1
                heapq.heappush(feed, (self.tweets[uId][length][0], self.tweets[uId][length][1], uId, length-1))
            
        while feed and len(res) < 10: 

            tweet = heapq.heappop(feed)
            res.append(tweet[1])

            if tweet[3] >= 0: 
                heapq.heappush(feed, (self.tweets[tweet[2]][tweet[3]][0], self.tweets[tweet[2]][tweet[3]][1], tweet[2], tweet[3]-1))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]: 
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: 
            self.follows[followerId].remove(followeeId)
        
