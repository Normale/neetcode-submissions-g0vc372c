class Twitter:

    def __init__(self):
        self.user_tweets = dict() # user_id -> heap of (tweet, timestamp)
        self.follows = dict() # user_id -> list of followed
        self.timestamp = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = list()
        item = (self.timestamp, tweetId)
        heapq.heappush(self.user_tweets[userId], item)
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        if userId not in self.follows or not self.follows[userId]:
            users = {userId}
        else:    
            users = self.follows[userId].copy()
        users.add(userId)
        
        for user in users:
            if user not in self.user_tweets or not self.user_tweets[user]:
                continue
            top10 = heapq.nsmallest(10, self.user_tweets[user])
            for item in top10:
                heapq.heappush(result, item)
        return [tweet_id for timestamp, tweet_id in heapq.nsmallest(10, result)]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
