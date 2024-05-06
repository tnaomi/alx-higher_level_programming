# 0x15-javascript-web_jquery

## Author

Tadala N. Kapengule

## Tasks

### 0. No JQuery

Write a JavaScript script that updates the text color of the ``<header>`` element to red ``(#FF0000)``:

- You must use ``document.querySelector`` to select the ``HTML`` tag
- You can’t use the ``JQuery`` API

__File__

``0-script.js``, test w ``0-main.html``

### 1. With JQuery

Write a JavaScript script that updates the text color of the ``<header>`` element to red (``#FF0000``):

- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__
``1-script.js``, test w ``1-main.html``

### 2. Click and turn red

Write a JavaScript script that updates the text color of the ``<header>`` element to red (``#FF0000``) when the user clicks on the tag ``DIV#red_header``:

- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__

``2-script.js``, test w ``2-main.html``

### 3. Add '.red' class

Write a JavaScript script that adds the class ``red`` to the ``<header>`` element when the user clicks on the tag ``DIV#red_header``

- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__

``3-script.js``, test w ``3-main.html``

### 4. Toggle classes

Write a JavaScript script that toggles the class of the ``<header>`` element when the user clicks on the tag ``DIV#toggle_header``:

- The ``<header>`` element must always have one class: ``red`` or ``green``, **never both** in the same time and **never empty**.
- If the current class is ``red``, when the user click on ``DIV#toggle_header``, the class must be updated to ``green`` ; and the reverse.
- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__
``4-script.js``, test w ``4-main.html``

### 5. List of elements

Write a JavaScript script that adds a ``<li>`` element to a list when the user clicks on the tag ``DIV#add_item``:

- The new element must be: ``<li>Item</li>``
- The new element must be added to ``UL.my_list``
- You can’t use ``document.querySelector`` to select the HTML tag
- You must use the ``JQuery`` API

__File__

``5-script.js``, test w ``5-main.html``

### 6. Change the text

Write a JavaScript script that updates the text of the ``<header>`` element to ``New Header!!!`` when the user clicks on ``DIV#update_header``

- You can’t use ``document.querySelector`` to select the ```HTML``` tag
- You must use the ``JQuery`` API

__File__

``6-script.js``, test w ``6-main.html``

### USING JQUERY WITH APIs

### 7. Star Wars character

Write a JavaScript script that fetches the *character name* from this URL: ``https://swapi-api.alx-tools.com/api/people/5/?format=json``

- The name must be displayed in the ``HTML`` tag ``DIV#character``
- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__

``7-script.js``, test w ``7-main.html``

### 8. Star Wars movies

Write a JavaScript script that fetches and lists the *title* for all movies by using this URL: ``https://swapi-api.alx-tools.com/api/films/?format=json``

- All movie titles must be list in the ``HTML`` tag ``UL#list_movies``
- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API

__File__

``8-script.js``, test w ``8-main.html``

### 9. Say Hello!

Write a JavaScript script that fetches from ``https://hellosalut.stefanbohacek.dev/?lang=fr`` and displays the value of hello from that fetch in the HTML tag ``DIV#hello``.

- The translation of *“hello”* must be displayed in the ``HTML`` tag ``DIV#hello``
- You can’t use ``document.querySelector`` to select the ``HTML`` tag
- You must use the ``JQuery`` API
- Your script must work when it is imported from the ``<head>`` tag

__File__

``9-script.js``, test w ``9-main.html``