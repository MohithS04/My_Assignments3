bike = {                     #using clear()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
bike.clear()
print(bike)

bike = {                     #using copy()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}

x = bike.copy()               
print(x)

x = ('key1', 'key2', 'key3')    #using fromkeys()
y = 0

thisdict = dict.fromkeys(x,y)
print(thisdict)

bike = {                      #using get()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
x = bike.get("model")
print(x)

bike = {                      #using items()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
x = bike.items()
print(x)

bike = {                      #using keys()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
x = bike.keys()
print(x)

bike = {                      #using pop()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
bike.pop("model")
print(bike)

bike = {                      #using popitem()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
bike.popitem()
print(bike)

bike = {                       #using setdefault()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
x = bike.setdefault("model", "RR310")
print(x)

bike = {                       #using update()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
bike.update({"color":"Silver"})
print(bike)

bike = {                      #using values()
    "brand":"Apache",
    "model":"RTR160",
    "year":2009
}
x = bike.values()
print(x)
