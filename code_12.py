def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return get_fibonacci_number(position-2)+get_fibonacci_number(position-1)


def get_fibonacci_number_sequence(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    
    previous_x = 1
    previous_y = 1

    number_sequence = [1,1]

    for i in range(2,n):
        current = previous_x + previous_y
        previous_x = previous_y
        previous_y = current

        number_sequence.append(current)

    return number_sequence

if __name__ == "__main__":
# testing out position
    position = 3
    fib_num = get_fibonacci_number(position)
    print(f"The fibonacci number in position {position} is {fib_num}")
# testing out sequence 
    n = 7
    fib_sequence = get_fibonacci_number_sequence(n)
    print(f"The Fibonacci sequence for {n} is {fib_sequence} ")


