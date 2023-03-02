Jonah Jepson

March 1, 2023

IT FDN 110

Assignment07

# Pickling and Structured Error Handling

## Introduction

The purpose of this assignment is to create a script and an accompanying knowledge document that explains how to use the pickle module in python and demonstrates structured error handling. To do this we are going to look at some fictional examples that involve a student named Charlie Brown.

### Pickling and Unpickling

Charlie Brown didn't do so well on the final exam, and he is afraid that he may not pass his class. While his teacher was out of the room, he decided to sneak a peak at the student grade file on her computer. To his dismay it all looked like a bunch of gibberish! That's because his teacher used the pickle module in python to save her grade file.


### What is Pickle?

The python pickle module is used to serialize and de-serialize python objects. "Pickling" is the process that "serializes" or converts python objects into a byte stream (0's and 1's). Conversely, unpickling is the act of de-serializing byte streams back into python objects. This can be extremely useful because it allows for easier storage and transfer of data from system to system.

### Pickling

To use the pickle module, it must be imported. At the beginning of the script type "import pickle" to load the pickle module. Next, to pickle your data and save it to a file you first open the file in binary write mode (using _open(file\_name, 'wb')_)then you use the command _pickle.dump(your\_data, file\_name)_ to pickle your data into a byte stream and write it to the file. For an example, see how Charlie Brown's teacher used python to pickle her grade book:

![](RackMultipart20230302-1-jwzwc0_html_c2b0c1b57e7e2f37.png)

When we open the pickled 'StudentGrades.pickle' file in a text editor this is what we see:

![](RackMultipart20230302-1-jwzwc0_html_8a16138dfcf2f00c.png)

### Unpickling

Unpickling works similarly to pickling. At the top of the script you must import the pickle module then open the file in binary read mode (using _open(file\_name, 'rb')_)and use the command _pickle.load(file\_name,)_ to read your data from the file and unpickle it from the byte stream. To unpickle his teachers grade file, Charlie Brown's Script needs to look like this:

T ![](RackMultipart20230302-1-jwzwc0_html_15bd2effbca8e995.png) his code will read the pickled data and output it in the form that it was input. See the output:

![](RackMultipart20230302-1-jwzwc0_html_1353ed02a928367d.png)

## Structured Error Handling

You may be wondering what happens if you try to unpickle a file by opening it in read mode (using _open(file\_name,_ _ **'r'** __)_) instead of binary read mode (using _open(file\_name,_ _ **'rb'**__)_). An error will occur, and the program will crash. Errors like this can be handled using structured error handling.

### What is structured error handling?

Structured error handling allows you to control what happens to your code if an error occurs by using a try-except block. This is what a try-except block looks like:

![](RackMultipart20230302-1-jwzwc0_html_ca300c3ecfd8dd53.png)

Basically, this tells the program to try and run the first code. If that code causes an error, then run the second code instead. In the case of trying to read a pickled file we can handle the error like this:

![](RackMultipart20230302-1-jwzwc0_html_5d9ca3d572347bc4.png)

This will output the following:

![](RackMultipart20230302-1-jwzwc0_html_87e5c5c31a94d5ca.png)

## Conclusion

With this assignment I have explained and demonstrated Pickling and Structured Error Handling. I've combined code used in the examples above into one script to demonstrate how pickling and structured error handling can be used in tandem. First the code pickles the data and writes it to a file. Then it tries to read the file as a regular file and when that errors, it reads the file as a binary file. Finally, it unpickles the file and formats it in a way that is easy to read. See the output below.

 ![](RackMultipart20230302-1-jwzwc0_html_1e0f43c79e685231.png)

![](RackMultipart20230302-1-jwzwc0_html_b50c90731b41a271.png)
