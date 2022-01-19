#author: DMH 1/18/22

def smash(lst):
    x = ""
    for i, v in enumerate(lst):
        if i == 0:
            x += v
        else:
            x += " " + v
    return x 

print(smash(["YO", "Wassup", "Howdy"]))
        
