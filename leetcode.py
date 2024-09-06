import time

def evaluate(function, inputs, outputs):
    for input_num, (i, o) in enumerate(zip(inputs, outputs)):
        a = time.time()
        function_output = function(*i)
        b = time.time()
        if o == function_output:
            print(f"input {input_num} solved correctly in {b-a}ms")
        else:
            raise Exception(f"Output not matched \n\
    input: {i}\n\
    output expected : {o}\n\
    output generated: {function_output}\n")
    print(f"{len(inputs)} solved correctly")
    return True
