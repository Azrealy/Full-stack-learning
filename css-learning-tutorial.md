* CSS classes are meant to be reused over many elements. By writing CSS classes, you can style elements in a variety of ways by mixing classes on HTML elements. Multi-classes example will be like following.
```javascript
.title {
    color: red;
}
.uppercase {
    text-transform: uppercase;
}

<h1 class="title uppercase">Hello Wold</h1>
```
* While classes are meant to be used many times, an ID is meant to style only one element. IDs can override the styles of tags and classes. Since IDs override class and tag style, they should be used sparingly and only on elements that need to always appear the same.
IDs example is can be like:
```javascript
#article-title {
    font-family: cursive;
    text-transform: capitalize;
}
<h1 id="article-title" class="title uppercase">hello world</h1>
```

# Specificity

Specificity is the order by which the browser decides which CSS styles will be displayed. IDs are the most specific selector in CSS followed by classes, and finally, tags.

The lowest elements like tags, which adding more than one tag, class or ID to a CSS selector increases the specificity of the CSS selector.

There is one thing that is even more specific than IDs: `!important`. This wll make you selectors hard to override.

Units for offset properties can be specified in pixels, ems, or percentages. Note that offset properties will not work if the value of the element's position property is the default static.

inline elements cannot be altered in size with the height or width CSS properties.

The CSS display property provides the ability to make any element an inline element. 