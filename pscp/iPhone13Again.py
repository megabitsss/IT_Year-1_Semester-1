"""iPhone 13 Again"""
def price_finder(iphone, storage):
    """find price of each iphone specs"""
    match iphone:
        case "iPhone 13 mini":
            match storage:
                case "128 GB":
                    print(25900)
                case "256 GB":
                    print(29900)
                case "512 GB":
                    print(37900)
                case _:
                    print("Not Available")
        case "iPhone 13":
            match storage:
                case "128 GB":
                    print(29900)
                case "256 GB":
                    print(33900)
                case "512 GB":
                    print(41900)
                case _:
                    print("Not Available")
        case "iPhone 13 Pro":
            match storage:
                case "128 GB":
                    print(38900)
                case "256 GB":
                    print(42900)
                case "512 GB":
                    print(50900)
                case "1 TB":
                    print(58900)
                case _:
                    print("Not Available")
        case "iPhone 13 Pro Max":
            match storage:
                case "128 GB":
                    print(42900)
                case "256 GB":
                    print(46900)
                case "512 GB":
                    print(54900)
                case "1 TB":
                    print(62900)
                case _:
                    print("Not Available")
        case _:
            print("Not Available")
price_finder(input(), input())
