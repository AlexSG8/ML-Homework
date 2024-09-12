in_length = int(input())
in_width = int(input())
piece = int(input())
print("Output:", not(bool((in_length % piece)%2) and bool((in_width % piece)%2)))
