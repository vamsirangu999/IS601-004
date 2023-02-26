<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 26/02/2023 15:56:00</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404499-cd9e11af-abff-4fb9-a246-af98a6958e27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid Addition Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404534-fc6beb2c-9a27-4216-9e16-294509673c2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid Subtraction Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404571-bdca9f9a-acf9-45d1-861e-7ed679fa1d63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid Multiplication Function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404586-f8d834e4-a87b-42cb-8083-ea399772383a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid division Function<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404639-bcf1bc8c-ec8f-42db-8de0-80799e5f8687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-add-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404671-bd4b0246-36e6-42d2-b4c2-9a8f6b93eb02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-add-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404699-48c51225-0ea4-43de-a4a4-0fa755e53c36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-sub-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404716-cf12cbbe-74c9-4db6-8cbf-c2de730d8473.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-sub-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404760-f0256eaa-c4a3-4c30-91fd-f4b88a969d8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404773-d8ae37f5-723d-4a5e-8202-cb0e6ad9f920.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404785-8e6a1fd1-7146-46db-9246-1fa170033b2f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404798-bd32fd3a-607d-41b8-a439-5b3edc7b1c9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number Test Case<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/221404837-24acdf72-4d64-49e8-8bf6-9d4d37e466dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test case output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <div>Pytest is a testing framework for Python that allows developers to write tests<br>in a more concise and readable way compared to the built-in unittest module.<br>It provides powerful features such as fixtures, parameterization, and plugins, which can help<br>simplify the testing process and make it more efficient.</div><div><br></div><div>Some of the key concepts<br>in pytest include:</div><div><ul><li>Test functions: These are regular Python functions that use assert statements<br>to check the expected behavior of code.</li><li>Fixtures: These are functions that provide a<br>set of preconditions or resources that can be used by test functions. Fixtures<br>can be defined at different scopes, such as module, class, or function.</li><li>Assertions: These<br>are statements that verify whether an expected result is true or false. Pytest<br>provides a wide range of assertion helpers that make it easy to write<br>expressive and informative tests.</li><li>Markers: These are labels that can be applied to test<br>functions or fixtures to specify their behavior or categorize them for selective test<br>runs.</li></ul></div><div>Overall, pytest is a flexible and powerful testing framework that can be used<br>for a variety of testing scenarios, from unit tests to functional and integration<br>tests. Its simple and intuitive syntax makes it easy to write and maintain<br>tests, while its advanced features provide the flexibility and extensibility needed for complex<br>testing scenarios.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases are a set of instructions or scenarios that are created to<br>verify the correctness and accuracy of a software program or a specific feature<br>of the program. In the context of the simple calculator program, test cases<br>are used to check if the calculator functions as intended, and if it<br>can handle various scenarios or inputs in a correct and expected manner.<div><br><div>While working<br>on this assignment, I learned that test cases are crucial in software development,<br>as they help catch bugs and errors before the program is released to<br>the public. Test cases can also be used to test edge cases or<br>boundary conditions, which are scenarios where the input values are at the limits<br>of what the program can handle.</div><div><br></div><div>Furthermore, I learned that writing test cases can<br>help developers understand the requirements of a program better, and can help them<br>design a better program architecture. Test cases can also serve as documentation for<br>the program, as they describe the various scenarios that the program is expected<br>to handle.</div><div><br><div>In conclusion, test cases are an essential part of software development, and<br>creating them is an important skill for developers. They help ensure that the<br>program functions as intended, and that it can handle various scenarios and inputs<br>in a correct and expected manner.<br></div></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/7">https://github.com/vamsirangu999/IS601-004/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/vr76" target="_blank">Grading</a></td></tr></table>