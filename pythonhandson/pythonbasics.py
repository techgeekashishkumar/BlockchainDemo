block_chain = []


def add_value():
    block_chain.append(5.3)
    print(block_chain)


# function with argument
def add_arg_value(transaction):
    block_chain.append(transaction)
    print(block_chain)


add_value()
add_value()
add_value()
add_arg_value(10.89)

# print the last value of list
print(block_chain[-1])

# for loop implementation
for block in block_chain:
    print('Outputting block', block)

# while loop implementation
while True:
    print('Populating data')
    block_chain.append(add_arg_value(10.98))
    break


# verify the blockchain
def verify_chain():
    block_index = 0
    isValid = True
    for block in block_chain:
        if block[0] == block_chain[block_index - 1]:
            isValid = True
        else:
            isValid = True
            break
    return isValid


verify_chain()
