<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 29/04/2023 23:40:33</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235311248-62025b6e-cb21-450c-ae9b-c60cc64d8c07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Orders table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235311534-b4373315-f328-43d4-8044-8fc80b24627e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of OrderItems table with validate data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235311655-0b1e0541-aa2c-480d-8d0a-cc97feb68fd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the purchase form UI from Heroku<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235311897-47480743-773c-417a-9c12-4e0c53d752f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the items pending purchase from Heroku<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235312286-75d7c6ba-6843-494b-854b-9dee9101343b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1 screenshot Process validations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235312425-7b2145e5-7508-4e36-b640-74faf654d703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>2 screenshot Process validations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235312437-d02e0431-3fe8-4a58-95d6-b0c4055e0e59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 screenshot Process validations code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235312720-7bec348b-891b-40e6-a9ab-cd2c67f611e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unavailable stock message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235313390-26c33e91-73a1-4d6c-8fde-bdcd0959e261.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show invalid &quot;Money Received&quot; message and Price difference message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <div>This is a Flask application endpoint that allows users to purchase items from<br>a store. The process involves several steps, as described below:</div><div><ol><li>The user submits a<br>POST request to the '/purchase' endpoint, which requires the user to be logged<br>in.</li><li>The function retrieves the user's cart, which contains all the items the user<br>intends to purchase, and verifies that there are no errors.</li><li>If there are no<br>errors, the function calculates the total cost of the purchase and checks if<br>the user can afford it.</li><li>If the user can afford the purchase, the function<br>creates an order data object containing the order ID, payment method, total cost,<br>and user information.</li><li>The function records the order history by copying the items in<br>the user's cart to the order history table.</li><li>The function updates the stock of<br>the items in the store based on the items the user has purchased.</li><li>If<br>everything has been successful so far, the function deletes the items from the<br>user's cart and commits the transaction.</li><li>Finally, the function displays an order summary page<br>to the user.</li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/25">https://github.com/vamsirangu999/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone3-prod.herokuapp.com">https://vr76-milestone3-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235313981-9a1d63ce-506b-4ed4-b4e2-5531dc988d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the order details from the purchase form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <div>This is a Flask application endpoint that allows users to purchase items from<br>a store. The process involves several steps, as described below:</div><div><ol><li>The user submits a<br>POST request to the '/purchase' endpoint, which requires the user to be logged<br>in.</li><li>The function retrieves the user's cart, which contains all the items the user<br>intends to purchase, and verifies that there are no errors.</li><li>If there are no<br>errors, the function calculates the total cost of the purchase and checks if<br>the user can afford it.</li><li>If the user can afford the purchase, the function<br>creates an order data object containing the order ID, payment method, total cost,<br>and user information.</li><li>The function records the order history by copying the items in<br>the user's cart to the order history table.</li><li>The function updates the stock of<br>the items in the store based on the items the user has purchased.</li><li>If<br>everything has been successful so far, the function deletes the items from the<br>user's cart and commits the transaction.</li><li>Finally, the function displays an order summary page<br>to the user.</li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/25">https://github.com/vamsirangu999/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone3-prod.herokuapp.com">https://vr76-milestone3-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235315619-8fb5f2a2-ce6f-4ff3-a7eb-841ae6be965a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing purchase history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235315685-123383d1-53ad-4c99-9a52-2ea6e32a0f70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <div>This code defines a Flask route to display the details of an order.<br>When a user or an admin clicks on an order in the purchase<br>history, they will be redirected to this page with the order ID as<br>a parameter in the URL.</div><div>The code first checks if the current user is<br>an admin or a regular user. Then, it retrieves the order ID from<br>the URL parameter using request.args.get(). If the ID is not provided, it flashes<br>an error message and redirects the user to the purchase history page.</div><div>Next, the<br>code performs a database query to retrieve the details of the order. It<br>selects the product name, unit price, quantity, and subtotal for all order items<br>with the given order ID. The query also joins the IS601_S_Products and IS601_S_Orders<br>tables to retrieve additional information about the product and order.</div><div>If the query is<br>successful and returns rows, the code computes the total cost of the order<br>by summing up the subtotals of all order items. Finally, it renders the<br>order.html template with the list of order items and the total cost.</div><div>If the<br>query fails, the code flashes an error message and redirects the user to<br>the purchase history page.</div><div>In summary, this code retrieves the details of an order<br>and displays them to the user or admin who clicks on the order<br>in the purchase history.</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/25">https://github.com/vamsirangu999/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone3-prod.herokuapp.com">https://vr76-milestone3-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235316157-6ed609a8-f382-439b-ac3b-7c696758977e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing purchase history from multiple users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235317285-308a748b-e5b8-4c6d-b8bd-76c9ebec5488.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing full details of a purchase <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <div>When an admin user clicks on an order from the purchase list, the<br>function is triggered, and the order details for that particular order are retrieved<br>from the database using a SELECT query. The order details retrieved include the<br>product name, unit price, quantity, shipping address, and subtotal.</div><div>The query used to retrieve<br>the order details uses the order ID passed in as an argument in<br>the request, which ensures that the user can only view their own orders.</div><div>Once<br>the order details are retrieved, the function calculates the total cost of the<br>order by summing up the subtotal for each item in the order. Finally,<br>the function renders the order details on an HTML template named "order.html", which<br>is returned to the user.</div><div>This differs from the user's purchase history feature because<br>the user's purchase history feature would typically show a list of all orders<br>that the user has placed in the past. In contrast, this function is<br>responsible for displaying the details of a specific order that the admin user<br>has selected</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/25">https://github.com/vamsirangu999/IS601-004/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone3-prod.herokuapp.com">https://vr76-milestone3-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/235317423-e66ad34e-f6fa-4db7-a983-2132246f4e43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart page showing the button to place an order<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Updating the database is a critical aspect of any web application, and it<br>is important to ensure that only authenticated and authorized users can modify data.<br>Flask provides a session and authentication system that allows developers to authenticate users<br>and limit their access to certain parts of the application.</div><div>To ensure that only<br>authenticated users can access the database update feature, we can create an authentication<br>system using Flask-Login. This package allows us to easily manage user authentication and<br>session management. We can define user roles and assign permissions based on those<br>roles.</div><div>Once the user is authenticated, we can use Flask session to store user-specific<br>data, such as the user ID or username. This data can be used<br>to ensure that users can only access their own data in the database.<br>For example, when updating user profile information, the user ID stored in the<br>session can be used to update only the user's own data in the<br>database.</div><div>In addition, we can use Jinja templates to render dynamic content within the<br>application. However, it is important to be mindful of the data being displayed<br>in the templates, as sensitive information should be protected from unauthorized access. We<br>can use Flask's role-based access control to ensure that sensitive information is only<br>displayed to users with appropriate access.</div><div>Overall, implementing session management and authentication in Flask<br>is crucial for ensuring that users can only access appropriate parts of the<br>application and that sensitive data is protected from unauthorized access. By using role-based<br>access control and storing user-specific data in the session, developers can create secure<br>and reliable web applications.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-shop-project/grade/vr76" target="_blank">Grading</a></td></tr></table>