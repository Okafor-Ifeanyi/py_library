# Sync prog means everything happens sequenctially 
# function runs after each other
# async means we dont need to wait for other programs to run before we run the code we want.
# An event loops is a prog construct or design pattern that waits for and dispatches events or 
# messages in a program, a lower level thing that allows us to write a async code.
# Await can only be inside an async func.


import asyncio

async def main():
    print("tim")
    foo('test')

async def foo(text):
    print(text)
    await asyncio.sleep(2)

asyncio.run(main())

# main()