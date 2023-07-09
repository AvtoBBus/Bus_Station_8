from Memo import Memoizator


def calc(args: list[int], mem: Memoizator) -> int:
    try:
        checker = mem.check_memory(args)
    except ValueError:
        return None
    if checker == -1:
        result = args[0] + args[1]
        mem.add_values(args, result)
        return result
    else:
        return mem.get_result(checker)


if __name__ == "__main__":
    memo = Memoizator(2)
    print(calc([1, 2], memo))       # 3 (with calc)
    print(calc([1, 2], memo))       # 3 (without calc)
    print(calc([1, 2, 3], memo))    # None
