import random

def generate_and_sort():
    rnum_list = [random.randint(0, 100) for _ in range(200)]
    rnum_list.sort()
    return rnum_list

def counting(list):
    categories = [0, 0, 0, 0, 0]
    for num in list:
        if 1 <= num <= 20:
            categories[0] += 1
        elif 21 <= num <= 40:
            categories[1] += 1
        elif 41 <= num <= 60:
            categories[2] += 1
        elif 61 <= num <= 80:
            categories[3] += 1
        elif 81 <= num <= 100:
            categories[4] += 1
    return categories

def print_star(category):
    labels = ["1 - 20", "21 - 40", "41 - 60", "61 - 80", "81 - 100"]
    for i in range(5):
        stars = "*" * category[i]
        print(f"{labels[i]}: {stars} {category[i]}")

if __name__ == "__main__":
    num_list = generate_and_sort()
    ans_category = counting(num_list)
    enter = 0
    for i in num_list:
        print(i, end=" ")
        enter+=1
        if enter==20:
            enter = 0
            print("\n")
    print("\n-----------------------------------------------\n")
    print_star(ans_category)
