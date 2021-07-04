from decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


def main():
    tw = TimeWaster(1000)
    print('====')
    tw.waste_time(999)
    print('Here, @timer only measures the time it takes to instantiate the class')


if __name__ == '__main__':
    main()
