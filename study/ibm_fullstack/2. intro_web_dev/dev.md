1. Web APIs Reference
   https://developer.mozilla.org/en-US/docs/Web/API?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkCD0101ENSkillsNetwork1051-2022-01-01

JavaScript APIs (Application Programming Interfaces) are sets of instructions that allow web developers to access certain functionality or data from an external source, such as a web service, and use it in their own web applications. These APIs are typically made available via a URL endpoint that developers can send HTTP requests to in order to retrieve or manipulate the data.

APIs use a request-response model, meaning that a developer sends a request to the API endpoint, and the API sends a response back to the developer's application. The request typically includes information such as the type of data being requested, any authentication credentials that may be required, and any other relevant parameters. The response typically includes the requested data in a format such as JSON or XML.

JavaScript is often used to make these API requests directly from the browser, using techniques such as AJAX (Asynchronous JavaScript and XML) or Fetch, which allows the developer to retrieve data from an API without needing to refresh the entire web page. This enables a more dynamic and interactive user experience by making it possible for web pages to update in real-time based on data from an API.

Overall, JavaScript APIs enable developers to build powerful web applications by making it easy to access external functionality and data, that allows enrich the experience of their applications.

Mohamed Riswan Mohamed Saheed
DOM API
The DOM (Document Object Model) API is a programming interface for HTML and XML documents. It represents the structure of a document as a tree-like object model, with each node in the tree representing a piece of the document, such as an element, an attribute, or text content.

The DOM API provides a way for JavaScript to access and manipulate the content and structure of a web page. For example, it allows you to:

Traverse the document tree to find elements by their tag name, class name, or ID
Get and set the content, attributes, and styles of elements
Add, remove, and move elements in the tree
Using the DOM API, a developer can change the contents or layout of a web page in response to user input, browser events, or other triggers.

The DOM is also a standard, which means that it is implemented consistently across different web browsers, so the same JavaScript code that uses the DOM API will work on different browsers. There are two main versions of the DOM specification: DOM Level 1 and DOM Level 2. The DOM Level 1 specification is split into two parts: Core and HTML. The DOM Level 2 specification is split into several modules, like the DOM Event specification.

Overall the DOM API allows developers to access the content and structure of web pages, and interact with it, through JavaScript, to make dynamic and interactive web pages.

Mohamed Riswan Mohamed Saheed
what are the complete list of DOM APIs with example?
The DOM (Document Object Model) API provides a wide range of methods and properties for manipulating the content and structure of a web page. Here is a list of some common DOM APIs along with examples:

document.getElementById(id): Retrieves an element from the document by its unique id.
Copy code
// HTML: <p id="myParagraph">Hello World</p>
var myParagraph = document.getElementById("myParagraph");
console.log(myParagraph.textContent); // "Hello World"
document.getElementsByTagName(tagName): Retrieves a collection of elements from the document by their tag name.
Copy code
// HTML: <p>Hello</p><p>World</p>
var paragraphs = document.getElementsByTagName("p");
console.log(paragraphs[0].textContent); // "Hello"
console.log(paragraphs[1].textContent); // "World"
document.getElementsByClassName(className): Retrieves a collection of elements from the document by their class name.
Copy code
// HTML: <p class="my-class">Hello</p><p class="my-class">World</p>
var elements = document.getElementsByClassName("my-class");
console.log(elements[0].textContent); // "Hello"
console.log(elements[1].textContent); // "World"
element.querySelector(selector): Retrieves the first element in the document that matches a specified CSS selector.
Copy code
// HTML: <p class="my-class">Hello</p><p class="my-class">World</p>
var element = document.querySelector(".my-class");
console.log(element.textContent); // "Hello"
element.querySelectorAll(selector): Retrieves all elements in the document that match a specified CSS selector.
Copy code
// HTML: <p class="my-class">Hello</p><p class="my-class">World</p>
var elements = document.querySelectorAll(".my-class");
console.log(elements[0].textContent); // "Hello"
console.log(elements[1].textContent); // "World"
element.innerHTML: gets or sets the HTML content within an element
Copy code
//HTML: <div id="myDiv"></div>
var myDiv = document.getElementById("myDiv");
myDiv.innerHTML = "Hello <b>World</b>";
console.log(myDiv.innerHTML); // "Hello <b>World</b>"
element.textContent: gets or sets the text content within an element
Copy code
//HTML: <div id="myDiv">Hello <b>World</b></div>
var myDiv = document.getElementById("myDiv");
console.log(myDiv.textContent); // "Hello World"
myDiv.textContent = "New Text";

