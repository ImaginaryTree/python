# Parameter rectangles is an array of dictionaries where each dict
# has the keys "x1", "y1", "x2" and "y2" defined with integer values
# The function should return an integer
def intersecting_rectangles(rectangles):
    #print(rectangles)
    count = 0
    for i in range(len(rectangles)):
        for j in range(i,len(rectangles)):
            if i != j:
                if rectangles[i]['x2'] > rectangles[j]['x1'] and rectangles[i]['y2'] > rectangles[j]['y1']:
                    if rectangles[i]['x1'] < rectangles[j]['x2'] and rectangles[i]['y1'] < rectangles[j]['y2']:
                        count +=1
    return count
                    
###
n = int(input())
rectangles = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split(' '))
    rectangles.append({
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    })
answer = intersecting_rectangles(rectangles)
print(answer)
