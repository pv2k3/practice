import threading

"""
# Multithreading!!

Multithreading:
		 We use threading to run multiple threads (tasks, function calls) at the same time. 
		 This means that your program will have two things happening at the same time.

Thread :
	A thread is a lightweight process which do not require much memory.

Process :
	A process can have more than one thread.

For example:
	You starts any game in your device that game is going to be main
	process and in that game many things like global chat, 
	friends status(online or offline), any slide show of events 
	udates every seconds they are running separately in their own( threads ).

Benefits of threading: 
	Program remains responsive.
	The master behind visual animations in  Apps.

Multithreading in Python is done by threadin module.

Lets have an example...
"""

# import Thread
import threading

# temp function
def a(name):
	for i in range(100):
		print( threading.current_thread().name)
		print("My name is" + name)



# t1 = threading.Thread(target=a, args=("Thread 1", ))
# t2 = threading.Thread(target=a, args=("Thread 2", ))

# t1.start()
# t2.start()


"""
Here is output of above program...

My name isThread 1My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2

My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1

As you can see they are running at the sane time but not in  any manner.

How to deal with it?

>> join() method..
"""


t1 = threading.Thread(target=a, args=("Thread 1", ), name="my thread >> t1")
t2 = threading.Thread(target=a, args=("Thread 2", ), name="my thread >> t2")

t1.start()
t2.start()
t1.join()
t2.join()



"""
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 1
My name isThread 2
My name isThread 2
My name isThread 1My name isThread 2
My name isThread 2
My name isThread 1
My name isThread 1
My name isThread 1

My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2
My name isThread 2

As we add .join() method second therad will run after only when first thread has
completed its execution.

output may vary because of CPU....
"""

# The threadin module: 
	# >>>> threading.activeCount() returns number of active threads
	# >>>> threading.currentThread() returns count of thread objects in the caller's thread control
	# >>>> threading.enumerate() returns a list of all active thread objects.

# Thread methods:
	# >>>> run() this marks the entry point of the thread
	# >>>> start() this starts the execution of thread by calling run method
	# >>>> join()  waits for thread to terminate...
	# >>>> is_alive() cheks whether a thread is still active or not
	# >>>> name   retuns the name of thread.

	