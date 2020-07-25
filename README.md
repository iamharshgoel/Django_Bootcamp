Django BOOTCAMP

-> The Front-End is what you see as a user on the website
-> The Back-End is the technology used to actually decide what to show you on the Front-End.

Best referring websites fot Front-End are:-
-> w3schools.com
-> developer.mozilla.org

#################
# HTML:-        #
#################
Hyper Text Markup Language

There are two ways to make the text bold <b> or <strong> tag.
There are two ways to make the text italics <i> or <em> emphasis tag.

=> How to make lists in HTML?
1. An unordered list starts with the <ul> tag. Each list item starts with the <li> tag.
2. An ordered list starts with the <ol> tag. Each list item starts with the <li> tag.
3. The <dl> tag defines the description list, the <dt> tag defines the term (name), and the <dd> tag describes each term

=> Difference between <div> and <span> tag?
The difference between <span> and <div> is that a <span> element is in-line and usually used for a small chunk of HTML inside a line (such as inside a paragraph) whereas a <div> (division) element is block-line (which is basically equivalent to having a line-break before and after it) and used to group larger chunks of code.

The <table> tag defines an HTML table.

Each table row is defined with a <tr> tag. Each table header is defined with a <th> tag. Each table data/cell is defined with a <td> tag.

By default, the text in <th> elements are bold and centered.

By default, the text in <td> elements are regular and left-aligned.


Forms are created using <form> tag which contains <input>,<label>,<select>, <option> tags inside for different information.
For more on forms and HTML check out:- w3schools.com

####################################
# CSS:-
####################################
Cascading Style Sheet

https://www.w3schools.com/css/css_intro.asp

css file is linked with html page via <link> tag.

selected tag{
        property: value;
}

In CSS classes are represented using . and id's are represented using #
Eg. .firstclass{
           color: red;
           }

#firstid{
       color: red;
       }

*(asterisk) is used for selecting every element on the page.

Specificity defines the hierarchy of CSS styling, and what type of tags overrule others.

Fonts:- There are several fonts available in CSS but we can use other font families also which are  not present in our system

1em = 16px

cssfontstack.com is the best link for different font styles.

The order of margin, padding, border is always:- top, right, bottom, left

coolors.co is used for color palettes.

#################################
# BOOTSTRAP:-
#################################

It contains 12 columns and infnite rows.
Most important framework of front-end development

=> Framework
          - Inversion of Control
          - Default Behavior
          - Extensibility
          - Non-modifiable Framework Code

A key feature of Bootstrap are its default classes

Jumbotron is a lightweight, flexible component that can optionally extend the entire viewport to showcase key content on your site.

Navbars are navigational bars that you will often see on the top of a website

The grid system provides the core mechanism by which using Bootstrap allows websites to look good across multiple devices of multiple screen sizes.

The grid system call will make use of the class='row'
Inside of a row class, we then have the following format:
-> col-ScreenSize-NumberOfColumns

##################################
# JAVASCRIPT:-
##################################

Javascript support is built directly into modern web browsers.
We can run Jvascript directly into the browser console, or as a full .js script connected to an HTML file.

Javascript is a full programming language, meaning unlike HTML or CSS is supports things such as arrays, loops and general logic.

Commenting in Javascript is done by using //

There is no distinction between int, float, negative .... all are treated as numbers.

clear() is used to clear the console.
+ is used to concatenate two strings.
.length is used to check the length of the string.
\n starts a new line.
\t gives a tab.
\" gives a quote in quotes.
var varName = value; is the basic format for declaring and initialising variable using var keyword.
undefined is the state between declaration and initialisation.

alert() is used for creating pop-up on browser page.
console.log() is used for printing out statement or values in JavaScript
prompt() is used to give input to the variable

If you want to check the equality in string and a number then use ===

JavaScript has three types of For Loops:
-> For - loops through a number of times
-> For/In - loops through a JS object
-> For/of - used with arrays

-> num = num +1
-> num +=1
-> num++
these three are all the same

Functions in JavaScript:-
They allow us to easily reuse code more than once and not constantly repeat ourselves.
function keyword is used to create functions.
Scope in JavaScript refers to the current context of code, which determines the accessibility of variables to JavaScript. The two types of scope are local and global: Global variables are those declared outside of a block. Local variables are those declared inside of a block.

Arrays in JavaScript:-
Arrays are mutable
Strings are immutable
array.pop() function is used to remove the last element of the array.
array.push function is used to add an item at the last of the array.

for of loop:-
for(a of array){
    console.log(a);
}  //basic structure of for of loop

forEach loop:-
array.forEach(function);   /?basic structure if forEach loop

splice() method is an inbuilt method in JavaScript which is used to modify the contents of an array by removing the existing elements and/or by adding new elements. Parameter: This method accepts many parameters some of them are described below: index: It is a required parameter.


Objects in JavaScript:
JS Objects are hash-tables, they store information in a key-value pair
When we loop over Objects in JS then they dont have any specific order of printing for key:value pairs.

Object methods are essentially functions that are inside of an object.
For a JS Objet, the **this** keyword is set to the object is called on.

The split() method is used to split a string into an array of substrings, and returns the new array.

