
def twoCitySchedCost( costs: list[list[int]]) -> int:
    n=len(costs)
    costs.sort(key=lambda cost:cost[0]-cost[1])
    total=0
    for i in range(n):
        if i<n//2:
            total+=costs[i][0]
            continue
        total+=costs[i][1]
    return total
print(twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))