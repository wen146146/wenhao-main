def get_name() -> str:
    """
    获取用户输入的名字并返回。
    """
    name = input("请输入你的名字：")
    return name


def main() -> None:
    """
    简单示例：询问名字并打招呼。
    """
    name = get_name()
    print(f"你好，{name}！欢迎使用这个程序。")


if __name__ == "__main__":
    main()

