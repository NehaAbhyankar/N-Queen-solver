Following files are required to run the program on a MacOS/Linux based system:

1. minisat.py: This file contains the code that is generating the CNF encodings. The generated encodings will be saved in nqueen.cnf file as well as printed on the terminal.

2. The generated nqueen.cnf file will be fed into minisat solver to solve the satisfiablity problem and the output will be saved in a new file called nqueen_result.txt

3. figure.py can be run to visualize the satisfiability solution generated by nqueen_result.txt into a board. 


Note: The path of the file may vary based on user directory. They need to be changed while running commands on terminal as well as inside minisat.py and figure.py
For minisat.py, the two path directories are under Input heading few lines from the top.


Following commands on the linux terminal can be run to solve the N-queen problem:

1. python ~/minisat.py
2. minisat ~/nqueen.cnf ~/nqueen_result.txt
3. cat ~/nqueen_result.txt
4. python ~/figure.py
5. cat ~/result.txt

MiniSat is generating Satisfiability results correctly for all the values of N. The screenshots are attached in screenshots.pdf file.
