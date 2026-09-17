class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

        # list of users, and list of who they're following
        # keys are userId's
        # values are following list, and tweet minheap

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # for each person userId is following:
            # push to minheap that persons tweets
            # final of heap will be 10 most recent tweets
        posts = []
        minHeap = []
        self.following[userId].add(userId)

        for account in self.following[userId]:
            
            if account in self.tweets:
                index = len(self.tweets[account]) - 1
                count, tweetId = self.tweets[account][index]
                heapq.heappush(minHeap, [count, tweetId, account, index - 1])

        while minHeap and len(posts) < 10:
            count, tweetId, account, index = heapq.heappop(minHeap)
            posts.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[account][index]
                heapq.heappush(minHeap, [count, tweetId, account, index - 1])
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        # add to userId's following list

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        # remove from userId's following list
