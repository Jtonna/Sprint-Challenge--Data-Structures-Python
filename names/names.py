import time
from binary_search_tree import BinarySearchTree

#  --- Plan ---
#  

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Call the tree and pass it the names_1[0]
# for loop that inserts the name into the tree
# for loops that checks if the tree contains a name
#   append the name to duplocates because its well a duplicate

bns = BinarySearchTree(names_1[0])

for name_from_list in names_1[1:]:
    bns.insert(name_from_list)

for name_from_list in names_2:
    if bns.contains(name_from_list):
        duplicates.append(name_from_list)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