**DOCUMENT OBJECT MODEL(DOM)**
The DOM will allow us to interface our JavaScript code to interact with HTML and CSS.
Browsers will contruct the DOM, which basically means storing all the HTML tags as JavaScript objects.
Here are some important document attributes:
-> document.URL -- This is the actual URL of the website-
-> document.body -- This is everything inside of the body
-> document.head -- This is everything in the head of the page
-> documnet.links -- These are all the links on the page

Then we also have methods we can use to grab HTML elements:

-> document.getElementById() -- Returns the element with the id
-> document.getElementsByClassName() -- Returns list of all elements belonging to a class
-> document.getElementsByTagName() -- Returns list of all elements with the tag
-> document.querySelector() -- Returns the first object matching the CSS style selector
-> document.querySelectorAll() -- Returns all objects matchin the CSS style selector

To Edit Styles, we've already seen we can use the .style tag. Now if we want to edit actual html or text or attributes we can use different methods. If you want to change the text,html content, or attributes you can use the following:

myvariable.textContent - This returns just the text
myvariable.innerHTML - This returns the actual html
myvariable.getAttribute() - This returns the original attribute
myvariable.setAttribute() - This allowed you to set an attribute

myvariable.addEventListener(event, func)
There are many possible events:-
-> clicks
-> Hovers
-> Double Clicks
-> Drags etc.

-> https://developer.mozilla.org/en-US/docs/Web/Events

"mouseover" and "mouseout" are the conditions for Hovering mouse.
"click" is used for click function.
"dblclik" is used for double click function.



**jQuery**
-> jQuery is a JavaScript library.
-> It is just a large single .js file that has many pre-built methods and objects that simplify your workflow.
-> Specifically interacting with the DOM and making HTTP requests(AJAX).

//jQuery
var divs = $('div');

//Vanilla
var divs = document.querySelectorAll('div');

//jQuery
$(el).css('border-width', '20px');

//Vanilla
el.style.borderWidth = '20px';

//jQuery
$(document).ready(function(){ //code });

//Vanilla
function ready(fn){
    if (document.readyState != 'loading'){
       fn();
      }else{
       document.addEventListener('DOMContentLoaded', fn);
       }

**code.jquery.com**

To make round buttons in CSS make border-radius: 50%;


############################################
**Back-End**
###########################################

**Python**

# Strings in Python:-
-> Strings in Python are used to hold text information and are indicated with the use of single or double quotes.

-> They are a sequence of characters, meaning they can be indexed using bracket notation.

string.upper() converts the whole string to Uppercase.
string.capitalize() converts the first letter capital in the string.
string.split() converts the multi word string string into list of words.


# Lists in Python:-
-> Lists are the arrays form of Python
-> Lists are mutable in nature.

list.append(["a","b"]) will append list in a list 
list.extend(["a","b"]) will extend the list further after.

list.pop() is used to remove the item from list and it always returns the removed item.

list.reverse() is used to reverse the order of list.
list.sort() the list in ascending order.

# Dictionaries in Python:-
-> Dictionaries are Python's version of Hash Tables
-> They allow us to create a "mapping" with key-value pairs.
-> They don't retain any order.

# Some Key Points:-
-> Tuples are immutable sequences.
-> Sets are unordered collections of unique elements.
-> Booleans are just True and False.

-> Functions in Python use def keyword.

def function(){
    """
    THis THE DOCSTRING
    """
    }

Python Scope follows the LEGB rule:-
-> Local
-> Enclosing Function Locals
-> Global
-> Built-in


* L: Local -- Names assigned in any way within a function (def or lambda), and not declared global in that function.

* E: (EFLs) -- Name in the locsl scope of any and all enclosing functions (def or lambda), from inner to outer.

* G: Global (module) -- Names assigned t the top-level of a module file, or declared global in a def within th file.
Effect of global keyword in the function is permanent.
return keyword also somewhat have same effect as global keyword.


* B: Built-in (Python) -- Names preassigned in the built-in names module:
                          ope, range, SyntaxError,...


# Object Oriented Programming

* Object Oriented Programming is a way to use Python to create our own objects.
* Methods are functions defined inside the body of a class they're used to perform operations.
* **Inheritance** is a way to form new classes using older classes that have already been defined that way.
* The newly formed classes are called derived classes and the classes that we derive from are called the base classes.

def __str__(self) is the method used for string representation.
def __len__(self) is the method used for length. 
def __del__(self) is the method used for deletion.

# Errors and Exceptions
* One way to open the file is by using open() function, it consists of two parameters, the first parameter contains the file name and the second parameter in the open() function dictates whether you are opening the file for just reading, just writing, or to do both.

* Errors detected during execution of the file are called exceptions.
* Use these keywords from getting errors:
-> try
-> except
-> Finally

try, except actually helps you do is handle errors and then continue on with your code.
finally key block of code will always be run regardless if there's an exception in the try code block.

# Regex
Regular Expressions allow us to search for patterns in Python strings.
http://regexcheatsheet.com/

-> * means 0 or more
-> ? means 0 and 1 time
-> + means 1 or more
-> ^ is used for exclusion
