def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s_split = string[i:i+k]
        output = s_split[0]
        for s in s_split[1:]:
            if s in output:
                continue
            output += s
        print(output)

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
