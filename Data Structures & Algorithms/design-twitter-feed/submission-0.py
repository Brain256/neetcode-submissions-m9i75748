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
        feed += self.tweets[userId]

        res = []

        for uId in self.follows[userId]: 
            feed += self.tweets[uId]

        heapq.heapify(feed)

        while feed and len(res) < 10: 
            res.append(heapq.heappop(feed)[1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]: 
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: 
            self.follows[followerId].remove(followeeId)
        
