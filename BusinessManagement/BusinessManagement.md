<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 12/04/2023 21:05:32</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230970306-83fc6580-695d-4c56-aa91-a582cb5f4a15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Visible URL from heroku dev<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230970638-78e9e0eb-709a-4e5d-8048-44396d8f0a91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of url_for references<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230971679-1a723118-ca9f-45d2-af00-dedab8dbf2b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Companies Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230971791-eef956de-80ab-45ca-9500-1b90be7ad05d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employees Table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230973378-45e3d8e3-e60b-46d4-968c-8ba7b38e6686.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reject if not CSV<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230973776-d6796cdb-dcb7-4b3a-9c54-58c368c2c013.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230975839-724a43bd-0d96-4d5f-8c38-76002d1aab6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted employee and company data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230976303-40daec88-e063-47db-adcc-fe5570db74cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230977144-29dfdcc3-89a1-4d43-8d28-9472f7f2d210.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Not a CSV file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230977285-53ea6fa8-5dd8-4dfd-b99c-6416cdece8b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>File not selected<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230977399-0f4d857e-c2f7-46ec-b6ef-12463c60c141.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230971679-1a723118-ca9f-45d2-af00-dedab8dbf2b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Companies Table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/230971791-eef956de-80ab-45ca-9500-1b90be7ad05d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of Employees Table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231465388-a51c87a7-81df-4746-8432-6fed63bed553.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of Add Employee code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231473814-758d8638-8489-4a66-9579-95dcf3639aa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231473970-6c90c38d-f9b6-4b9e-8162-4dd5e82a88d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231474122-b8572a74-8843-40ee-9e91-db878c4ed5c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231474270-632b8678-cdf8-4329-ae76-447ffbe39eda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231474428-36950200-7716-4e66-aac9-b5ca84e7fb3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231475446-f20c3798-0803-499d-aa10-5f18cd1b4d14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Jhon new employee DB record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231476360-8717bd87-4ac5-413e-96cd-6fa111a977d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screen shot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231476548-4666032d-bcd7-4236-854d-3f9aa3dafe3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screen shot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231477549-a7a1b3ac-53e3-4fb0-acab-90d53b83fed9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231477636-a1abba20-9dca-446e-80f9-1de9b0c19d0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231477783-d2b35ce8-501a-4961-be52-c69311fa99ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231477904-a462fa2e-4c0d-4cd5-b8e5-0a661e02ec88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231478069-9dde144e-5fba-4319-9a5b-982696542a6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asc filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231478151-d7ba2b1d-2409-419b-a0e9-fcd7392ed699.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>desc filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231479490-3a4a8c77-727b-4d23-96e8-f1bf7240d054.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231479590-a035f3d9-252a-4389-ba28-6a1ec1bb1447.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231480582-76d4e326-4386-4a2f-beab-56c9d1d26b0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231480746-c40deb20-0626-450d-8850-6641ae07b21b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231480858-c209cb20-2f34-4351-90a3-7304f63485e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231475446-f20c3798-0803-499d-aa10-5f18cd1b4d14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231482117-a764e732-5d0c-4382-8a3a-4a10fa7f101a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231482763-8d5f43b2-4f5b-44b5-80d7-1bf47a758c6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231482939-4b3f2f1d-718f-4c29-b22e-0cb663d22901.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code Screenshot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231485135-91576775-9558-4431-9919-d45b90797635.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231485335-0f1e7c13-b46f-4f57-b397-9e1e4a7f0ad4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231485505-325f472e-2197-4747-89dc-7744431c3583.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231485608-be9dd5b1-fce0-44d2-994a-8c6a6f620d18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231485858-7752aa50-f76b-41ad-ab4b-5718bbcda14b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231486018-e42be418-04b7-4c04-9fd0-eeb22546dc2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231486115-eee0dc5b-09d3-4f7d-8b0d-9c755b2e8988.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231486977-f6fc9d02-5b73-4c7d-a3ce-e6e4ae85d59b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid company data shown previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231487698-c33b8295-6da4-45b6-a319-8912994f021d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231487789-ac624b2c-3a51-42ce-9229-140aed9a4cc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screenshot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231488943-45d1842e-fe04-486a-bb24-1d4e09da46d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231489087-24d4d0b1-1097-40b9-b085-bed5d5082108.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231489216-51a61a15-0615-4496-920c-9b004e49ade0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231489346-054d5af8-e1e8-4235-b24b-be224ddbba93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asc filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231489478-fe5c32a6-1326-4924-a5b3-2a2a1074addf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>desc filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231494034-0ae3a9b9-57d3-4f60-a024-c6e1324bc096.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231494185-08ab42e8-4d4a-4606-9cad-71f21ef49224.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code screenshot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231495770-c3ea6bc3-61b0-4636-b22f-592f89faaf6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231495940-e44a8cc0-b310-46b0-9894-ebbd795724b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231496073-b0916c66-ed92-42ea-b96c-ee81a19d56b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231496317-b3df0d29-450d-4e3f-819c-77c039a4df72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231496433-8a7600a8-b2f9-4a51-8908-28a9de18470d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231497564-e8b07b58-b701-4e6f-8581-a48c271fcca7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of Delete employe<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231498641-141ab2f8-650e-4e17-9a95-ab48f76da31b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231498827-fe3ebc6e-4fa6-46fd-9682-b74d3942a5f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231497442-19985d91-f129-481b-8a66-ee3c97269544.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of Delete company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231499270-0aeacbec-ecf4-44c9-a59d-1eb1d04deb3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231499426-c069f615-245f-4a21-acf3-62e877b8e248.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Delete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/231499980-b3c06225-c544-4ada-a1f5-b7f147610285.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test case shows pass<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>This assignment gave knowledge how a complete web application is developed. Using flask<br>to write backend and frontend with HTML to help users to interact with<br>the application and deploying it over heroku . I learned to securely connect<br>to a DB with python and fetch records &nbsp;and other DB operations. In<br>the beginning it was a bit difficult to understand how to create two<br>VMs over Heroku and connect to DB after creating. These two requirements I<br>felt a bit confused about.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/vr76" target="_blank">Grading</a></td></tr></table>