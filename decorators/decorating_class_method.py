from decorators import debug, timer


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


def main():
    tw = TimeWaster(1000)
    print('====')
    tw.waste_time(999)


if __name__ == '__main__':
    main()
