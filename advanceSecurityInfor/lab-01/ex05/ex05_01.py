import itertools

ds = [1, 2, 3]
hoan_vi = list(itertools.permutations(ds))
print("Tất cả các hoán vị của", ds, "là:")
for hv in hoan_vi:
    print(hv)