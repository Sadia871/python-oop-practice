class countdown_iterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1
# Test
cd = countdown_iterator(100000)
for number in cd:
    print(number)
# Output:
# 5