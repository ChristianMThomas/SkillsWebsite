// Printing  Basics in JavaScript

    console.log("Skills USA 2025");



// Variables in Javascript

    let firstName = "Bobby";      // declared firstName  with the value of Bobby
    let middleInitial = 'R';      // declared middleInitial  with the value of R
    let lastName = "Hill";        // declared lastName  with the value of Hill
    let age = 16;                 // declared age with the value of 16
    let isAStudent = true;        // declared isAStudent  with the value of true
    let hasAJob = false;          // declared hasAJob  with the value of false


//  let  vs const

    let day = "Monday";         //declared day with the value of Monday
    const numOfWeekDays = 7;    //declared a constant numOfWeekdays with the value of 7

    day = "Tuesday";            //reassigned day with the value of Tuesday


// Types in Javascript

let school = "Central Georgia Technical College"      // Type would be String
let GPA = 3.21;                                       // Type would be Number
let letterGrade = "A"                                 // Type would be String
let isATeacher = false;                               // Type would be boolean
let graduationDate;                                   // Type would be undefined

let students = [];                                    // Object Type would be Array

function print(){                                     // Object Type would be function
    console.log("Hello");
}





// Arithmetic //

let friends = 20;

friends = friends + 1;    // adding 1  this will give you 21
friends = friends - 1;    // subtracting 1  this will give you 20
friends = friends * 2     // multiplying by 2  this will give you 40
friends = friends / 2     // diving by 2  this will give you 20

// augment assingment operator  (shortcut)

friends +=1;        // adding 1  this will give you 21
friends -=1;        // subtracting 1  this will give you 20
friends *=2;        // multiplying by 2  this will give you 40
friends /=2;        // diving by 2  this will give you 20









firstName = "John";
lastName = "Doe";

// Using + operator
let fullName = firstName + " " + lastName;
console.log(fullName); // Output: John Doe

// Using template literals
let fullNameTemplate = `${firstName} ${lastName}`;
console.log(fullNameTemplate); // Output: John Doe


let text = "Hello, World!";

// Length of the string
console.log(text.length); // Output: 13

// Convert to uppercase
console.log(text.toUpperCase()); // Output: HELLO, WORLD!

// Convert to lowercase
console.log(text.toLowerCase()); // Output: hello, world!

// Find the position of a substring
console.log(text.indexOf("World")); // Output: 7

// Extract a substring
console.log(text.substring(0, 5)); // Output: Hello

// Replace a substring
console.log(text.replace("World", "JavaScript")); // Output: Hello, JavaScript!





// Using array literal
let fruits = ['Apple', 'Banana', 'Cherry'];

// Using Array constructor
let numbers = new Array(1, 2, 3, 4, 5);

let firstFruit = fruits[0]; // 'Apple'
let secondNumber = numbers[1]; // 2

// Adding elements
fruits.push('Orange'); // ['Apple', 'Banana', 'Cherry', 'Orange']
numbers.unshift(0); // [0, 1, 2, 3, 4, 5]

// Removing elements
let lastFruit = fruits.pop(); // 'Orange', fruits is now ['Apple', 'Banana', 'Cherry']
let firstNumber = numbers.shift(); // 0, numbers is now [1, 2, 3, 4, 5]


// Using for loop
for (let fruit in fruits) {
    console.log(fruit);
  }
  
  // Using forEach
  fruits.forEach(fruit => console.log(fruit));
  
  // Using map
  let upperCaseFruits = fruits.map(fruit => fruit.toUpperCase()); // ['APPLE', 'BANANA', 'CHERRY']
  


            //userInput
  //let userInput = prompt("Please enter your input:");
  //console.log("User input:", userInput);
  
