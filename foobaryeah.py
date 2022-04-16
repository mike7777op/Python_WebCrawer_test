class FooBar():
    def __init__(self, n):
            self.n = n

    def foo(self):
        foo_list =[]
        for _ in range(self.n):
            a = 'foo'
            foo_list.append(a)
        return foo_list

    def bar(self):
        bar_list = []
        for _ in range(self.n):
            b = 'bar'
            bar_list.append(b)
            # print("bar")
        return bar_list

    def yeah(self):
        yeah_list = []
        for _ in range(self.n):
            c = 'yeah'
            yeah_list.append(c)
            # print("yeah")
        return yeah_list


def convert(i,x,y,z):
    j = 0
    while j < i:
        print(x[j-1]+y[j-1]+z[j-1])
        j+=1

def main():
    x = input('input:')
    x = int(x)
    output = FooBar(x)
    foo = output.foo()
    bar = output.bar()
    yeah = output.yeah()
    convert(x,foo,bar,yeah)

if __name__ == "__main__":
    main()
