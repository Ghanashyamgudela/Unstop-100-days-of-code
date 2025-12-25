
# Read n and m from input
n, m = map(int, input().split())

# Dictionaries to count gifts given and received
gave_count = {i: 0 for i in range(1, n+1)}
received_count = {i: 0 for i in range(1, n+1)}

# Process each gift
for _ in range(m):
    giver, receiver = map(int, input().split())
    gave_count[giver] += 1
    received_count[receiver] += 1

# Find the youngest member: gives 0, receives n-1
for member in range(1, n+1):
    if gave_count[member] == 0 and received_count[member] == n-1:
        print(member)
        break
else:
    print(-1)
