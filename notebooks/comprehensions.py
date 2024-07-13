from pprint import pprint as pp


def main():
    pp([i for i in range(10)])
    pp([i for i in range(50) if i % 2 == 0])
    l = [
        "any",
        "all",
        "sum",
        "any",
        "all",
        "sum",
        "apple",
        "banana",
        "cherry",
        "",
    ]
    pp([name for name in l if name if name[0] != "a" if name[-1] != "y"])
    matrix = [[i + j for i in range(5)] for j in range(5)]
    pp(matrix)
    pp([i for row in matrix for i in row])


if __name__ == "__main__":
    main()
