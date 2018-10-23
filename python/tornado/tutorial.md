# Deep understanding python asynchronous programming of `tornado`

Thoroughly understand what, why, and how asynchronous programming is. 
And learning the basic concept of `tornado` asynchronous programming.

* `Keywords`: Asynchronous, Non-blocking, concurrency, asyncio, coroutine, event loop, tornado.

# Introduction

This article will include three part of content.

## Part One:

Before we talking about `tornado`, this part will try to introduce the basic concept of python asynchronous programming you should know. Though this part learning, using those concepts to help us understand how `tornado` working at asynchronous programming.

1. Explain what is asynchronous programming is and its closely related concepts such as blocking/non-blocking, synchronous/asynchronous, concurrent/parallel, etc. (Explaining the basic concept which will thorough all of this article.)

2. Why we need to use asynchronous programming. 

3. How to develop from synchronous blocking to asynchronous non-blocking.

4. How does `epoll`, `Callback` and `Event loop` works.

5. How asynchronous programming gradually moves from callbacks to generators to native coroutine.

6. How the lib `asyncio` works in python 3.5.

## Part Two: 

Though the first part of learning, this part will start looking inside of `tornado` package itself.

1. Though demo codes to understand how the function be decorated by `@gen.coroutine` executed involving from `Future`, `Runner` to `IOLoop`.

## Part Three: 
Though some demo codes to introduce some usefull module in `tornado`.

1. Demo code of use `tornado.concurrent`.
2. Demo code of use `tornado.log`.


# What is the asynchronous programming.

Through the following concept, explain what the asynchronous programming is. If you already know what's the actually asynchronous programming is, you can skip this part.

## blocking

* The program process will be suspended when it does not get the required computing resources.
* The program is **unable to continue doing something else** while waiting for an operation to complete, saying that the program is blocked on the operation.
* The commom blocking process is like: network I/O blocking, disk I/O blocking, user input blocking, and so on.

For example, when you order a meal, you need waiting for the meal completed and between this period you can not do other something.

## non-blocking

* When the program is waiting for an operation, **itself is not blocked**, and can continue to run other things. Then the program is said to be non-blocking in the operation.

Take a familiar example like above, you order a meal and this time when you waiting for it you can do something your like.

## Synchronization

* In order to accomplish a certain task, different program units need to be **coordinated** by some communication method during execution, and these program units are saids to be executed synchronously.
* In short, **synchronization means order**.

## Asynchronous

* In order to complete a task, there is **no need for coordinating communication** between different program units. and the task can be completed.
* Unrelated program units can be asynchronous.
* In short, **asynchronous means unordered**.

## Concurrency

* Concurrency is when multiply tasks can execute and complete in overlapping time periods. It's doesn't necessarily mean they'll ever both be running at the same instant.

For example, **multitasking on a single-core machine**.

## Parallelism 

* Tasks literally run at the same time. 

For example, **multitasking on multi-core processor**.

## Concept summary

* **Non-blocking** is to improve the efficiency of overall program execution.
* **Asynchronous** is the way to efficiency the non-blocking tasks.
* **Parallelism** is adopted with acceleration multitasking completion with multi-core.
* **Concurrency** is to allow independent subtasks to have the opportunity to executed as soon as possible, but not necessarily to speed up the overall progress.

## Asynchronous programming

* Through multi-process, multi-threads, coroutine, function and method are used as the basic approach of the multitask program, and combine with callback, event loop, and other mechanisms to improve the overall efficiency and concurrent of program is be called `Asynchronous Programming`.

For some cases when we meet a I/O operation like read and write to the database or files, we don't want our program process blocked to waiting for those result return, in that case the `non-blocking` approach is adopted. And sometimes you have to query different user's info in the database, as it is not sequence operation, in that case you can use `asynchronous` approach. But in some case like user want to change his password, here you need get the user info first then change the user password, this is sequence, `synchronous` approach is good choice, and also you want handle different user to change password, that is why you need `non-blocking` you user password change operation.

# Why we need use asynchronous programming.

## Cost problem

If a program can't effectively use a computer resource, it will inevitably require more computer to make up for the calculation demand gap. For example if the server threshold of handling client requests per seconds is 1,000, for the 10,000 expected requests we may need create at least 10 of server instance. But what if one server already can handle 10,000 requests in which can cut nearly 90% cost.

## C10k/C10M problem

[The C10k problem](https://en.wikipedia.org/wiki/C10k_problem) is how to provide a single server with FTP service for 10,000 clients in a 1GHz CPU, 2G memory, and 1gbps network environment. And after 2010, with the development of hardware technology, this problem is extended to C10M, that is, how to use 8 core CPU, 64G memory, maintain 10 million concurrent connections on 10gbps network, or process 1 million per second. connection.

## Solution

The CPU tells use that it is very fast, but the context switching is slow, memory read data is slow, disk addressing is slow and fetching data is slow. In short, everything after leaving the CPU is slow except for level 1 cache. Which make the **I/O become the biggest bottleneck**.

# The road to asynchronous I/O evolution.

This part I will use the case of improving the efficiency of **network I/O** of fetching data from the Internet to introduce the asynchronous programming evolution.

And the mission is download 10 pages from the Internet.

## Synchronous blocking mode

The easiest solution to think of is to download them by order, from setting up a socket connection to sending a network request to reading the response data in sequence.
```python
def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect((host, port))
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response
```
And execute the fetching data by 10 times range. 
```python
def sync_way():
    res = []
    for i in range(10):
        res.append(thread_way())
    return len(res)
```
Result: The blocking way of fetching 10 pages will cost 1.81 seconds.

We know that creating a network connection is not determine by the client, but by the network transportation capability and processing speed of the server. Also we unpredictable to when the response will be received from the server.

As the reasons at above pointed out, the methods `sock.connect()` and `sock.recv()` are blocked by default.

For downloading the 10 pages from the web, it will blocking 20 times for waiting the connection and data receive. We can noticed that the efficiency of this synchronous approach is very slow.

## Improvement: Multi-process

The first solution of improve it is to open 10 identical programs at the some time. Use the multi-cores advantages to make every programs running in a dependent process. The code is like the following:
```python
import futures
def process_way():
    workers = 10
    # open some processors which depended on your computer  core numbers.
    with futures.ProcessPoolExecutor(workers) as executor:
        thread_futures = {executor.submit(blocking_way) for i in range(10)}
    return len([future.result() for future in thread_futures])
```
The improvement is immediately effected. But there are still have some problems. The overall time-consuming has not been reduced to one-tenth of the original one, but which is one-sixth, so where does the time spent? The answer is process switching overhead.

**When the number of processes is greater than the number of CPU cores, process switching is necessarily required.**


## Improve: Multi-threaded

