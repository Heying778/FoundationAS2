# FoundationAS2

### Hi Abilash, thanks for marking my FS2！💜


#### Here is the bried instruction to guide you the correct file:
#### **Theory Qs** -- Either find the word file called 'AS2_Theory Questions_YH.docx' or see below:
#### **Section 2** : 2.1--Isogram.py; 2.2 --2.2.py
#### **Section 3** : Section3.py
#### **Section 4** : foundation_assessment_ii.sql




<br>




<br/>


#### Theory Qs:
#### 1.1    What does SDLC stand for?	1 mark
#### SDLC : software development lifecycle

####   1.2   What exception is thrown when you divide a number by 0?	1 mark 
#### ZeroDivisionError 


####   1.3   What is the git command that moves code from the local repository to the remote repository? 	1 mark
#### git push

####   1.4   What does NULL represent in a database? 	   1 mark

#### NULL represents the absence of a value or an unknown value.

 ####  1.5   Name 2 responsibilities of the Scrum Master 	2 marks
#### Facilitating the Scrum process and Removing impediments

 ####  1.6   Name 2 debugging methods, and when you would use them.	  4 marks
#### Debug tools: Using IDE to step through the code, set breakpoints, inspect variables, and analyze the program's behavior.
#### Log statements: Adding log statements to the code to track the flow of execution and identify potential issues

  #### 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. 

def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False
	  5 marks
The given function would throw a TypeError when called if the price or cash_given arguments are not numeric values, for example a Boolean or string. By using try-except, the TypeError could be determined and return an error message of “invalid input. Numeric values only.”

   1.8    What is git branching? Explain how it is used in Git. 	  6 marks

Git branching allows the creation of multiple isolated environments to work on different aspects of a project. And we could merge different branches to our main branch by using ‘git merge <branch>’ where <branch> is the branch you want to merge FROM

   1.9  Design a restaurant ordering system. 
           You do not need to write code, but describe a high-level approach: 
a.	Draw a list of key requirements
b.	What are your main considerations and problems?
c.	What components or tools would you potentially use? 	  10 marks
a. Key requirements:

User account login and visual interfaces
Admin managing dashboard for menus, inventory, and user accounts
Ordering system 
Menu display with item details and pricing
Payment processing and transaction management

b. Main considerations and problems:

User-friendly interface for easy navigation and order placement
Ensuring the security of customer information and payment transactions
Managing different user roles and permissions
Handling order cancellations, refunds, and returns

c. Potential components or tools:

Front-end development frameworks like React for building the user interface
Back-end technologies like Node.js for handling user authentication, order processing, and database management
Database management systems like MySQL for storing customer information, menus, and order data
Payment gateways for secure payment processing, such as PayPal
Analytics tools for monitoring user behavior and system performance


