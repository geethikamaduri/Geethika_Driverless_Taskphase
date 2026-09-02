import math
def distance(point,reference):
    x1, y1 = point
    x2, y2 = reference
    return (x2 - x1)**2 + (y2 - y1)**2

def main():
    points_input = input('enter coordinates separated by spaces: ')
    coordinates = [tuple(map(int,item.split(',')))for item in points_input.split()]

    ref_input = input('enter reference point: ')
    reference = tuple(map(int,ref_input.split(',')))

    sorted_list = sorted(coordinates,key = lambda p: distance(p,reference))
    print(sorted_list)

if __name__ == "__main__":
    main()
