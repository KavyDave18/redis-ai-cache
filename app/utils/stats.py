class CacheStats:

    def __init__(self):
        self.total_requests=0
        self.cache_hits=0
        self.cache_misses=0

    def increment_request(self):
        self.total_requests+=1

    def increment_hit(self):
        self.cache_hits += 1

    def increment_miss(self):
        self.cache_misses +=1

    def get_stats(self):

        hit_rate=0

        if self.total_requests>0:
            hit_rate = (self.cache_hits/self.total_requests)*100

        return {
                "total_requests": self.total_requests,
                "cache_hits": self.cache_hits,
                "cache_misses": self.cache_misses,
                "hit_rate": round(hit_rate, 2)
            }

cache_stats = CacheStats()