This is a design for a Turing Machine (TM) that will compute Huffman Codes.  

The completed Turing Machine is in the file 'huffman_encoding.txt'.  
The code uses the syntax of Anthony Morphett's Turing Machine Simulator, and can be ran here:  

On top of general tape management, there are 4 main components to this TM:  
  Processing binary values 
  Finding the two smallest characters  
  Merging the two smallest characters  
  Unmerging the characters to compute the prefix code  

For many of these components, it was required to move sets of characters around the tape. It made sense to create general move  
circuits that performed a set of instructions and then moved to a control element which redirected the program. By changing the   
control character, these circuits could be called again and again similar to functions.  
There were 5 move circuits:  
>  move  
>  find  
  copy  
  moveToFront  
  writeLeft  
  
These circuits had a lot of repetition since identical states were needed for each letter in the alphabet. alphabet dependent states  
were written in python, see create_circuits.py. Here is the current alphabet:  
a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9  
  
While the format of the tape changed during each algorithmic component, in general # was the start symbol, $ was the end symbol, and the   
character right before the end symbol was the control character. @ and % were used to wrap the text to be moved to the end of the tape   
in the move circuits. ~ and & were used to denote the smallest and second smallest characters respectively. The frequencies were r  
represented by sets of o's, and the - character was used to separate the merged characters from their frequencies.  

\#   x-ooo     @ooo% z-oooo c$y-oo  
Example of what the tape would look like when moving the y character and its frequency representation to the end of the tape. The c represents a control symbol.  
  
This project was inspired by CS 4820, a Cornell class which gives an introduction to both Turing Machines and the Huffman Encoding Algorithm.  
