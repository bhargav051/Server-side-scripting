# Frappe Framework: Server Script / Hooks Controllers

## Hooks

### 1. What is hooks.py, How does hooks work?
Hooks in Frappe are configuration points where you can extend or override the core functionalities. The `hooks.py` file allows you to define events, scheduled tasks, custom permissions, and more.

### 2. Why do we use hooks.py file?
We use `hooks.py` to customize the behavior of the Frappe application without altering the core code. This makes it easier to maintain and upgrade the application. For more details, refer to the [official documentation](https://frappeframework.com/docs/user/en/python-api/hooks).

## Server Script

### 1. Server Py Controllers. What are controllers?
Controllers in Frappe are Python scripts that manage the logic of DocTypes. They control how data is processed and ensure the correct functioning of various operations.

### 2. How to use it.
To use controllers, you create custom Python scripts for your DocTypes. You can find more information on controllers [here](https://frappeframework.com/docs/user/en/basics/doctypes/controllers).

### Server script:
For more information on server scripts, refer to the [ERPNext documentation](https://docs.erpnext.com/docs/user/manual/en/server-script).

## Assignment

### 1. Create a dashboard, and add number cards in it, with the (whitelisted) custom method.
- Develop a custom dashboard and include number cards using whitelisted methods to display key metrics.

### 2. Create a script report showing the following columns: customer name, sales order name, delivery date, item code, item name, and item qty from sales order.
- Generate a script report that displays customer details along with sales order information including delivery dates and item specifics.

### 3. Override Python Class.
- Demonstrate how to override an existing Python class in Frappe.

### 4. Override Method.
- Show the process of overriding a specific method in Frappe.

### 5. Create an API to get the list of users and create an API to create a user.
- Develop REST APIs for retrieving a list of users and creating a new user in the system.

### 6. Create Frappe REST APIs for CRUD operations of any DocType.
- Implement REST APIs to perform Create, Read, Update, and Delete operations on a specified DocType.

### 7. Create a new DocType, add first name, last name, and full name as a data field, and a check box; if the check box is checked and first name and last name are filled with values, then the full name = first name and last name (Use validate trigger).
- Design a new DocType with the specified fields and functionality, ensuring the full name is automatically populated based on the checkbox status and input values using a validate trigger.