Mohamed Riswan Mohamed Saheed
more
Here are some more commonly used DOM APIs and examples of how they are used:

element.style: gets or sets the inline styles of an element.
Copy code
//HTML: <div id="myDiv"></div>
var myDiv = document.getElementById("myDiv");
myDiv.style.backgroundColor = "red";
myDiv.style.height = "100px";
element.setAttribute(name, value): sets the value of an attribute on an element.
Copy code
//HTML: <img id="myImg" src="image.jpg">
var myImg = document.getElementById("myImg");
myImg.setAttribute("alt", "A beautiful image");
element.getAttribute(name): gets the value of an attribute on an element.
Copy code
//HTML: <img id="myImg" src="image.jpg" alt="A beautiful image">
var myImg = document.getElementById("myImg");
console.log(myImg.getAttribute("alt")); // "A beautiful image"
element.addEventListener(event, callback): registers an event listener on an element that will be invoked when the specified event occurs.
Copy code
//HTML: <button id="myButton">Click me</button>
var myButton = document.getElementById("myButton");
myButton.addEventListener("click", function() {
alert("Button was clicked!");
});
element.appendChild(child): adds a child element to an element.
Copy code
//HTML: <div id="myDiv"></div>
var myDiv = document.getElementById("myDiv");
var newP = document.createElement("p");
newP.textContent = "Hello World";
myDiv.appendChild(newP);
element.removeChild(child): removes a child element from an element.
Copy code
//HTML: <div id="myDiv"><p id="myP">Hello World</p></div>
var myDiv = document.getElementById("myDiv");
var myP = document.getElementById("myP");
myDiv.removeChild(myP);
These are just some of the most commonly used DOM APIs, but there are many more available, depending on the specific manipulation or information you need to retrieve from the page.

Mohamed Riswan Mohamed Saheed
more
Sure, here are some more methods available in the DOM API:

document.createElement(tagName): creates a new element with the specified tag name.
Copy code
var newDiv = document.createElement("div");
newDiv.textContent = "Hello";
document.body.appendChild(newDiv);
document.createTextNode(text): creates a new text node with the specified text.
Copy code
var newText = document.createTextNode("Hello World");
var newDiv = document.createElement("div");
newDiv.appendChild(newText);
document.body.appendChild(newDiv);
parentNode.insertBefore(newNode, referenceNode): inserts a new node before the reference node in the parent element.
Copy code
var newP = document.createElement("p");
newP.textContent = "Inserted paragraph";
var referenceNode = document.getElementById("existing-element");
var parent = referenceNode.parentNode;
parent.insertBefore(newP, referenceNode);
element.cloneNode(deep): creates a duplicate of the element, if deep is true it will also clone the children.
Copy code
var original = document.getElementById("existing-element");
var clone = original.cloneNode(true);
document.body.appendChild(clone);
element.hasChildNodes(): returns a Boolean indicating whether an element has any child nodes.
Copy code
var element = document.getElementById("existing-element");
console.log(element.hasChildNodes());
element.compareDocumentPosition(otherNode): returns a bitmask indicating the position of the current element with respect to the other element
element.isEqualNode(otherNode): compares the current node with otherNode and returns true if they are equal and false otherwise.
It's worth noting that all these methods and properties are available for most of the elements on the DOM and not just for certain specific elements. With them, you can manipulate and inspect elements, text, attributes and layout on the page.

Let me know if you have any more questions or if there's any other specific thing you'd like to know about the DOM API.
