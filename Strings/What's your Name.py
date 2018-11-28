def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        if(string[i]==sub_string[0]):
            #print("i value is {} len value is {}".format(i,len(sub_string)))
            end=i+len(sub_string)
            if(end<=len(string)and string[i:end]==sub_string):
                #print(string[i:end])
                c=c+1
    return(c)


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)


