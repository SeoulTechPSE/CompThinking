def main():
    print("-- run test.py --", __debug__)

    if __debug__:
        print("-- debug run --")
    else:
        print("-- release run --")

if __name__ == '__main__':

    main()