unsorted = [1,9,2,4,0,8,14,6]
sorted =[]
for _ in unsorted:
    indexToPlace = len(sorted)
    for i,num in enumerate(sorted):
        if _ > num:
            indexToPlace = i
            break
    sorted.insert(indexToPlace,_)

print(sorted[:4])
