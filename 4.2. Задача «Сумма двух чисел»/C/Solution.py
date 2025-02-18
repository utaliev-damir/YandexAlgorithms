def str_sum(str1, str2):

    result = ''
    for char1, char2 in zip(str1, str2):
        result += char1 + char2
    return result


if __name__ == '__main__':

    n = int(input())
    str1 = input()
    str2 = input()
  
    print(str_sum(str1, str2))
