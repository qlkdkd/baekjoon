x, y, w, h = map(int, input().split())
minimum = 1000

if w - x < minimum:
    minimum = w - x
if x - 0 < minimum:
    minimum = x - 0
if h - y < minimum:
    minimum = h - y
if y - 0 < minimum:
    minimum = y - 0

print(minimum)