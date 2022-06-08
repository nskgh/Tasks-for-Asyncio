# Tasks-for-Asyncio: 
Programs for the Tasks
For Task 1, I replaced the function sleep_coro() with the function run() to display the contents of the webpages in the Python Shell. 
For Task 2, there were 2 parts.
The first part required me to download the JSON files from the xkcd website in a synchronous manner(which is time consuming). JSON commands were used for the same(for decoding and writing to the files). The total time taken for all the contents to be downloaded and the files written was 81.02 seconds. 
For the second part, JSON files were downloaded using asyncio asynchronously.
This method was way faster, but aiohttphas an inbuilt JSON decoder which decodes the JSON files to 'byte' type of file.
So, in order for the JSON files to be stroed in the files in correct format, I used a byte to dict convertror to convert the JSON files to the appropriate dict type.
As expected, this method was really faster than the previous method and took only about 2.46 seconds. 
There was one thing to note that the order in which the contents are downloaded and written can be clearly seen in my program, and we can see the efficiency of the async module in trying to execute the tasks in action in the python shell. 
