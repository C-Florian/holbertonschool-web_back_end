# Python - Async Comprehension

This project demonstrates how to use asynchronous generators, asynchronous comprehensions, and how to measure runtime when running tasks concurrently in Python.

## Project Structure

### Files
- **0-async_generator.py**  
  Contains the coroutine `async_generator` which:
  - loops 10 times,
  - asynchronously waits 1 second on each iteration,
  - yields a random floating-point number between 0 and 10.

- **1-async_comprehension.py**  
  Contains the coroutine `async_comprehension` which:
  - uses an asynchronous comprehension to collect 10 numbers from `async_generator`,
  - returns the numbers as a list.

- **2-measure_runtime.py**  
  Contains the coroutine `measure_runtime` which:
  - runs `async_comprehension` 4 times in parallel using `asyncio.gather`,
  - measures and returns the total runtime (≈ 10 seconds).

### Test Files
- **0-main.py**, **1-main.py**, **2-main.py**  
  Test files provided to validate the behavior of the coroutines.

## Learning Objectives

By the end of this project, you should be able to:
1. Write an asynchronous generator using `async def` and `yield`.
2. Use asynchronous comprehensions:  
   ```python
   [i async for i in async_generator()]
