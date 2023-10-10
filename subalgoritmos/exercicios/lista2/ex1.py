def recur(n : int):
    if n > 0:
        print(n)
        return n * recur(n-1)
    

recur(10)
