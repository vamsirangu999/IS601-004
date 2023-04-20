<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 20/04/2023 20:50:45</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233370116-b6e6acd8-0070-4422-b2f4-c6edf98edcfd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233370405-6dad93bd-170b-4b0c-ba0a-9ac3203a9306.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords not much validation and invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233371135-b7b56fb4-25e6-49b7-adfa-860c6e376d44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233371379-db1c0f71-9d53-4ef0-9203-74ec603a4017.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233370895-51edc4e6-68fa-4a7e-8f92-f72eb9c9f5cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233371741-3462b007-53e0-4ca5-abb6-a29c7b054866.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid user data in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><div>When this form is submitted, the data entered by the user is sent<br>to the server, which then processes it. In Flask, this is typically done<br>using a view function, which is a Python function that handles a particular<br>URL route. The view function would instantiate an instance of this RegistrationForm class<br>and pass it to a Jinja template to be rendered.</div><div><br></div><div>The validation logic for<br>this form is handled by the validators attached to each field. The DataRequired()<br>validator ensures that the user must enter some data into the field before<br>submitting the form. The Email() validator checks whether the email entered by the<br>user is in a valid email format. The EqualTo() validator checks that the<br>values entered in the password1 and password2 fields match.</div><div><br></div><div>The password is handled using<br>a PasswordField. This field ensures that the password is not visible to the<br>user when they type it in. The EqualTo() validator is used to check<br>that the user has entered the same password in both the password1 and<br>password2 fields.</div><div><br></div><div>The validation logic first checks if the username and email are not<br>already taken in the database by using the User.query.filter_by() method. If the username<br>or email already exists in the database, the user is notified by a<br>flash message and the registration form is re-rendered.</div><div><br></div><div>If the username and email are<br>both unique, the user is created and stored in the database. The set_password<br>method is used to hash and store the password in the user's model.<br>If the user creation is successful, a success flash message is displayed, and<br>the user is redirected to the login page.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233375543-1a0fa2ed-b4fc-4839-a5d2-6e5eac5b53ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233377940-86260db8-19db-4066-a3c7-5a501ec1cd61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233378158-93096cb2-d90d-468a-8afd-89db7486713f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of successful login with flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The login() function handles the submission of the form. First, an instance of<br>the LoginForm class is created. If the form has been submitted and all<br>the validators have passed, the function searches for the user in the database<br>using the entered email or username. If a user is found and the<br>entered password matches the stored password, the user is logged in using login_user(user).<br>The next_route variable is used to redirect the user to the requested page<br>after login, which is passed through the URL as a query parameter called<br>next.</div><div><br></div><div>If the form submission fails, an error message is displayed using the flash<br>function. The render_template function is then used to render the login.html template along<br>with the form.</div><div><br></div><div>The check_password() method of the User model is used to validate<br>the entered password against the stored password. This method hashes the entered password<br>and compares it to the stored hashed password to ensure that they match.<br>This is a secure way of storing passwords in the database.</div><div><br></div><div>The User model<br>is utilised to retrieve the user information from the database. The query.filter() method<br>is used to filter the records based on the entered email or username.<br>The or_() function is used to create an OR condition to retrieve the<br>user information based on either the email or the username. This ensures that<br>the user can log in using either their email or their username.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233380405-a4db922e-1c6e-405a-a835-d17e9246d79b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233380720-5308a34a-8118-4f6b-afd6-e59392f99252.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>the session is used to manage user authentication and to store data for<br>subsequent requests. When a user logs in, their credentials are checked and, if<br>valid, a session is created for the user.</div><div><br></div><div>The session is a dictionary-like object<br>that can store arbitrary data, which is available for subsequent requests from the<br>same client. In Flask, session data is stored in a cookie, which is<br>encrypted and signed to prevent tampering.</div><div><br></div><div>During the login process, the user's identity is<br>stored in the session. This identity can be used to enforce access control<br>throughout the application. For example, in this code snippet, Flask-Principal is used to<br>manage access control based on user roles.</div><div><br></div><div>When the user logs out, the logout_user()<br>function is called, which clears the user's session. In addition, any session keys<br>set by Flask-Principal are removed, and the user's identity is set to anonymous</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233380720-5308a34a-8118-4f6b-afd6-e59392f99252.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the logged out user can&#39;t access a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233383396-f19bf7c5-c17b-48fa-b25d-04f465042a10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing a user without an appropriate role can&#39;t access the role-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233383767-0a49cf20-d7b5-436a-8ab8-b255369754f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Roles table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233383931-23fcf60e-e13e-499d-b17f-489da67b5f14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of UserRoles table with valid data which links user with role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>the session is used to store the user's identity information, which is used<br>by Flask-Principal for authentication and authorization purposes. Flask-Principal is a Flask extension that<br>provides role-based access control (RBAC) and identity management.</div><div><br></div><div>When a user logs out, their<br>identity information is removed from the session using the session.pop() method. This ensures<br>that the user's identity is not retained after they have logged out.</div><div><br></div><div>Unauthorised Page<br>is displayed on&nbsp;<span style="letter-spacing: 0.09996px;">login-protected pages when user try to access those pages</span></div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>the session is used to store the user's identity information, which is used<br>by Flask-Principal for authentication and authorization purposes. Flask-Principal is a Flask extension that<br>provides role-based access control (RBAC) and identity management.</div><div><br></div><div>When a user logs out, their<br>identity information is removed from the session using the session.pop() method. This ensures<br>that the user's identity is not retained after they have logged out.</div><div><br></div><div>Forbidden Page<br>is displayed on&nbsp;<span style="letter-spacing: 0.09996px;">role-protected pages when user try to access those pages</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233370895-51edc4e6-68fa-4a7e-8f92-f72eb9c9f5cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of Navigation and Forms are styled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>Bootstrap includes predefined styles for various elements, including nav and forms. Therefore, the<br>specific styling applied to these elements may depend on the version of Bootstrap<br>being used and how it has been customized</div><div><br></div><div>At a high level, CSS is<br>composed of selectors and rules. Selectors are used to target specific HTML elements,<br>while rules are used to define the styling properties of those elements. CSS<br>can be applied inline to individual HTML elements, or it can be applied<br>externally in a separate CSS file, which is then linked to the HTML<br>document using the &lt;link&gt; element</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233383396-f19bf7c5-c17b-48fa-b25d-04f465042a10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Forbidden page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233375543-1a0fa2ed-b4fc-4839-a5d2-6e5eac5b53ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233380720-5308a34a-8118-4f6b-afd6-e59392f99252.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Unauthorised page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>To handle technical messages and make them more user-friendly, the code uses the<br>Flask "flash" function to display messages to the user on the webpage. The<br>"flash" function is used to display success, warning, and error messages to the<br>user, depending on the outcome of an action. For example, when a new<br>role is successfully created, the code displays a success message to the user.<br>On the other hand, if an error occurs during the deletion of a<br>role, the code displays an error message.</div><div><br></div><div>To further improve the user experience, the<br>code uses templates to render the HTML pages with a user-friendly interface. The<br>HTML pages display forms for creating new roles, assigning roles to users, and<br>unassigning roles from users. The templates also display lists of existing roles and<br>users.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233395224-43eaad14-42e0-4de2-a382-de1386828b48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the User Profile page with Email and Username should prefill<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>When a user accesses the /profile route, a new instance of the ProfileForm<br>class is created and populated with the current user&#39;s data (current_user). If the<br>form is submitted with a POST request and all the fields pass their<br>respective validators, the form data is retrieved from the form object and used<br>to update the current user&#39;s properties in the database<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233398247-0a407903-8d83-4535-b8c9-d179ceb939dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233400302-60c37aa9-fa43-4a0a-bb29-1c420c8dbd88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233402276-48bba3c7-6e6f-4791-aa8d-b11b2b1018db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233401983-4c94977b-2501-4f51-8d30-95e72fb3c58b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233401720-51adb43d-d283-41d3-80bf-e4891430779e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233405010-d848cda0-65f7-46f2-9bf2-8ae609da2c23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the Users table before edit - username=vamshi, email=<a href="mailto:&#x76;&#97;&#x6d;&#x73;&#x68;&#x69;&#x40;&#x67;&#x6d;&#x61;&#105;&#108;&#x6c;&#x2e;&#x63;&#111;&#x6d;">&#x76;&#97;&#x6d;&#x73;&#x68;&#x69;&#x40;&#x67;&#x6d;&#x61;&#105;&#108;&#x6c;&#x2e;&#x63;&#111;&#x6d;</a><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/233405392-125eff07-4934-4717-8bf0-11d19bd9dde5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of the Users table before edit - username=vamshik, email=<a href="mailto:&#118;&#x61;&#x6d;&#115;&#104;&#x69;&#x6b;&#107;&#64;&#103;&#109;&#97;&#x69;&#108;&#108;&#x2e;&#99;&#x6f;&#x6d;">&#118;&#x61;&#x6d;&#115;&#104;&#x69;&#x6b;&#107;&#64;&#103;&#109;&#97;&#x69;&#108;&#108;&#x2e;&#99;&#x6f;&#x6d;</a><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/19">https://github.com/vamsirangu999/IS601-004/pull/19</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>In the profile function, the form.validate_on_submit() method is called to check if the<br>form has been submitted and passes validation. If the form is valid, the<br>current_password, password1, and password2 fields are checked to see if the user wants<br>to update their password. If so, the current_user's password is updated with the<br>new password.</div><div><br></div><div>Finally, the current_user's email and username fields are updated with the data<br>from the form, and the changes are committed to the database. If the<br>update is successful, a success message is flashed and the profile.html template is<br>rendered with the updated ProfileForm object.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>SQLAlchemy, which provides a powerful and flexible Object-Relational Mapping (ORM) layer for working<br>with databases in Flask.</div><div><br></div><div>Sessions, on the other hand, are a way of storing<br>user-specific data on the server-side. In Flask, sessions are implemented using a session<br>object, which provides a dictionary-like interface for storing and retrieving data. This data<br>is stored in a cookie on the client-side, and is encrypted to prevent<br>tampering.</div><div><br></div><div>Here are some key learnings I have gained from working with Flask SQLAlchemy<br>and sessions:</div><div>Flask SQLAlchemy:</div><div><ol><li>ORM - Flask SQLAlchemy provides a powerful and flexible Object-Relational Mapping<br>(ORM) layer for working with databases in Flask. ORM allows developers to work<br>with databases using object-oriented programming concepts, making it easier to manage database operations.</li><li>Models<br>- In Flask SQLAlchemy, models are Python classes that represent database tables. Each<br>model is defined with a set of attributes that correspond to the columns<br>of the table. This allows developers to interact with the database using Python<br>code, rather than writing SQL queries.</li><li>Querying - SQLAlchemy provides a number of different<br>query methods for retrieving data from the database. These include methods like filter(),<br>order_by(), and limit(), which allow developers to write complex queries with ease.</li></ol></div><div>Sessions:</div><div><ol><li>Storing Data<br>- In Flask, the session object is used to store user-specific data on<br>the server-side. Data is stored in a cookie on the client-side, and is<br>encrypted to prevent tampering. This data can be accessed across multiple requests, allowing<br>developers to build more complex web applications.</li><li>Security - Flask sessions are encrypted to<br>prevent tampering, which makes them more secure than using cookies alone. Developers can<br>also configure session timeouts and other security measures to further enhance the security<br>of their web applications.</li><li>Usage - Sessions can be used to store a wide<br>range of data, including user preferences, shopping cart information, and login credentials. They<br>are a powerful tool for building web applications that require user-specific data storage.</li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="http://vr76-milestone1-prod.herokuapp.com/login">http://vr76-milestone1-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone1-deliverable/grade/vr76" target="_blank">Grading</a></td></tr></table>