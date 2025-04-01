import heapq

def match_best_prices(requests, sellers):
    # Organize sellers in a min-heap for each equipment type
    seller_map = {}
    for equip, price in sellers:
        if equip not in seller_map:
            seller_map[equip] = []
        heapq.heappush(seller_map[equip], price)
    
    # Process each request
    result = []
    for equip, max_price in requests:
        if equip in seller_map:
            while seller_map[equip] and seller_map[equip][0] > max_price:
                heapq.heappop(seller_map[equip])  # Remove overpriced options
            result.append(heapq.heappop(seller_map[equip]) if seller_map[equip] else None)
        else:
            result.append(None)
    
    return result

# Example input
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

# Function call
print(match_best_prices(requests, sellers))
