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
question 5:
Longest Palindromic substring
Write a function that given a string returns the longest palindromic substring.
(string[i:j] returns substring from index i to j-1)

------------------------------------------------------------------------------------------------------------------------------
question 6:
Longest Substring Without Duplication
Write a function that given a string returns the Longest Substring Without Duplication.
(dictionary initialization)

------------------------------------------------------------------------------------------------------------------------------
question 7:
Underscorify substring

Write a function that takes in two strings: a main string and a potential substring of a main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores. If two instance of the substring in the main string overlap each other or sit side by side, the underscores relevent to these two substrings should only appear on the far left of the substring and far right of the substring. If the main string does not contain the other string at all, return the main string intact.

sample input: "testthis is a testtest to see if testestest it works", "test"
sample output:"_test_this is a _testtest_ to see if _testestest_ it works"
(googled splitting a substring and not operator)

------------------------------------------------------------------------------------------------------------------------------
question 8:
pattern Matcher

you are given two non-empty strings. The first one is a pattern consisting of only "x"s and/or "y"s; The other is a normal string of alpganumeric characters. Write a function that checks whether or not the normal string matches the pattern. A string SO is said to match a pattern if replacing all "x"s in the pattern with some string S1 and replacing all "y"s in the pattern with some string S2 yeilds the same string SO. If the input string does not match the input pattern,return an empty array; otherwise, return an array holding the representations of "x"s or "y"s, the respective letter should be represented by an empty string in the final array that you return. Assume that there will never be more than one pair of string S1 and S2 that appropriately represents "x" and "y" in the input string.

Sample input:"xxyxxy","gogopowerrangersgogopowerrangers"
Sample output:["go","powerrangers"]

------------------------------------------------------------------------------------------------------------------------------
