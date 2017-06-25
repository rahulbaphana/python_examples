class Operations:
    def add(self, a, b):
        return a + b


    def iterative_sum(self, numbers):
        sum = self.get_initial_value_from(numbers)
        validated_numbers = self.get_validated(numbers)
        for e in validated_numbers:
            sum = self.add(sum, e)
        return sum


    def tail_rec_sum(self, numbers):
        validated_numbers = self.get_validated(numbers)
        def reduce(index, numbers, acc):
            return acc if not numbers else reduce(index-1 , numbers[:-1], self.add(acc, numbers[index]))
        return reduce(len(validated_numbers)-1, validated_numbers, self.get_initial_value_from(numbers))


    def get_initial_value_from(self, numbers):
        return None if not numbers else numbers[-1]
        

    def get_validated(self, numbers):
        return [] if not numbers else numbers[:-1]