<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vamsi Naidu Rangu (vr76)</td></tr>
<tr><td> <em>Generated: </em> 24/04/2023 21:35:03</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/vr76" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234034025-abd31af0-c6e7-46e8-b620-34f5f8bea75d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid data filled in add products form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234038795-6d213c7a-558b-4221-94dd-24c9c9173eb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <div>High level steps for how the item goes from UI to DB based<br>on the given code:</div><div><br></div><div><ol><li>The user interacts with the UI by filling out the<br>"ItemForm" and submitting it.<br></li><li>The server (flask) receives the request and invokes the "item"<br>function defined for the "/admin/item" route.<br></li><li>The function initializes an instance of the "ItemForm"<br>and retrieves the item ID from the request query parameters.<br></li><li>The function determines whether<br>the request is for creating a new item or editing an existing one<br>based on the presence of the item ID.<br></li><li>If the form is valid, the<br>function performs either an update or an insert operation on the "IS601_S_Products" table<br>in the database, depending on whether it's a create or an edit.<br></li><li>If the<br>operation is successful, the function adds a flash message to indicate the result.<br></li><li>If<br>the operation fails, the function adds a flash message to indicate the error<br>and logs it.<br></li><li>If the request is for editing an existing item, the function<br>retrieves the item's details from the database and populates the form with them.<br></li><li>If<br>the retrieval is successful, the function populates the form fields with the retrieved<br>values.<br></li><li>If the retrieval fails, the function adds a flash message to indicate the<br>error and logs it.<br></li><li>The function renders the "item.html" template with the populated form<br>and the appropriate "type" variable (either "Edit" or "Create").<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234039400-ae9a75ee-7d43-44b8-8ca5-3a37287af53a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234039843-6f2859f9-1de7-4107-a086-68a1d5f0b829.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page showing both filters and a Low to High sorting applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234040167-6a3aa938-c028-4754-b1d3-cfd30e142251.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page showing both filters and a High to Low sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234041156-87d61d49-3c8f-4dbe-b25f-ded0f69f0e29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the filter/sort logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>This code defines a Flask route named "shop_list" that accepts GET and POST<br>requests to display a list of products from a database table named "IS601_S_Products".<br>The query starts with "SELECT id, name, description, stock, unit_price FROM IS601_S_Products WHERE<br>stock &gt; 0 AND visibility = 1", which selects the id, name, description,<br>stock, and unit_price columns from the table where the stock is greater than<br>zero and visibility is set to 1.</div><div><br></div><div>The filters are applied to the query<br>based on the values of the URL parameters "name", "category", and "price". If<br>the "name" parameter is present, the query is modified to include a "LIKE"<br>clause to match the name column with the provided value. If the "category"<br>parameter is present, the query is modified to include an "AND" clause to<br>match the category column with the provided value. If the "price" parameter is<br>present, the query is modified to include an "ORDER BY" clause to sort<br>the results by unit_price in either ascending or descending order.</div><div><br></div><div>The final query is<br>executed using the DB object's selectAll method, passing the query string and any<br>arguments as parameters. The resulting rows are stored in a list variable named<br>"rows", which is then passed to the shop.html template using the Flask render_template<br>function. The template will display the list of products in an HTML table.<br>If there is an error fetching items from the database, a "danger" flash<br>message will be displayed</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234042214-e206f8f6-c3ff-4a2f-85bd-b861cf5e4802.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Admin List page/results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The function receives GET and POST requests for the "/admin/items" endpoint.<br></li><li>An empty list<br>called "rows" is created.<br></li><li>A try-except block is used to catch any exceptions that<br>may occur when fetching items from the database.<br></li><li>The "DB.selectAll" method is called to<br>execute a SELECT query on the "IS601_S_Products" table in the database. The query<br>selects the "id", "name", "description", "stock", "unit_price", and "visibility" columns of up to<br>25 rows from the table.<br></li><li>If the query is successful and returns rows, the<br>"rows" list is populated with the fetched data.<br></li><li>If an exception occurs, an error<br>message is printed to the console and a flash message is displayed on<br>the rendered HTML page.<br></li><li>Finally, the "items.html" template is rendered with the "rows" data<br>passed as a parameter.<br></li></ol></div><div><br></div><div>"SELECT id, name, description, stock, unit_price, visibility FROM IS601_S_Products LIMIT<br>25"<br></div><div>The "DB.selectAll" method is used to execute the SELECT query on the "IS601_S_Products"<br>table with the specified columns and a LIMIT of 25 rows. The result<br>of this query is stored in the "result" variable<br></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234039400-ae9a75ee-7d43-44b8-8ca5-3a37287af53a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234042746-bbf384f3-bc41-401d-93f0-a6df67337cd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234042214-e206f8f6-c3ff-4a2f-85bd-b861cf5e4802.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234042214-e206f8f6-c3ff-4a2f-85bd-b861cf5e4802.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Editing a Product<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234043487-f9efc956-521c-40de-ae5e-75cc83aa4799.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Editing a Product - Product Name and Stock is changes in 1st<br>record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div><ol><li>The function creates an instance of a form class called ItemForm, which is<br>used to validate and process data submitted in the request.</li><li>The function then retrieves<br>an optional query parameter "id" from the request's arguments using request.args.get(). The value<br>of this parameter is stored in a variable id.</li><li>If the form has been<br>submitted and passes validation using form.validate_on_submit(), the function checks whether the form's id<br>field has a value. If it does, the function updates an existing item<br>in the database using a SQL UPDATE statement. If not, the function creates<br>a new item in the database using a SQL INSERT statement.</li><li>If an id<br>value was provided in the request's arguments, the function retrieves the corresponding item<br>from the database using a SQL SELECT statement and populates the form with<br>the item's data using form.process().</li><li>The function then renders a template called "item.html", passing<br>the form and the type variable as arguments. The type variable is set<br>to "Edit" if an id value was provided in the request's arguments, indicating<br>that the user is editing an existing item, and "Create" otherwise, indicating that<br>the user is creating a new item.</li><li>If there was an error during the<br>update, create or select query, a flash message is created with the error<br>details, and the message is displayed on the template.<br></li></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234044500-fb54aee3-6cd4-44e8-992d-d49308483088.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the button that directs the user to the Product Details Page<br>- by clicking on product name like highlighted in red circle<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234045078-179a5485-e48b-4384-96c7-67db0c6f6a3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the result of the Product Details Page Checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>Flask route for the /itemdetails endpoint. The route supports both GET and POST<br>requests</div><div><br></div><div>Then, the id parameter is extracted from the request arguments using the request.args.get()<br>method. If the id is not present in the request arguments, the form's<br>id data will be used, or None if the id is not set.</div><div><br></div><div>If<br>the id is present, a database query is executed to fetch the item<br>with the corresponding ID. The DB.selectOne() method is used to execute an SQL<br>query and return the result. If the query is successful and returns a<br>row, the row variable is set to the fetched data. If there is<br>an error during the database query, the error is caught and an error<br>message is flashed to the user.</div><div><br></div><div>Finally, the render_template() method is called to render<br>the item_details.html template, passing the row variable as context data. The row variable<br>will contain the data for the item with the specified ID, or None<br>if the ID is not present or the database query failed</div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234045281-0af08a1b-9b26-4323-a44d-dd8016cf6089.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234045853-feaaf550-4095-47f6-b677-08c2e259ad33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the error message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234046661-a5090eb8-eb28-4db8-9bef-a817c91a8ee8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <div>This code represents a Flask route for managing a shopping cart. Here is<br>how the cart works:</div><div><ol><li>When a user logs in, they can add items to<br>their cart by clicking on the "Add" button on the shop page.<br></li><li>When a<br>user clicks the "Add" button, the item is added to the cart in<br>the database. The item's ID, quantity, and unit price are stored along with<br>the user's ID.<br></li><li>If the user clicks the "Add" button again for the same<br>item, the quantity is incremented in the database.<br></li><li>If the user changes the quantity<br>of an item in the cart and clicks the "Update" button, the quantity<br>is updated in the database.<br></li><li>If the user clicks the "Delete" button next to<br>an item, the item is removed from the cart in the database.<br></li><li>If the<br>user clicks the "Clear Cart" button, all items in the cart are removed<br>from the database.<br></li></ol></div><div>The code retrieves the user's cart data from the database and<br>displays it on the "cart.html" template. The template displays the items in the<br>cart with their name, quantity, unit price, and subtotal. The subtotal is calculated<br>by multiplying the quantity by the unit price. The template also displays the<br>total cost of all items in the cart.</div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <div>This code represents a Flask route for managing a shopping cart. Here is<br>how the cart works:</div><div><ol><li>When a user logs in, they can add items to<br>their cart by clicking on the "Add" button on the shop page.<br></li><li>When a<br>user clicks the "Add" button, the item is added to the cart in<br>the database. The item's ID, quantity, and unit price are stored along with<br>the user's ID.<br></li><li>If the user clicks the "Add" button again for the same<br>item, the quantity is incremented in the database.<br></li><li>If the user changes the quantity<br>of an item in the cart and clicks the "Update" button, the quantity<br>is updated in the database.<br></li><li>If the user clicks the "Delete" button next to<br>an item, the item is removed from the cart in the database.<br></li><li>If the<br>user clicks the "Clear Cart" button, all items in the cart are removed<br>from the database.<br></li></ol></div><div>The code retrieves the user's cart data from the database and<br>displays it on the "cart.html" template. The template displays the items in the<br>cart with their name, quantity, unit price, and subtotal. The subtotal is calculated<br>by multiplying the quantity by the unit price. The template also displays the<br>total cost of all items in the cart.</div><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234047393-ec6ea10e-fec8-48ab-b6ac-a99b25f3d21a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Cart View Checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <div>From a code perspective, the cart is being shown by querying the database<br>for all items in the cart for the current user, and then rendering<br>them in the "cart.html" template.</div><div><br></div><div>The database query retrieves the following information for each<br>item in the cart: ID, product ID, product name, desired quantity, and subtotal<br>(which is calculated by multiplying the desired quantity by the unit price). This<br>information is stored in a list of dictionaries, where each dictionary represents an<br>item in the cart.</div><div><br></div><div>The "cart.html" template then iterates through this list of dictionaries<br>and displays each item in a table row. For each item, the template<br>displays the product name, desired quantity, unit price, and subtotal.</div><div><br></div><div>To calculate the total<br>cost of all items in the cart, the template iterates through the list<br>of dictionaries and adds up the subtotal for each item. The resulting total<br>is displayed at the bottom of the cart table.</div><div><br></div><div>Overall, the subtotal and total<br>calculations are performed in the database query and the template, respectively, by retrieving<br>and manipulating the necessary data</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234047393-ec6ea10e-fec8-48ab-b6ac-a99b25f3d21a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before Update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234048031-1105c990-3f61-4f80-ac1c-3e1e0425b85f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Update - Chocolate is update and calculated from 1 to 7 Quantity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234048754-4b212fd6-9666-419f-8d31-43099e654938.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before Update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234049051-8bb6cdc6-6950-4498-aa0e-c9473aa9500b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after Update - Updated quantity to 0 and clicking update button Product will<br>be removed from Cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234049621-f6647c48-54e0-40d8-b969-2c8c6dea0121.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>negative quantity is not allowed in the incremental <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <div><div>verview of how the update process works:</div><div><ol><li>Check if the user is authenticated. If<br>not, redirect them to the shop list page with a warning message.<br></li><li>Check if<br>the delete_all parameter was included in the request. If so, delete all items<br>in the user's cart and redirect them to the cart page.<br></li><li>Extract the item_id<br>and quantity parameters from the request's form data.<br></li><li>If item_id and user_id are not<br>empty, attempt to retrieve the product's unit price and name from the database<br>using the id parameter.<br></li><li>If the retrieved product information is valid, update the cart<br>in the database using an SQL query. If item_id is not empty, the<br>desired quantity and unit price for the corresponding product in the cart will<br>be updated. Otherwise, a new row will be inserted into the cart table<br>with the id, quantity, cost, and user_id parameters. If a duplicate key constraint<br>violation occurs, the desired quantity and unit price for the corresponding product in<br>the cart will be updated instead.<br></li><li>Display a success message to the user using<br>the flash function<br></li></ol></div></div><div><br></div>Regarding the handling of a value of 0 or negative numbers<br>for the quantity parameter, the code checks if quantity is greater than 0<br>before attempting to update the cart. If quantity is 0 or negative, the<br>else block at the end of the code snippet will be executed, which<br>doesn't do anything currently. It's up to the developer to decide how they<br>want to handle this case<br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234050349-f9362c94-ed9f-4e6c-8c4b-1383b87bf5dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before Deletion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234050523-aaa28044-70cd-4fd9-b148-d4e655c00335.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting single item by clicking on &quot;X&quot; button in actions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234050961-a127fe84-323a-493e-b636-28707cd43409.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Clearing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113048/234051154-f4cc98ba-028b-4cd0-9f4e-7a1137b06520.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Clearing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div>The code is for a shopping cart in a web application. There are<br>two delete processes that can be triggered:</div><div><ol><li>Deleting a single item from the cart:</li><ol><li>When<br>the user enters a quantity of 0 for a product, it is assumed<br>that they want to delete that item from the cart.</li><li>The DELETE FROM IS601_S_Cart<br>where product_id = %s and user_id = %s SQL statement is executed, where<br>%s is replaced with the id of the product and the user_id of<br>the logged-in user.</li><li>If the deletion is successful, a message is flashed to the<br>user indicating that the item has been deleted.</li><li>If there is an error during<br>the deletion process, an error message is flashed to the user.</li></ol><li>Deleting all items<br>from the cart:</li><ol><li>If the delete_all parameter is included in the request, the entire<br>cart for the logged-in user is cleared.</li><li>The DELETE FROM IS601_S_Cart WHERE user_id =<br>%s SQL statement is executed, where %s is replaced with the user_id of<br>the logged-in user.</li><li>If the deletion is successful, a message is flashed to the<br>user indicating that the cart has been cleared.</li><li>If there is an error during<br>the deletion process, an error message is flashed to the user.</li></ol></ol></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vamsirangu999/IS601-004/pull/21">https://github.com/vamsirangu999/IS601-004/pull/21</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Updating the database is a critical aspect of any web application. As data<br>is added or changed within the application, it must be reflected in the<br>database to ensure that the data is accurate and up-to-date. Failure to keep<br>the database updated can lead to errors and inconsistencies in the application. To<br>prevent this, it is important to regularly check and update the database as<br>necessary.</div><div><br></div><div>Jinja templates are a powerful tool for rendering dynamic content within Flask applications.<br>They allow developers to write HTML code that includes placeholders for dynamic content,<br>which is then filled in with data from the application. This makes it<br>easy to create dynamic pages that display data based on user input or<br>other factors. However, it is important to be mindful of the data being<br>displayed in the Jinja templates, as sensitive information should be protected from unauthorized<br>access.</div><div><br></div><div>Implementing roles in Flask can help to ensure that users have appropriate access<br>to different parts of the application. By assigning roles to users based on<br>their level of access, developers can limit the actions that users are able<br>to perform within the application. This can help to prevent unauthorized access to<br>sensitive data or functionality. It is important to ensure that roles are assigned<br>correctly and that users are only able to perform actions that are appropriate<br>for their level of access</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vr76-milestone1-prod.herokuapp.com">https://vr76-milestone1-prod.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-shop-project/grade/vr76" target="_blank">Grading</a></td></tr></table>