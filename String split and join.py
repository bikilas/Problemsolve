def split_and_join(line):
    # Split the line by spaces
    words = line.split(" ")
    
    # Join the words using hyphen
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
