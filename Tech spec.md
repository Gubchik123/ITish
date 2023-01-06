# 1. Introduction

Blog site "ITish".

## 1.1 Purpose

Write a blog site to practice working with the Flask framework and provide it to anyone who wants to use it to publish posts.
Everyone can visit the site, visit the "About" and "FAQs" pages, search for and read posts, etc.
Only registered users can create new posts, like them, and comment on them.

## 1.2 Scope

-   Write site markup;
-   Use Bootstrap 5 for some custom styles;
-   Write a Flask application using Python;
-   Work out the structure of the database;
-   Set up the migration mechanism;
-   Deploy the site to hosting.

## 1.3 Overview

-   General pages
    -   Home page
    -   Blog page (with all posts)
    -   User profile view page
    -   Post view page
    -   About page
    -   FAQs page
    -   Feedback page
-   Auth pages
    -   Login page
    -   Register page
    -   Admin login page
-   User pages
    -   Profile page
        -   Pages with a list of all:
            -   User posts
            -   User comments
            -   User likes
    -   Profile edit page
    -   Post creation page
    -   Post edit page
-   Admin pages
    -   Admin home page
    -   Pages with a list of all:
        -   Users
        -   Posts
        -   Tags
        -   Likes
        -   Comments
    -   Edit page
    -   Creation page

# 2. Functional requirements

The system consists of the following main functional blocks:

-   Registration, authentication and authorization;
-   Guest functionality;
-   User functionality;
-   Admin functionality.

## 2.1. User types

The system provides for three types of people:

-   Guest (a person who can visit general pages and read posts created by other users);
-   User (a registered person who can create new posts, comment and like them, has access to a profile and can keep abreast of their own activity);
-   Admin (a person who knows the admin password. Admin can create, read, update and delete users, posts, tags, likes and comments).

## 2.2. Registration

Registration should consist of user data such as username, email, and password.

The registration form should include fields such as:

1. Username (required field);
2. Email (required field);
3. Password (required field);
4. Password again (should be equal to the first password field).

## 2.3. User authentication

User authentication should be by email and password.

## 2.4. Admin authentication

Admin authentication should be by admin password.

## 2.5. Guest functionality

Guest can:

-   Visit the "Home," "About" and "FAQs" pages;
-   Visit the "Blog" page for a list of all posts;
-   Read any post created by another user;
-   Visit the "Feedback" page and send a feedback email to the author.

Guest can see but cannot:

-   Like posts;
-   Comment posts;
-   Create posts;
-   Edit any posts;
-   Having a personal profile

## 2.6. User functionality

After authentication, the user gets access to such functional blocks as:

-   Post commenting;
-   Post liking;
-   Creating your own posts;
-   Editing your own posts;
-   Having a personal profile;
-   Editing a personal profile.

### 2.6.1. Post commenting

The user can see the special form for writing comments under each post. Comments will consist of a username, body and the date and time they were created.

### 2.6.2. Posts liking

The user has access to a "like" button next to each post. This "like" button should be on the "Blog" page for all posts and on every post page.

### 2.6.3. Creating your own posts

The user has access to the post creation page.
The initial post creation page should contain:

1. A short hint
2. Field for post title (required field)
3. Empty area for post-body
4. Buttons for adding:
    - Subtitle 1 (\<h3>)
    - Subtitle 2 (\<h4>)
    - Paragraph (\<p>)
    - Code block (\<code>)
    - Image (\<img>)
    - Note (Bootstrap 5 alert)
    - Line (\<hr>)
5. Field for tags (optional)
6. Post-publish button

> Should use JavaScript for dynamically adding content.

> Every added element should include a button for deleting this one (and for future editing).

### 2.6.4. Editing your own posts

If the user has posted something, he or she can edit it.
The post edit page should be like the creation page, but in the post area there should be post content from the database.

> Need to find general JS functions and create another file. js for it

### 2.6.5. Having a personal profile

General information about the user should be printed:

-   Avatar,
-   Username,
-   Email,
-   Count of user:
    -   Posts,
    -   Likes,
    -   Comments.

And a profile should consist of the following pages:

-   User posts,
-   User likes,
-   User comments.

> These pages should be defined with the "tab" argument in the url.
> Example: /profile/?tab=posts

> On these pages, users can see and delete information.

### 2.6.6. Editing personal profile

The user can edit personal information:

-   Avatar,
-   Username,
-   Email,
-   Password.

That's why on this page there should be three forms for editing.

## 2.7. Admin functionality

Flask-Admin should be used for admin functionality.

> Add all models for admin to show them on admin pages.

> Need to redefine "master.html" in Flask-Admin and print the information on the admin panel about the general count of users, posts, tags, likes and comments.

## 2.8. Blueprints

-   Auth (for working with registration, authentication and authorization);
-   Blog (for working with posts and others that are connected with them);
-   Profile (for working with user profiles and pages that are connected with them).

