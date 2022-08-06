arrivals = sorted([float(x) for x in input().split()])
departures = sorted([float(x) for x in input().split()])
print(arrivals)
print(departures)
lenght = len(arrivals)

result = 1
platform_needed = 1
i = 1
j = 0

while i < lenght and j < lenght:
    if arrivals[i] < departures[j]:
        platform_needed += 1
        i += 1

    elif arrivals[i] >= departures[j]:
        platform_needed -= 1
        j += 1

    result = max(result, platform_needed)

print(result)
