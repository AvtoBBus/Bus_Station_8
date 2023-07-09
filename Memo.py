class Memoizator():
    __arg_num = 0
    __arg_mas = []
    __res_mas = []

    def __init__(self, arg_num: int) -> None:
        self.__arg_num = arg_num
        self.__arg_mas = []
        self.__res_mas = []

    def check_memory(self, arg_mas: list) -> int:
        if len(arg_mas) != self.__arg_num:
            raise ValueError
        try:
            return self.__arg_mas.index(arg_mas)
        except ValueError:
            return -1

    def get_result(self, index: int):
        return self.__res_mas[index]

    def add_values(self, args: list, result) -> None:
        self.__arg_mas.append(args)
        self.__res_mas.append(result)
