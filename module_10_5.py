import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        string = True
        while string:
            string = file.readline()
            all_data.append(string)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()
for i in filenames:
    read_info(i)
end = time.time()
print(end - start)

start = time.time()
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    end = time.time()
    print(end - start)
