import time

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для знаходження мінімальної кількості монет.
    Завжди вибирає найбільшу доступну монету.
    """
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            coin_count[coin] = count
            amount -= coin * count

    return coin_count

def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для знаходження мінімальної кількості монет.
    """
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return {}

    coin_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    return coin_count

def compare_algorithms(amount):
    """ Функція для порівняння швидкодії двох алгоритмів. """
    # Жадібний алгоритм
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Алгоритм динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    # Вивід результатів
    print(f"Сума: {amount}")
    print(f"Жадібний алгоритм: {greedy_result}, Час виконання: {greedy_time:.6f} сек")
    print(f"Алгоритм динамічного програмування: {dp_result}, Час виконання: {dp_time:.6f} сек")

if __name__ == "__main__":
    compare_algorithms(113)
