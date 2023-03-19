<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 19/03/2023 13:04:34</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158399-ab44f564-c510-4a5d-93cc-468a9f7f02c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of calculate_cost function which adds all costs by iterating over inprogress_burger array<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <div>The code shown above is a Python method called calculate_cost that calculates the<br>total cost of the inprogress_burger using a for-loop.</div><div>First, the method initializes the totalcost<br>variable to 0.</div><div>Then, it iterates over each item in the inprogress_burger list and<br>adds its cost to totalcost. The cost of each item is accessed through<br>the item.cost attribute.</div><div>Finally, the method returns the total cost formatted as a string<br>with commas separating the thousands and a dollar sign at the beginning of<br>the string. The format() method is used to achieve this currency formatting.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158833-0a472e5c-b72b-4ae7-bf09-165ee7cf0221.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of OutOfStockException Exception raised when the item selected by the user is<br>out of stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158851-d24ee9a0-9686-4fa7-af30-1dc7d2bb1ca9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of NeedsCleaningException Exception raised when the machine needs cleaning the user is<br>prompted to type &quot;clean&quot; to trigger the clean_machine()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158857-e6a37483-6457-40b5-aef9-940253ac8321.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of InvalidChoiceException Exception raised when the user selects an invalid option in<br>a particular stage/category<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158863-c84a60b4-6af8-4f1b-a109-13fee945b6bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of ExceededRemainingChoicesException Exception raised when the user exceeds the remaining choices in<br>a particular stage/category<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226158882-8c773246-4ea9-4e58-82ad-09edae35eba1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of InvalidPaymentException Exception raised when the user enters an invalid payment amount<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>OutOfStockException: This exception is raised when the item selected by the user is<br>out of stock. In such cases, an appropriate message is displayed to the<br>user informing them of the stage/category where the item was out of stock<br>and prompting them to select another option.</div><div><br></div><div>NeedsCleaningException: This exception is raised when the<br>machine needs cleaning. In such cases, the user is prompted to type "clean"<br>to trigger the clean_machine() method. Any other input is ignored. A message is<br>then displayed informing the user whether or not the machine was cleaned.</div><div><br></div><div>InvalidChoiceException: This<br>exception is raised when the user selects an invalid option in a particular<br>stage/category. In such cases, an appropriate message is displayed to the user informing<br>them of the stage/category where the invalid choice was made.</div><div><br></div><div>ExceededRemainingChoicesException: This exception is<br>raised when the user exceeds the remaining choices in a particular stage/category. In<br>such cases, an appropriate message is displayed to the user informing them of<br>the stage/category where the limit was exceeded, and the program moves to the<br>next stage/category.</div><div><br></div><div>InvalidPaymentException: This exception is raised when the user enters an invalid payment<br>amount. In such cases, an appropriate message is displayed to the user informing<br>them to correct the payment amount.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159729-2a46cc4d-6d0b-4227-bee3-54c67a9bf134.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly raises an InvalidStageException when<br>a patty is added before a bun<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159747-906b496a-8ab4-44f8-a114-8226d588c85e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly raises an OutOfStockException when<br>the number of burgers ordered exceeds the available buns<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159766-e60d2ca3-ac00-48d3-9f2f-a08e817be228.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly raises an OutOfStockException when<br>the number of toppings ordered exceeds the available toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159786-67b4cb2f-1e5f-4144-8b13-3c75e4b94c46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly raises an ExceededRemainingChoicesException when<br>more than four patties are added to a burger<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159798-803425c9-0399-4a9b-9f2b-e8467967445a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly raises an ExceededRemainingChoicesException when<br>more than four toppings are added to a burger<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159816-b5c9b51f-6963-44bb-b3ee-a755683a458a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly calculates the cost of<br>a burger with different bun, patty, and topping choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159839-8aca5057-b394-4b0b-a100-e4fc9bd4cd0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly updates its total sales<br>when multiple burgers are ordered and paid for<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226159858-bfb97fea-481a-447e-bc57-6897b6d400db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Pytest Test1 checks if the machine correctly updates its total number<br>of burgers sold when multiple burgers are ordered and paid for<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226160060-c2b567bc-f828-4470-8ec2-097c476fe1ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of All Pytest Tests 1-8 Passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1:</div><div>This test checks if the machine correctly raises an InvalidStageException when a<br>patty is added before a bun. The test creates a new instance of<br>the BurgerMachine, resets it to its initial state, adds a patty before a<br>bun, and then asserts that the machine raises an InvalidStageException.</div><div><br></div><div>Test 2:</div><div>This test checks<br>if the machine correctly raises an OutOfStockException when the number of burgers ordered<br>exceeds the available buns. The test creates a new instance of the BurgerMachine,<br>resets it to its initial state, and then attempts to order four burgers,<br>which requires eight buns in total. Since the machine only starts with four<br>buns, it should raise an OutOfStockException. The test asserts that the machine raises<br>this exception.</div><div><br></div><div>Test 3:</div><div>This test checks if the machine correctly raises an OutOfStockException when<br>the number of toppings ordered exceeds the available toppings. The test creates a<br>new instance of the BurgerMachine, resets it to its initial state, and then<br>attempts to order four burgers, each with four servings of cheese. Since the<br>machine only starts with twelve servings of cheese, it should raise an OutOfStockException.<br>The test asserts that the machine raises this exception.</div><div><br></div><div>Test 4:</div><div>This test checks if<br>the machine correctly raises an ExceededRemainingChoicesException when more than four patties are added<br>to a burger. The test creates a new instance of the BurgerMachine, resets<br>it to its initial state, and then attempts to add five patties to<br>a burger. Since each burger can only have up to four patties, the<br>machine should raise an ExceededRemainingChoicesException. The test asserts that the machine raises this<br>exception.</div><div><br></div><div>Test 5:</div><div>This test checks if the machine correctly raises an ExceededRemainingChoicesException when more<br>than four toppings are added to a burger. The test creates a new<br>instance of the BurgerMachine, resets it to its initial state, and then attempts<br>to add five servings of pickles to a burger. Since each burger can<br>only have up to four toppings, the machine should raise an ExceededRemainingChoicesException. The<br>test asserts that the machine raises this exception.</div><div><br></div><div>Test 6:</div><div>This test checks if the<br>machine correctly calculates the cost of a burger with different bun, patty, and<br>topping choices. The test creates a new instance of the BurgerMachine, resets it<br>to its initial state, and then adds different combinations of bun, patty, and<br>toppings to the burger. For each combination, the test asserts that the machine<br>correctly calculates the cost of the burger.</div><div><br></div><div>Test 7:</div><div>This test checks if the machine<br>correctly updates its total sales when multiple burgers are ordered and paid for.<br>The test creates a new instance of the BurgerMachine, adds three different burgers<br>to the order, pays for each burger, and then asserts that the machine's<br>total sales are equal to the sum of the prices of the three<br>burgers.</div><div><br></div><div>Test 8:</div><div>This test checks if the machine correctly updates its total number of<br>burgers sold when multiple burgers are ordered and paid for. The test creates<br>a new instance of the BurgerMachine, adds two different burgers to the order,<br>pays for each burger, and then asserts that the machine's total number of<br>burgers sold is equal to the number of burgers ordered.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/13">https://github.com/vamsirangu999/IS601-004/pull/13</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <div>Issues/Difficulties:</div><div><br></div><div>One potential issue is that the tests may not be comprehensive enough to<br>cover all possible edge cases, which may lead to undetected bugs or issues.</div><div>Another<br>issue could be that the tests rely on specific input data, which may<br>not be representative of all possible use cases for the system.</div><div>Debugging errors can<br>also be difficult if the tests are not written in a clear and<br>concise manner.</div><div>Learnings:</div><div><br></div><div>Writing tests can help ensure the correctness of the system and identify<br>issues early on in the development process.</div><div>It's important to write comprehensive tests that<br>cover a wide range of possible input and output scenarios.</div><div>Test-driven development can help<br>improve the overall quality of the system and reduce the number of bugs<br>and issues.</div><div>Tests should be written in a clear and organized manner to facilitate<br>debugging and improve readability.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226160419-20596942-c602-4ed4-926f-8bb2fb59bed4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Burger 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226160442-4cdc9913-3fbf-42df-a545-a0f900e36090.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Burger 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/226160453-bc20e5f5-5062-4cce-b522-43c56dcf2cbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Burger 3<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/vr76" target="_blank">Grading</a></td></tr></table>