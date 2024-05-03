# def pirs(x1, x2):
#     return x1 == 0 and x2 == 0

# def implications(x1, x2):
#     return not x1 or x2

# print("x1 x2 x3 f")
# for x1 in [0, 1]:
#     for x2 in [0, 1]:
#         for x3 in [0, 1]:
#             f = implications((not x1 and (pirs(x1, not x2)) and (x1 != (not x3))), x2 == x3)
#             print(f"{x1} {x2} {x3} {f}")

s = {1, 2}

# s += (1, 2, 3, 4)
# s.add(1, 2, 3)
# 

template <ForwardIterator Iter>
void update(const Iter &begin, const Iter &end);