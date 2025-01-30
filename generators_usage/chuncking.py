from utils.generators import chunk_list


def main():
    data = list(range(10))  # [0,1,2,3,4,5,6,7,8,9]

    for chunk in chunk_list(data, 3):
        print(chunk)


if __name__ == '__main__':
    main()
