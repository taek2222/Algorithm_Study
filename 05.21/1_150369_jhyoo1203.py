cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

# cap = 2
# n = 7
# deliveries = [1, 0, 2, 0, 1, 0, 2]
# pickups = [0, 2, 0, 1, 0, 2, 0]


def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    delivery = 0
    pickup = 0
    
    for i in range(n):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (n-i) * 2
    
    return answer


print(solution(cap, n, deliveries, pickups))