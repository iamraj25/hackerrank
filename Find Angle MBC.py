import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB ** 2 + BC ** 2)
angleC = math.asin(AB/AC)
print(str(round(math.degrees(angleC)))+'°')
