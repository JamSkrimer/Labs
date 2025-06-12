def sum_string_lengths(sequence):
    if isinstance(sequence, str):
        return sum(len(s) for s in sequence.split())
    return sum(len(s) for s in sequence)

test_string = ("Connection terminated. Im sorry to interrupt you Elizabeth, if you still even remember that name. But Im afraid youve been misinformed. "
               "You are not here to receive a gift, nor have you been called here by the individual you assume. Although you have indeed been called.")
print(sum_string_lengths(test_string))

