def Main():

    def DrunkenPython(some_number):
        def strtoint(some_str):
            return int(some_str)

        def inttostr(some_int):
            return str(some_int)

        if type(some_number) == int:
            return inttostr(some_number)
        else:
            return strtoint(some_number)


    print(DrunkenPython(5))
    print(DrunkenPython("11"))


if __name__ == '__main__':
    Main()