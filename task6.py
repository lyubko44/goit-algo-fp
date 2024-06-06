
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen_items = []
    total_calories = 0
    
    for item in sorted_items:
        if budget >= item[1]['cost']:
            budget -= item[1]['cost']
            total_calories += item[1]['calories']
            chosen_items.append(item[0])
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    # Initialize dp table
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item, item_info = item_list[i - 1]
        for j in range(1, budget + 1):
            if item_info['cost'] <= j:
                dp[i][j] = max(item_info['calories'] + dp[i - 1][j - item_info['cost']], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Find chosen items
    chosen_items = []
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp[i - 1][w]:
            continue
        else:
            item, item_info = item_list[i - 1]
            chosen_items.append(item)
            total_calories -= item_info['calories']
            w -= item_info['cost']
    
    return chosen_items, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))    