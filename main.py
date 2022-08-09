import time


def main():
    while True:
        n = int(input("Enter task number or 0 to exit: "))
        match n:
            case 0:
                return None
            case _:
                exec(f"import task.t{n}")
                start = time.time()
                eval(f"print(task.t{n}.main())")
                print(f"Elapsed time {time.time() - start} seconds")


if __name__ == '__main__':
    main()
