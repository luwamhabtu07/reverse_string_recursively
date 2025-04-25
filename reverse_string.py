def reverse_string(s):
    # Base case: if string is empty or one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: reverse rest of the string and add the first character at the end
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    example = "TextWise"
    print(reverse_string(example))  # Output: "esiWtxeT"
