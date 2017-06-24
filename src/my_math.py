class Operations:
    def add(self, a, b):
        return a + b


    def iterative_sum(self, numbers):
        sum = 0
        validated_numbers = [] if self.is_valid(numbers) else numbers
        for e in validated_numbers:
            sum = self.add(sum, e)
        return sum


    def tail_rec_sum(self, numbers):
        validated_numbers = [] if self.is_valid(numbers) else numbers

        def reduce(index, numbers, acc):
            if self.is_valid(numbers):
                return acc
            else: 
                return reduce(index-1 , numbers[:-1], self.add(acc, numbers[index]))
        return reduce(len(validated_numbers)-1, validated_numbers, 0)


    def is_valid(self, numbers):
        return not numbers
