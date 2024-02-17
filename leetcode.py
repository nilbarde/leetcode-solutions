def evaluate(function, inputs, outputs):
    for input_num, (i, o) in enumerate(zip(inputs, outputs)):
        function_output = function(*i)
        if o == function_output:
            print(f"input {input_num} solved correctly")
        else:
            raise Exception(f"Output not matched \n\
    input: {input}\n\
    output expected: {o}\n\
    output generated: {function_output}\n")
    print(f"{len(inputs)} solved correctly")
    return True
