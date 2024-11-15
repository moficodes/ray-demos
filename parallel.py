import ray
ray.init()
# ray.init("ray://127.0.0.1:10001")

import time

database = [
    "Learning", "Ray", "With", "Kubernetes", "Can", "Be", "Fun", "And", "Exciting"
]


def retrieve(item):
    time.sleep(.5)
    return item, database[item]

def print_runtime(input_data, start_time):
    print(f'Runtime: {time.time() - start_time:.2f} seconds, data:')
    print(*input_data, sep="\n")

def sequential():
    print("### Running Sequentially ###")
    start = time.time()
    data = [retrieve(item) for item in range(len(database))]
    print_runtime(data, start)
    print("### Done Running Sequentially ###")


@ray.remote
def retrieve_task(item):
    return retrieve(item)


def parallel():
    print("### Running Parallelly ###")
    start = time.time()
    object_references = [
        retrieve_task.remote(item) for item in range(len(database))
    ]
    data = ray.get(object_references)
    print_runtime(data, start)
    print("### Done Running Parallelly ###")


sequential()

parallel()
