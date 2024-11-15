import ray
import time

# ray.init("ray://127.0.0.1:10001")
ray.init()

@ray.remote
def some_function():
  return 1

obj = some_function.remote()

print(ray.get(obj))