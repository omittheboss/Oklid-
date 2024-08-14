import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

points = []
n = int(input("Kaç tane nokta gireceksiniz?: "))

for i in range(n):
    x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
    y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
    points.append((x, y))

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("Minimum Öklid Mesafesi:", min_distance)
