def digitize(n):
    d = []
    for i in str(n):
        d.insert(0, int(i))

    return(d)

print(digitize(543210))