# Step 1: Read input
N = int(input())
strings = [input().strip() for _ in range(N)]
k = int(input())

# Step 2: Count occurrences
count = {}
for s in strings:
    count[s] = count.get(s, 0) + 1

# Step 3: Collect unique strings in order
unique_strings = [s for s in strings if count[s] == 1]

# Step 4: Output kth unique string
if k <= len(unique_strings):
    print(unique_strings[k-1])
else:
    print(-1)
