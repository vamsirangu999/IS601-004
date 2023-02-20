<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:08:12 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220145278-c980697f-32ac-44ce-8487-9c3638730ca7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220145421-f67cdb61-0e6b-4d39-9b1d-f5778d63eaee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220145473-5f3265e2-a2b1-494c-9a1a-18c42a3c9ba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rejection screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>Solution:</div><div><ol><li>updated lastActivity with the current datetime using strftime function from datetime.now()</li><li>assigned name, description<br>and due date values to task Dict</li><li>for due date used str_to_datetime function for<br>validating the format</li><li>appended the new task to tasks List()</li><li>used try-except for displaying message<br>of confirmation or rejection</li><li>save() function remains same it the end</li><li>ucid and implemented date<br>has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220146979-a40cf600-6671-4503-9012-6187a167df04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>process_update( ) function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>Solution:</div><div><ol><li>fetched task from tasks list with given index value</li><li>used try-except for displaying message<br>for index out of bounds scenarios</li><li>used print statements for showing existing value of<br>each property where the TODOs are marked</li><li>ucid and implemented date has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220147773-dd21913c-6748-4b2d-9f5a-c07522812d56.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220147933-141c86a0-d003-4b91-8781-5be282274167.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220147971-de30031e-fd28-44f0-b365-961903218d96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rejection screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>solution:</div><div><ol><li>fetched task from tasks list with given index value</li><li>used try-except for displaying message<br>for index out of bounds scenarios</li><li>Updated name, description and due only if its<br>provided</li><li>updated lastActivity with the current datetime using strftime function from datetime.now()</li><li>used a flag<br>to check and print message</li><li>save() function remains same it the end</li><li>ucid and implemented<br>date has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220148433-7f368a4d-0a77-43ad-9054-d17496e54393.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>mark_done() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220148573-702ea9ed-9deb-4eaf-a5c5-77d7a7112023.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220148651-1dc81305-8092-4ac2-a42b-41a03d76fd82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rejection screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>solution:<div><div><ol><li>fetched task from tasks list with given index value</li><li>used try-except for displaying message<br>for index out of bounds scenarios</li><li>record the current datetime as the value if<br>done is False</li><li>Printed Message if done is not False</li><li>save() function remains same it<br>the end</li><li>ucid and implemented date has been added</li></ol></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220149125-7375df0c-98e9-4256-a376-4ad6c22ffa06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220149215-c4c38559-3ee6-48dc-9085-172ca9955e90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220149313-e98d6733-561f-41df-8f09-cb981f884c2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rejection screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220151200-b58ba009-4d57-4987-ae92-9adcf86390bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_tasks() output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220151499-0d99da44-621c-4753-8094-f7d99e07bbfb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220151627-a7f01748-6362-4312-8f19-2585bdf80bae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220151707-c230dee5-a3fb-4445-befc-0396e5cd87d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>reject screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>solution:<div><div><ol><li>delete/remove task from tasks list with given index value and del</li><li>Displayed message If<br>it is Successful</li><li>used try-except for displaying message for index out of bounds scenarios</li><li>save()<br>function remains same it the end</li><li>ucid and implemented date has been added</li></ol></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152231-3b68be29-97cb-4551-8f89-1f1da02a62db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_incomplete_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152342-79931f57-be20-42f8-958d-f68ff7da8ad5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152381-ef028851-6008-4f76-b424-48d63bfacf0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>reject screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>solution:</div><div><ol><li>iterating through tasks list&nbsp; and appending incomplete tasks to list</li><li>passing _tasks to list_tasks()<br>only if _tasks is not empty</li><li>ucid and implemented date has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152653-e27dc8f6-5645-4f6c-af5b-048564496918.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_overdue_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152754-900f7d43-325c-45a1-b521-c715548948de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220152811-549eaf15-18d8-4586-865e-0b72cf7932fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>rejetc screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>solution:</div><div><ol><li>iterating through tasks list&nbsp; and appending incomplete and overdue tasks</li><li>passing _tasks to list_tasks()<br>only if _tasks is not empty</li><li>ucid and implemented date has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220153020-4d76b756-4440-4c1d-a8e1-2760753aa096.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>get_time_remaining() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220153111-5a259224-23d8-4dbd-a4b8-69a3e80acfd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220153162-49717115-2838-426b-ae6e-9097380e6fdc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>reject screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div>solution:</div><div><ol><li>fetched task from tasks list with given index value</li><li>used try-except for displaying message<br>for index out of bounds scenarios</li><li>Difference between current date and due date</li><li>Displayed Remaining<br>time if current date is lesser than the due date</li><li>Displayed Overdue if current<br>date is greater than the due date</li><li>ucid and implemented date has been added</li></ol></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220153445-f2ad4fef-2e66-4d21-893f-347de182d9d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>program output generated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/220154054-8145d163-7ad9-4cf3-96b7-db90a0f74bd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>saved JSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div>Issues:</div><div>Converting datetime to no of days, hrs, mins</div><div><br></div><div>Solution:</div><div>By using a delta of 2<br>datetimes</div><div>days = delta.days</div><div>hours, remainder = divmod(delta.seconds, 3600)</div><div>minutes, seconds = divmod(remainder, 60)</div><div>seconds += delta.microseconds<br>/ 1e6</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/5">https://github.com/vamsirangu999/IS601-004/pull/5</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/vr76" target="_blank">Grading</a></td></tr></table>