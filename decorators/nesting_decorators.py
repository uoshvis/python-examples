from decorators import debug, do_twice


@debug
@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
@debug
def greet_reverse(name):
    print(f"Hello {name}")


def main():
    greet("Eva")
    print('======')
    greet_reverse('Nora')


if __name__ == '__main__':
    main()
