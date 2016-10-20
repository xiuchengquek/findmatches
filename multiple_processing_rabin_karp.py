




from multiprocessing import Queue, Process
import multiprocessing











## write your matching function here
def find_matches(input, output):
    results = []
    for value in iter(input.get, 'STOP'):
        previous_x = ''
        for x in value[0]:
            if x != previous_x:
                current_value = [ s for s in value[1] if x in s ]

            results.append(current_value)
            previous_x = x

    output.put(results)


def run():
    ## Start 2 CPU queue , one for input one for output . you can choose not to use a output queue if you do not need to ensure that the output need to not overlap
    input = Queue()
    output = Queue()



    ## example
    columns = ['a','a','a','b','c'] * 10000
    demul = [{'a','b','c'}, {'c','a'}] * 5




    ncores = 4 ## change this to the number of core you want to use

    num = float(len(columns))/ncores
    chunked_list = [ columns [i:i + int(num)] for i in range(0, (ncores-1)*int(num), int(num))]
    chunked_list.append(columns[(ncores-1)*int(num):])


    ## add your task to the columns
    for task in chunked_list:
        input.put([task, demul])


    ## Run based on the number of your columns you have . run the matching function.
    for w in range(int(ncores)):
        Process(target=find_matches, args=(input, output)).start()

    ## add a stop signal for each cores
    for i in range(int(ncores)):
        input.put('STOP')



    for w in range(len(chunked_list)):
        print(output.get())





if __name__ == '__main__':
    run()


