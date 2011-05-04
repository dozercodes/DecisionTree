README
Stephanie Aligbe
sna2111
05/03/11

Decision Tree Program

File Structure:
readme.txt
main.py
DecisionTree.py
Node.py
Development Environment:
My Decision Tree Learning program was developed in the Eclipse IDE in Python. 

Usage:
My program is compatible with Python2.6 and 2.7, I have not checked compatibility with any other versions. To run my program, issue the command “python main.py” from within this folder. This will output program.py which can then be run with “python program.py” and that will output to the console the target value for each entry of test data. 
To change the training data, change string in the function “open()” in line 8 of main.py to the path of the new training data. To change the target attribute, change the string in line 12 of main.py to the new target attribute. And to change the test data, change the string in the function “open()” at line 31 or main.py to the path of the new test data. If you forget, you can also change it at line 4 of program.py after running main.py. (note, my program is case sensitive)

Output of Test Cases:
Weather.csv:
entry1 = yes
entry2 = yes
entry3 = yes
entry4 = no
can't process input 5
entry5 = ?

Vote.csv:
entry1 = democrat
entry2 = democrat
entry3 = democrat
entry4 = democrat
entry5 = democrat

Soybean.csv:
can't process input 1
entry1 = ?
entry2 = brown-spot
can't process input 3
entry3 = ?
can't process input 4
entry4 = ?
can't process input 5
entry5 = ?

Code Review:
main.py imports and creates the tree using DecisionTree.py. It uses the DecisionTree.py implements the ID3 algorithm and returns the resulting tree as a multi-dimensional dictionary. This dictionary is the fed to program.py which processes the dictionary as a tree. It does so by importing and using Node.py and generates appropriate output based on that tree. 

I feel compelled to say that this was probably my favorite program to write. 
Thank you for allowing me to submit late, Prof. Stolfo and Tianju.

Credits
http://onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=1
This tutorial was used as a guide for developing my ID3 algorithm.
