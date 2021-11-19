#https://practice.geeksforgeeks.org/problems/reach-a-given-score-1587115621/1/?category[]=Dynamic%20Programming&category[]=Dynamic%20Programming&page=1&query=category[]Dynamic%20Programmingpage1category[]Dynamic%20Programming

def count(n):
    memset = []
    reducers = [3,5,10]
    count = n
    for number in reducers:
        container = []
        while count > 0:
            if count - 3 >= 0:
                count -= 3
                container.append(3)
            elif count - 5 >= 0:
                count -= 5
                container.append(5)
            elif count - 10 >= 0:
                count -= 10
                container.append(10)
            else:
                container = []
                break
        if container not in memset and not []:
            memset.append(container)
        count = n
    return len(memset)




# your code here

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    # for _ in range(int(input())):
    #     n = int(input())
    #     print(count(n))
    print(count(20))

# } Driver Code Ends