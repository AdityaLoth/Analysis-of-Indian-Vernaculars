# Analysis-of-Indian-Vernaculars

######Installing Dependencies########

For the project to work you will need Python3 installed in your system along with Numpy, Pandas and Openpyxl. Open the terminal and run these commands one by one

sudo apt-get install python3

pip install numpy

pip install pandas

pip install openpyxl

############ Usage ##################

For each question I have created separate shell script which run the python files for that question. All the scripts can be run by executing 'assign2.sh' file. Open the terminal in the extracted folder and run the following command.

bash assign2.sh
 
It took about 2 minutes for my system to execute all the files and generate output.

############# Working #################

The zip file contains a dataset folder, individual shell scripts for each question and python code for each question. 

**QUESTION 1 (q1.py, percent-india.sh)
The census data and C19 file are used.

**QUESTION 2 (q2.py, gender-india.sh)
The census data and C19 file are used. I performed Z-test to calculate p values. First the percentage of mono,ni and tri lingual males and females is calculated.Then I calculated differnce in percentage of males and females for each group. Then calculated z score and then used scipy.stats library to calculate p values. The p values less then 0.05 states that the percentages are significantly different.

**QUESTION 3 (q3.py, geography-india.sh)
Similar files and methods were used as above question. Instead of males/females the differnce was taken for urban/rural population.

**QUESTION 4 (q4.py, 3-to-2-ratio.sh and 2-to-1-ratio.sh)
The census data and C19 file are used. There is two .py files for each part.

**QUESTION 5 (q5.py, age-india.sh)
C18 and C14 files are used. "Age not stated" is not considered as a age group in calculations.

**QUESTION 6 (q6.py, literacy-india.sh)
C08 and C19 files are used.

**QUESTION 7(q7.py,region-india.sh
C17 file for each state has been used.

**QUESTION 8(q8.py, age-gender.sh)
C18 and C14 files are used. "Age not stated" is not considered as a age group in calculations.

**QUESTION 9(q9.py, literacy-gender.sh)
C08 and C19 files are being used.
