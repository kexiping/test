def make_sandwich(*items):
    """使用指定的食材制作三明治"""
    print("\n I'll make a great sandwich:")
    for item in items:
        print(f"  ...adding {item} to your sandwich.")
    print("Your sandwcih is ready!")
    
make_sandwich('roast beef', 'cheddar chese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
    