w = input().upper()
nw = list(set(w))

wl = []
for i in nw:
    wl.append(w.count(i))

if wl.count(max(wl)) > 1:
    print("?")
else:
    print(nw[(wl.index(max(wl)))])