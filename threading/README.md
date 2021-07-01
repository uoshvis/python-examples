#  Threading

###Thread

* Programming construct
* Separate flow of execution
* Uses single CPU
*  In Python, the threads may be running on different processors, but they will only be running one at a time.

###Python’s Global Interpreter Lock (GIL)

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.
On programs running in the standard CPython interpreter. **It’s not recommended to use multithreading for CPU intensive tasks in Python.** (multiprocessing is the fair alternative)

GIL provides a performance increase to single-threaded programs as only one lock needs to be managed. Removing GIL would complicate the interpreter’s code and greatly increase the difficulty for maintaining the system across every platform.


If not for CPU intensive tasks, Python threads are helpful in dealing with blocking I/O operations including reading & writing files, interacting with networks, communicating with devices like displays etc.

These tasks happen when Python make certain types of system calls. Tasks that spend much of their time waiting for external events are generally good candidates for threading.

###Summary

* Python threads can’t run in parallel on multiple CPU cores because of the global interpreter lock (GIL).

* Use Python threads to make multiple system calls in parallel. This allows us to do blocking I/O at the same time as computation.

**Code example:** [global_interpreter_lock.py](global_interpreter_lock.py)

# Thread Locks

Even though Python has a global interpreter lock, we’re still responsible for protecting against data races between the threads in our program.

Our programs will corrupt their data structures if we allow multiple threads to modify the same objects without locks.

The Lock class in the threading module is Python standard mutual exclusion lock implementation.

`counter.object += 1` is equivalent to:

```
value = getattr(counter, 'count')
result = value + 1
setattr(counter, 'count', result)
```
Python threads incrementing the counter can be suspended between any two of these operations.

To prevent data races like these and other forms of data structure corruption, Python includes a robust set of tools in the threading built-in module. The simplest and most useful of them is the Lock class, a mutual-exclusion lock(mutex).

By using a lock, we can have the Counter class protect its current value against simultaneous access from multiple threads.

**Code example:** [thread_lock.py](thread_lock.py)
