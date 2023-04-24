def make_shirt(shirt_size, shirt_word='I Love python' ):
    """一个尺码以及要印到T恤上的字样"""
    print(f"This shirt's size is {shirt_size} ")
    print(f'it should print {shirt_word}\n')

make_shirt('medium', 'M')
make_shirt('large', shirt_word='L')
make_shirt('large')
make_shirt('medium')
make_shirt('')