# Luizalabs Employee Manager

Rest API for control employees


### Built With
* [Python](https://www.python.org/) A programming language that lets you work quickly
* [Django](https://www.djangoproject.com/) The web framework for perfectionists

 ### Authors
 
 * **Cassiano Souza** - *Initial work* - [borgessouza](https://github.com/borgessouza)

### Executing 
```
python manage.py runserver
```

### Prerequisites
* Python==3.5.3
* Django==2.0.5
* djangorestframework==3.8.2
* pytz==2018.4


### API Documentation

**Add Employee**
----
Add new Employee in the data params 

* **URL:** /employee/

* **Method:** POST

* **Data Params:**
```json
  {
      "first_name": "first",
      "last_name": "last",
      "department": "dept",
      "email": "email@company.com"
  }
```

* **Success Response:**
  * **Code:** 201 Created
  * **Content:**
```json
     {
         "id" : 1,
         "first_name": "first",
         "last_name": "last",
         "department": "dept",
         "email": "email@company.com"
     }
```

* **Error Response:**
  * **Code:** 400 Bad Request

    
---
**Update Employee info**
---
  Update the employee in the data params
  
* **URL:** /employee/id

* **Method:** PUT

* **URL Params:**

   `id=[integer]`
   
* **Data Params:**
```json
{
    "first_name": "first",
    "last_name": "last",
    "department": "dept",
    "email": "email@company.com"
}
```   

* **Success Response:**
  * **Code:** 200 OK
  
 * **Error Response:**
   * **Code:** 400 Bad Request
   * **Code:** 404 Not Found
 
 
 ---
 **Delete Employee**
 ----
   Delete the employee
   
 * **URL:** /employee/id
 
 * **Method:** DELETE
 
 *  **URL Params:**
 
    `id=[integer]`
 
 * **Success Response:**
   * **Code:** 204 No Content
   
  * **Error Response:**
    * **Code:** 404 Not Found

     
---
**List Employees**
----
  List all employees
     
   * **URL:** /employee/
   
   * **Method:** GET
   
   * **Success Response:**
     * **Code:** 200 OK
     * **Content:**
```json
[
  {
    "id" : 1,
    "first_name": "first",
    "last_name": "last",
    "department": "dept",
    "email": "email@company.com"
  }
]
```

       
---
 **List Employee by id**
----
 List employee by id
     
   * **URL:** /employee/id
   
   * **Method:** GET
   
   *  **URL Params:**
    
       `id=[integer]`
   
   * **Success Response:**
     * **Code:** 200 OK
     * **Content:**
 ```json
     {
         "id" : 1,
         "first_name": "first",
         "last_name": "last",
         "department": "dept",
         "email": "email@company.com"
     }
 ```
     
   * **Error Response:**
     * **Code:** 404 Not Found