## 2.9. File structure

<pre>
ITish
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── funcs.py
│   ├── views.py
│   ├── config.py
│   ├── models.py
│   ├── extensions.py
│   │
│   ├── auth
│   │   ├── __init__.py
│   │   ├── funcs.py
│   │   ├── forms.py
│   │   └── blueprint.py
│   ├── blog
│   │   ├── __init__.py
│   │   ├── funcs.py
│   │   ├── forms.py
│   │   └── blueprint.py
│   ├── profile
│   │   ├── __init__.py
│   │   ├── funcs.py
│   │   ├── forms.py
│   │   └── blueprint.py
│   │
│   ├── static
│   │   ├── js
│   │   ├── css
│   │   └── images
│   │
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── error.html
│       ├── _messages.html
│       ├── _forms_macros.html
│       ├── _alerts_macros.html
│       │
│       ├── admin
│       │   └── master.html
│       ├── auth
│       │   ├── login.html
│       │   ├── admin_login.html
│       │   └── registration.html
│       ├── blog
│       │   ├── index.html
│       │   ├── tag.html
│       │   ├── post.html
│       │   ├── add_post.html
│       │   ├── edit_post.html
│       │   ├── _pagination.html
│       │   └── _post_macros.html
│       └── profile
│           ├── index.html
│           ├── edit.html
│           ├── posts.html
│           ├── likes.html
│           └── comments.html
├── env
├── run.py
├── README.md
├── .gitignore
├── Tech spec.md
│
├── md_images
│   ├── telegram_icon.png
│   ├── readme_header.png
│   └── database_structure.jpg
└── requirements
    ├── base.txt
    ├── development.txt
    └── production.txt
</pre>

## 2.10. Database structure

<img title="DB" alt="Database structure image" src="./md_images/db_structure.jpg">

# 3. Technology stack

To implement the site, the following stack of technologies is proposed:

-   Backend:
    -   Python programming language;
    -   Flask framework;
    -   MySQL / PostgreSQL database;
    -   SQLAlchemy ORM;
    -   Flask-Migrate (for migrations).
-   Frontend:
    -   JavaScript;
    -   Bootstrap 5.

# 4. Non-functional requirements

-   Localization and languages
-   Design requirements
    -   General site structure
    -   Layout requirements
-   Graphic content
-   Website domain, hosting
-   Browser support
-   Requirements for the development of the site from the standpoint of search engine promotion
    -   General
    -   Text
    -   Images
    -   Meta tags

## 4.1. Localization and languages

The site must be implemented in English.

## 4.2. Design requirements

Minimalist design with clear content. Site layout must be implemented on the Bootstrap 5 layout framework because Bootstrap supports the latest, stable releases of all major browsers and platforms.

### 4.2.1 General site structure

-   Header
-   Main
-   Footer

The site header should have a light/dark mode switcher. The footer of the site should have a logo and links to the author's social networks.

### 4.2.2 Layout requirements

-   Should be displayed correctly, both on computers and on mobile devices;
-   Should be cross-browser.

## 4.3 Graphic content

-   Favicon image (website icon for the browser);
-   Application logo image;
-   Icon set on [ionicons](https://ionic.io/ionicons).

## 4.4 Website domain, hosting

Use PythonAnywhere hosting (which will give us a domain) to deploy the site because it has web application support and provides a MySQL database.

## 4.5 Browser support

The site should open and function correctly in the current versions of the main popular browsers: Chrome, Firefox, Safari, etc.

## 4.6 Requirements for the development of the site from the standpoint of search engine promotion

### 4.6.1 General

The site must meet the requirements of the Google search engine for ease of viewing on mobile devices. The requirements are displayed at https://developers.google.com/speed/docs/insights/mobile.

### 4.6.2 Text

-   It is necessary to place the text in the form of text (not pictures). It is desirable that the text be available immediately and not open on click, hover, etc. The text should not be hidden by JavaScripts;
-   The text on the site should be easy to read, formatted, and not contain spelling errors;
-   All site pages must contain unique text;
-   The text of the page should contain 1 heading with the H1 tag, which should include key words and phrases. There can be 2 headings with the H2 tag in the text, and they should also include keywords and phrases. You can't put all the text on the page in the title tag;
-   Headings should at least partially match the navigation.

### 4.6.3 Images

-   An alt-attribute must be registered for all pictures. You can't put more than 7 words in an alt attribute. As for images, they must be unique;
-   Only popular image extensions (JPEG and PNG) should be used.

### 4.6.4 Meta tags

-   It should be possible to edit meta tags and add text;
-   The \<title> tag must match the content of the page and include the main search queries, must include no more than 64 words;
-   The \<description> meta tag should be a brief and precise description of the content of the page and should not be the same as the \<title> tag.
