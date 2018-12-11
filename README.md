# Interview_prep
Contains the actual questions of all the code.

question 1:
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
(Time took to solve: 21 mins, did i google any syntax: yes) 

------------------------------------------------------------------------------------------------------------------------------

Question 2 :
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
(Time took to solve: 10 mins, did i google any syntax: no) 


------------------------------------------------------------------------------------------------------------------------------

Question 3 :
This question was asked in Twilio first coding round.
Given the name of the text file which contains the log information. print the host name and occurances of the hosts in a new text file which is named as "record_"+filename.
The input file is uploaded in the GIT which is named as hosts_access_log_00.txt
The output file in the git is named as record_hosts_access_log_00.txt


------------------------------------------------------------------------------------------------------------------------------

Question 4:
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

(Saw the solution and then coded)


------------------------------------------------------------------------------------------------------------------------------

