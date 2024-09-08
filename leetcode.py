import time

def evaluate(function, inputs, outputs, evaluate_time=False):
    for input_num, (i, o) in enumerate(zip(inputs, outputs)):
        a = time.time()
        if evaluate_time:
            for _ in range(100):
                function_output = function(*i)
        else:
            function_output = function(*i)
        b = time.time()
        if o == function_output:
            print(f"input {input_num} solved correctly in {b-a}sec")
        else:
            raise Exception(f"Output not matched \n\
    input: {i}\n\
    output expected : {o}\n\
    output generated: {function_output}\n")
    print(f"{len(inputs)} solved correctly")
    return True
