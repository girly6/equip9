from collections import defaultdict

def preprocess_maintenance_logs(maintenance_logs):
    cost_by_date = defaultdict(int)
    
    # Aggregate costs by date
    for _, date, cost in maintenance_logs:
        cost_by_date[date] += cost
    
    # Sort dates and compute prefix sum
    sorted_dates = sorted(cost_by_date.keys())
    prefix_sum = {}
    total = 0
    for date in sorted_dates:
        total += cost_by_date[date]
        prefix_sum[date] = total
    
    return prefix_sum, sorted_dates

def get_total_cost_in_range(prefix_sum, sorted_dates, start_date, end_date):
    if start_date > end_date:
        return 0
    
    # Find the nearest available dates in the prefix sum
    valid_dates = [date for date in sorted_dates if date >= start_date and date <= end_date]
    
    if not valid_dates:
        return 0
    
    last_date = valid_dates[-1]
    first_date = valid_dates[0]
    
    return prefix_sum[last_date] - (prefix_sum[first_date] - cost_by_date[first_date] if first_date > sorted_dates[0] else 0)

def process_queries(maintenance_logs, queries):
    prefix_sum, sorted_dates = preprocess_maintenance_logs(maintenance_logs)
    
    results = []
    for start_date, end_date in queries:
        results.append(get_total_cost_in_range(prefix_sum, sorted_dates, start_date, end_date))
    
    return results

# Example input
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

# Function call
print(process_queries(maintenance_logs, queries))
