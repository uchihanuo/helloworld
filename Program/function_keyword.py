def func(a, b=3, c=10):
    print('a is', a, 'b is', b, 'c is', c)


func(5)
func(5, 7, 9)
func(5, c=2)
func(c=2, a=10)
