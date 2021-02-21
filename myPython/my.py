import argparse

# prog: program name(程式名稱)
# usage: how to use your program(default=None, it will replace with your program name)(如何使用這個程式)
# description: describe about your program(介紹一下你的程式)

# my python
#print("hello world")


def add(a, b):
    return a / b


def main():

    # 準備參數解析
    parser = argparse.ArgumentParser()
    parser.add_argument("a", help="被除數",
                        type=int, )

    parser.add_argument("b", help="除數",
                        type=int)
    args = parser.parse_args()

    # 執行函數
    ans = add(args.a, args.b)
    print(ans)


if __name__ == "__main__":
    main()

# by NV10505
# change by PC10401
