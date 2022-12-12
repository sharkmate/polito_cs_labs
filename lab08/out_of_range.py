def main():
    dummie = [1, 2, 3, 4, 5, 6]
    new_list = list()
    for num in dummie:
        new_list.append(dummie[num]+dummie[num+1])


if __name__ == "__main__":
    main()