def main():
    n= int(input())
    arr=list(map(int,input().split()))
    
    sum1=n*(n+1)//2
    print (sum1-sum(arr))
main()