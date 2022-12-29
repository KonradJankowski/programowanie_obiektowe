class Products:
    pass

class Orders:
    pass

class Apple:
    pass

class Potato:
    pass


if __name__ == '__main__':
    green_apple = Apple()
    apple = Apple()
    apple_2 = [Apple(), Apple()]
    potato_1 = Potato()
    potato_2 = Potato()
    print("green apple type: ", type(green_apple))
    print(" object apple: ", type(apple))
    print(" object apple_2: ", type(apple_2[1]))
    print(" objrct potato_1: ", type(potato_1))
    print(" objrct potato_2: ", type(potato_2))
    print(apple_2)

    products = {
        "jablko" : Products(),
        "Ziemniaki" : Products(),
        "Marchew" : Products(),
        "Ciastka" : Products(),
    }
    print(products)