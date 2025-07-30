A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Union
union_AB = A.union(B)
print("1:", union_AB)

# 2. Intersection
intersection_AB = A.intersection(B)
print("2:", intersection_AB)

# 3. A est-il un sous-ensemble de B ?
print("3:", A.issubset(B))

# 4. A et B sont-ils disjoints ?
print("4:", A.isdisjoint(B))

# 5. Join A avec B et B avec A (équivalent à union)
print("5:", A.union(B))
print("5:", B.union(A))

# 6. Différence symétrique
symmetric_diff = A.symmetric_difference(B)
print("6:", symmetric_diff)

# 7. Supprimer complètement les ensembles
A.clear()
B.clear()
print("7:", A, B)
