from app.utils.stats import cache_stats

cache_stats.increment_request()
cache_stats.increment_request()

cache_stats.increment_hit()
cache_stats.increment_miss()

print(
    cache_stats.get_stats()
)