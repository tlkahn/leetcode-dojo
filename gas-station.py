def canCompleteCircuit(gas, cost):
    n = len(gas)
    total = 0

    # Calculate the difference between gas and cost for each station
    for i in range(n):
        total += gas[i] - cost[i]

    # If the total sum is negative, it means the total gas is insufficient to cover the total cost,
    # so there is no possible solution
    if total < 0:
        return -1

    # Initialize variables to track the current gas in the tank and the starting point
    tank = 0
    start = 0

    # Iterate through each station
    for i in range(n):
        tank += gas[i] - cost[i]

        # If the gas in the tank is negative, it means it is not possible to reach the next station from the current start point
        # Therefore, the next station should be the new start point
        if tank < 0:
            tank = 0
            start = i + 1

    # If start is equal to n, it means the entire circular route has been completed, so the start point is 0
    # Otherwise, return the start point
    return 0 if start == n else start
