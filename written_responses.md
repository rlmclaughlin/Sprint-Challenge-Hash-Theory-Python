1. What is a regular expression and how does it work?

   A regular expression (regex) is an extremely powerful tool that is used for matching patterns in strings. The code consist of symbols and characters. When arranged in a specific way, regex will fulfill certain programming duties, based on the objective. It's process is analogous to a finite state machine. Each regex input can be thought of as a new state. The state will only move forward if the circumstance or condition has been reconciled. This process shall continue until the 'accept state' has been reached. To add visual context to this analogy, let us observe a basic string - "python" 

   If we were using regex to scan through this string, the sequence would begin on 'p'. The only way for it to move forward to the letter 'y', is to first have a value of 'true' returned for the 'p'. This process will continue with each character until it has reached the end (accept state)

2. What is an array and how does it work?

   By definition, an array is an 'ordered series or arrangement'. In CS, although true, this is a massive simplification of something slightly more complex. A CS definition is as follows: 'Arrays are a sequence of elements, of the same type, stored in a contiguous block of memory'. This is a little closer to the truth. When creating and working with arrays, it follows a particular process. We begin by determining how big the array needs to be, then retrieve a block of memory that will fit the size of the array, the computer then follows by receiving the memory address of the occupied block, and concludes by writing the values within the array. 

3. What is a hash table and how does it work?
   
   Simply put, a hash table is a data structure that will pair keys to values. It organizes data so that the values for a given key can be retrieved quickly. There are two core components of a hash table: 

   1) It requires an array to store the data
   
   2) It requires a hash function that returns a hash code (integer), depending on the data being stored, and stores it with the index of that hash code.

   The hash table provides easy insertion/deletion due to the fact that these features don't require shifting all of the elements before or after it. The index/hash code also allows for quick access. We also must utilize tools such as chaining with hash tables so that we can avoid situations where elements are overwritten, also known as collisions. 