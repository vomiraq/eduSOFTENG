def poluchit_chast_kortezha(kortezh, element):
    if element not in kortezh:
        return ()
    perviy = kortezh.index(element)
    try:
        vtoroy = kortezh.index(element, perviy + 1)
        return kortezh[perviy:vtoroy + 1]
    except ValueError:
        return kortezh[perviy:]

print(poluchit_chast_kortezha((1, 2, 3), 8))            
print(poluchit_chast_kortezha((1, 8, 3, 4, 8, 8, 9, 2), 8)) 
print(poluchit_chast_kortezha((1, 2, 8, 5, 1, 2, 9), 8))    