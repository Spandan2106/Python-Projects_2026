import time
import re
from datetime import datetime, timedelta
from collections import defaultdict

class LogAggregator:
    def __init__(self):
        self.logs = []
        # Inverted index for fast keyword lookups: word -> set of log indices
        self.inverted_index = defaultdict(set)
        # Sliding-window metrics tracking
        self.error_counts = []

    def ingest_log(self, level, message, timestamp=None):
        ts = timestamp or datetime.now()
        log_entry = {
            "timestamp": ts,
            "level": level.upper(),
            "message": message
        }
        
        idx = len(self.logs)
        self.logs.append(log_entry)

        # Track error rates for metrics
        if log_entry["level"] in ("ERROR", "FATAL"):
            self.error_counts.append(ts)

        # Tokenize message for inverted index
        tokens = re.findall(r'\w+', message.lower())
        for token in tokens:
            self.inverted_index[token].add(idx)

    def search(self, keyword=None, level=None, start_time=None, end_time=None):
        results = set(range(len(self.logs)))

        # Filter by keyword using inverted index
        if keyword:
            kw_tokens = re.findall(r'\w+', keyword.lower())
            for token in kw_tokens:
                matching_indices = self.inverted_index.get(token, set())
                results.intersection_update(matching_indices)

        # Filter by log level and time range
        filtered_logs = []
        for idx in sorted(results):
            log = self.logs[idx]
            if level and log["level"] != level.upper():
                continue
            if start_time and log["timestamp"] < start_time:
                continue
            if end_time and log["timestamp"] > end_time:
                continue
            filtered_logs.append(log)

        return filtered_logs

    def get_error_rate_last_minute(self):
        now = datetime.now()
        cutoff = now - timedelta(minutes=1)
        # Clean up old timestamps and count errors within the last 60 seconds
        self.error_counts = [ts for ts in self.error_counts if ts >= cutoff]
        return len(self.error_counts)

# --- Example Usage ---
if __name__ == "__main__":
    logger = LogAggregator()

    # Ingesting sample logs
    logger.ingest_log("INFO", "User login successful for user_id: 1042")
    logger.ingest_log("WARN", "Database connection pool reached 85% capacity")
    logger.ingest_log("ERROR", "Failed to process payment transaction for user_id: 1042")
    logger.ingest_log("INFO", "Cache refreshed successfully")

    print("--- Searching for keyword 'user_id' ---")
    results = logger.search(keyword="user_id")
    for log in results:
        print(f"[{log['timestamp'].strftime('%H:%M:%S')}] [{log['level']}] {log['message']}")

    print("\n--- Searching for ERROR logs ---")
    error_results = logger.search(level="ERROR")
    for log in error_results:
        print(f"[{log['timestamp'].strftime('%H:%M:%S')}] [{log['level']}] {log['message']}")

    print(f"\nErrors in the last minute: {logger.get_error_rate_last_minute()}")
