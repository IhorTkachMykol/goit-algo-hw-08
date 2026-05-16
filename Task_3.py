import heapq

def min_cost_cables(cables):
    """
    Знаходить мінімальні витрати на з'єднання всіх кабелів.
    cables: список довжин кабелів
    Повертає: (загальні витрати, список кроків з'єднання)
    """
    if not cables or len(cables) == 1:
        return 0, []

    heap = cables[:]
    heapq.heapify(heap)          # будуємо мін-купу за O(n)

    total_cost = 0
    steps = []

    while len(heap) > 1:
        a = heapq.heappop(heap)  # найкоротший кабель
        b = heapq.heappop(heap)  # другий найкоротший

        cost = a + b             # витрати на це з'єднання
        total_cost += cost

        steps.append((a, b, cost, total_cost))
        heapq.heappush(heap, cost)  # результат повертаємо у купу

    return total_cost, steps


# --- Тест ---
cables = [4, 3, 2, 6, 5]

total, steps = min_cost_cables(cables)

print(f"Кабелі: {sorted(cables)}")
print(f"{'Крок':<6} {'Кабель A':<12} {'Кабель B':<12} {'Витрати кроку':<16} {'Загалом'}")
print("-" * 56)
for i, (a, b, cost, running) in enumerate(steps, 1):
    print(f"{i:<6} {a:<12} {b:<12} {cost:<16} {running}")
print(f"\n Мінімальні загальні витрати: {total}")
