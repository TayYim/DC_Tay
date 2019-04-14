import os
# DATA_PATH = "../TestData/"
DATA_PATH = "../Data/"
BLACK_PATH = os.path.join(DATA_PATH, "black_count")
WHITE_PATH = os.path.join(DATA_PATH, "white_count")


def get_api_set(path):
    folders = os.listdir(path)

    api_list = []

    for folder in folders:
        if os.path.isdir(os.path.join(path, folder)):
            files = os.listdir(os.path.join(path, folder))
            f = open(os.path.join(os.path.join(path, folder),
                                  "api_name"), "r")  # read api_name file
            for line in f.readlines():
                api_name = line.split(" ")[0]
                api_list.append(api_name)
            f.close()
    return set(api_list)


if __name__ == "__main__":
    black_api_list = get_api_set(BLACK_PATH)
    white_api_list = get_api_set(WHITE_PATH)
    print("Only in black samples:")
    print(black_api_list - white_api_list)
    print("Only in white samples:")
    print(white_api_list - black_api_list)
    print("All api used:")
    print(black_api_list | white_api_list)
