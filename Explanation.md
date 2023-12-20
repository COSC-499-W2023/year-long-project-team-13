# Bootstrap/Styling Explanation

When you're using base CSS, you can include the styling in one of two ways:

1. Include the CSS file in your HTML file's `<head>` tag.
2. Copy the CSS file's contents into your own CSS file.

You almost always want to use option 2, because it's faster for the browser to load one CSS file than it is to load multiple CSS files. Also, it's more readable/reusable to have all of your CSS in one file — you can easily reuse styles across multiple pages.

## Bootstrap

However, since you're using a **CSS framework** (Bootstrap in your case), you're given base CSS styles. This is done by adding classes to your HTML elements. For example, if you want to make a button, you can add the class `btn` to your `<button>` element. This will give it the base button styles. Like this:

```html
<button class="btn">Click me!</button>
```

Since you added the `btn` class to your button, it will have the base button styles. You can also add other classes to your button to give it more styles. For example, if you want to make a button that's red, you can add the `btn-danger` class to your button. There's a huge list online of pre-made classes you can use.

### The Grid System

The other very important set of classes Bootstrap takes care of is the **grid system**. This is what allows you to make your website *responsive* (regardless of screen size), and also allows you to easily position elements on your page.

Image your page is a grid split into 12 columns. You can then add classes to your elements to tell them how many columns they should take up. For example, if you want an element to take up 6 columns, you can add the class `col-6` to it. If you want an element to take up 3 columns, you can add the class `col-3` to it. If you want an element to take up 12 columns, you can add the class `col-12` to it. And so on.

Then, you can get more fine-grain, and add classes to tell your elements how many columns they should take up on different screen sizes. For example, if you want an element to take up 6 columns on a large screen, but 12 columns on a small screen, you can add the classes `col-lg-6 col-sm-12` to it. The `lg` stands for "large", and the `sm` stands for "small". There are also `md` (medium) and `xs` (extra small) classes.

Here is an example of a grid system:

```html
<div class="row">
  <div class="col-6 col-sm-12">
    This element will take up 6 columns on a large screen, and 12 columns on a small screen.
  </div>
  <div class="col-6 col-sm-12">
    This element will take up 6 columns on a large screen, and 12 columns on a small screen.
  </div>
</div>
```