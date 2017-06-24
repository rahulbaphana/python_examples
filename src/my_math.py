class Operations:
    def add(self, a, b):
        return a + b

    def iterative_sum(self, numbers):
        sum = 0
        for e in numbers:
            sum = self.add(sum, e)
        return sum

    def tail_rec_sum(self, numbers):
        def reduce(index, numbers, acc):
            #Uncomment the print to see the tail-rec optimization
            #print("index:{} , numbers:{} , acc:{}".format(index, numbers, acc))
            if index < 0:
                return acc
            else: 
                return reduce(index-1 , numbers[:-1], self.add(acc, numbers[index]))
        return reduce(len(numbers)-1, numbers, 0)
