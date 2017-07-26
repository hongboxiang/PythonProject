"""
2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""
import os


def write_file():
    with open("./commonTool.txt", 'w') as f:
        for filename in os.listdir('.'):
            f.write(filename + '\n')


if __name__ == '__main__':
    write_file()
