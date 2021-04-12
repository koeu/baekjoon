x, y, w, h = map(int, input().split())
minum = min(x,y,abs(w-x), abs(h-y))
print(minum)