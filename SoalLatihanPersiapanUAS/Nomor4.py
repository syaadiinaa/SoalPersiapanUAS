def sum_without_twenties(a, b, c):
    def filter_twenty(x):
        return x if x < 20 or x > 29 else 0
    
    return filter_twenty(a) + filter_twenty(b) + filter_twenty(c)

#penggunaan
print(sum_without_twenties(10, 20, 30))
print(sum_without_twenties(25, 15, 29))