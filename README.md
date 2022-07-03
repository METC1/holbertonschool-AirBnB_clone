# AirBnB clone - The console

### Description of the project

The proyect consist in building a command interpreter, which is the first step towards building a full web application, an AirBnB clone.  This back-end console of the website, will allow the user to:

*Create a new object (ex: a new User or a new Place)
*Retrieve an object from a file, a database etc…
*Do operations on objects (count, compute stats, etc…)
*Update attributes of an object
*Destroy an object

#### Usage

To launch the console application in interactive mode simply run:

```console.py ```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#
Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | **EOF**
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key "value"\>

 
### Example
```
root@1cd2cac7724d:/home/holbertonschool-AirBnB_clone# ./console.py
(hbnb)all User
[User] (96d477bc-bd41-44c9-b998-53e783369d93) {'id': '96d477bc-bd41-44c9-b998-53e783369d93', 'created_at': datetime.datetime(2022, 7, 2, 17, 55, 23, 103548), 'updated_at': datetime.datetime(2022, 7, 2, 17, 55, 23, 103562)}
[User] (f80526f0-b347-4d18-b75f-427d1b745c2f) {'id': 'f80526f0-b347-4d18-b75f-427d1b745c2f', 'created_at': datetime.datetime(2022, 7, 2, 17, 57, 20, 808502), 'updated_at': datetime.datetime(2022, 7, 2, 17, 57, 20, 808511)}
(hbnb)create User
8e5cf3c1-4bff-4b2b-9770-666149dc33d0
(hbnb)show User 8e5cf3c1-4bff-4b2b-9770-666149dc33d0
[User] (8e5cf3c1-4bff-4b2b-9770-666149dc33d0) {'id': '8e5cf3c1-4bff-4b2b-9770-666149dc33d0', 'created_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512576), 'updated_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512590)}
(hbnb)update User 8e5cf3c1-4bff-4b2b-9770-666149dc33d0 first_name "Otto"
(hbnb)show User 8e5cf3c1-4bff-4b2b-9770-666149dc33d0
[User] (8e5cf3c1-4bff-4b2b-9770-666149dc33d0) {'id': '8e5cf3c1-4bff-4b2b-9770-666149dc33d0', 'created_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512576), 'updated_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512590), 'first_name': 'Otto'}
(hbnb)destroy User 96d477bc-bd41-44c9-b998-53e783369d93
(hbnb)all User
[User] (f80526f0-b347-4d18-b75f-427d1b745c2f) {'id': 'f80526f0-b347-4d18-b75f-427d1b745c2f', 'created_at': datetime.datetime(2022, 7, 2, 17, 57, 20, 808502), 'updated_at': datetime.datetime(2022, 7, 2, 17, 57, 20, 808511)}
[User] (8e5cf3c1-4bff-4b2b-9770-666149dc33d0) {'id': '8e5cf3c1-4bff-4b2b-9770-666149dc33d0', 'created_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512576), 'updated_at': datetime.datetime(2022, 7, 3, 16, 20, 15, 512590), 'first_name': 'Otto'}
(hbnb)
```
### List of object-attribute

**Common base attribute** *It's the base of all other object-attribute*

* **Base Model** : id, created_at, updated_at

**Specific object-attribute**

* **User** : email, password, first_name, last_name

* **Review** : place_id, user_id, text

* **Place** : city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

* **Amenity** : name

* **State** : name

* **City** : state_id, name
