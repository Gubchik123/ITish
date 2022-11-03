# 1. Introduction

Blog site "ITish"

## 1.1 Purpose

Write a blog site to practice working with the Flask framework and provide anyone who wants to use this site to publish posts.
Everyone can visit site, visit 'About' and 'FAQs' pages, search and read posts etc.
Only registered user can create new posts, like and comment ones

## 1.2 Scope

-   Write site markup
-   Use Bootstrap 5 with some custom styles
-   Write Flask application using Python
-   Work out the structure of the database
-   Set up the migration mechanism
-   Deploy site on hosting

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

-   Registration, authentication and authorization
-   Guest functionality
-   User functionality
-   Admin functionality

## 2.1. User types

The system provides for three people types:

-   Guest (can visit general pages and read posts created by other users);
-   User (one is who registered. User can create new own posts. Also user can comment and like posts. Have access to profile and can keep abreast of self activity);
-   Admin (one is who know admin password. Admin can create, read, update and delete users, posts, tags, likes and comments).

## 2.2. Registration

Registration should consist for such user data as: username, email and password

Registration form should include such fields as:

1. username - required field
2. email - required field
3. password - required field
4. password again - should be equal to first password field

## 2.3. User authentication

User authentication should be by email and password

## 2.4. Admin authentication

Admin authentication should be by admin password

## 2.5. Guest functionality

Guest can:

-   Visit 'Home', 'About' and 'FAQs' pages
-   Visit 'Blog' page with list of all posts
-   Read any post created by other user
-   Visit 'Feedback' page and send a feedback to author email

Guest can see but cannot:

-   Like posts
-   Comment posts
-   Edit any posts
-   Create own posts
-   Have an own profile on the site

## 2.6. User functionality

After authentication, user gets access to such functional blocks as:

-   Post commenting
-   Liking posts
-   Creating your own posts
-   Editing your own posts
-   Having personal profile
-   Editing personal profile

### 2.6.1. Post commenting

User can see the special form for writing comment under every post. Comment will consist for username, body and created date and time

### 2.6.2. Liking posts

User has access to a like button next to each post. This like buttons should be on 'Blog' page for all posts and on every post page

### 2.6.3. Creating your own posts

User has access to a post creation page.
The initial post creation page should contain:

1. Short hint
2. Field for post title - required field
3. Empty area for post body
4. Buttons for adding:
    - Subtitle 1 (\<h3>)
    - Subtitle 2 (\<h4>)
    - Paragraph (\<p>)
    - Code block (\<code>)
    - Image (\<img>)
    - Note (Bootstrap 5 alert)
    - Line (\<hr>)
5. Field for tags - optional
6. Post publish button

> Should use JavaScript for dynamic adding content.

> Every added element should include for button for deleting this one (and for future editing)

### 2.6.4. Editing your own posts

If user has own post(s) the one can edit it
Post edit page should be like creation page, but in post area should be post content from database

> Need find general JS functions and create other file .js for it

### 2.6.5. Having personal profile

User has person profile.
In the main profile page should print general information about user:

-   Avatar
-   Username
-   Email
-   Count of user:
    -   Posts
    -   Likes
    -   Comments

And profile should consist for other subpages:

-   User posts
-   User likes
-   User comments

> This pages should be defined with 'tab' argument in url
> Example: /profile/?tab=posts

> On this pages user can see and delete information

### 2.6.6. Editing personal profile

User can edit personal information:

-   Avatar
-   Username
-   Email
-   Password

That's why on this page should be 3 form for editing

## 2.7. Admin functionality

Flask-Admin should be used for admin functionality

> Need add all models for admin for showing it on admin pages

> Need redefine 'master.html' in Flask-Admin and print the information on admin panel about general count of users, posts, tags, likes and comments

## 2.8. Blueprints

-   Auth (for working with registration, authentication and authorization)
-   Blog (for working with posts and others which are connected with them)
-   Profile (for working with user profile and pages which are connected with them)

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
│   ├── extentions.py
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
│       ├── _pagination.html
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
│       │   └── edit_post.html
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
└── requipments
    ├── base.txt
    ├── development.txt
    └── production.txt
</pre>

## 2.10. Database structure

# 3. Technology stack

To implement the site, the following stack of technologies is proposed:

-   Backend:
    -   Python programming language
    -   Flask framework
    -   MySQL / PostgreSQL database
    -   SQLAlchemy ORM
    -   Flask-Migrate for migrations
-   Frontend:
    -   JavaScript
    -   Bootstrap 5

# 4. Non-functional requirements

## 4.1. Localization and languages

The site must be implemented in English.

## 4.2. Design requirements

Minimalist design with clear content. Site layout must be implemented on the Bootstrap 5 layout framework, because Bootstrap supports the latest, stable releases of all major browsers and platforms.

### 4.2.1 General site structure

-   Header
-   Main
-   Footer

The site header should have a light/dark mode switcher. The footer of the site should have a logo and links to the author's social networks.

### 4.2.2 Layout requirements

-   Should be displayed correctly, both on computers and on mobile devices
-   Should be cross-browser

## 4.3 Graphic content

-   Favicon image (website icon for the browser)
-   Application logo image
-   Icon set on [ionicons](https://ionic.io/ionicons)

## 4.4 Website domain, hosting

Use PythonAnywhere hosting (it will give us a domain) to deploy the site, because it has web application support and it provides a MySQL database

## 4.5 Browser support

The site should open and function correctly in the current versions of the main popular browsers - Chrome, Firefox, Safari...

## 4.6 Requirements for the development of the site from the standpoint of search engine promotion

### 4.6.1 General

The site must meet the requirements of the Google search engine for ease of viewing on mobile devices. The requirements are displayed at https://developers.google.com/speed/docs/insights/mobile.

### 4.6.2 Text

-   It is necessary to place the text in the form of text (not pictures). It is desirable that the text be available immediately, and not open on click / hover, etc. The text should not be hidden by java scripts.

-   The text on the site should be easy to read, formatted, should not contain spelling errors.

-   All site pages must contain unique text.

-   The text of the page should contain 1 heading with the H1 tag, which should include key words/phrases, there can be 2 headings with the H2 tag in the text, and they should also include keywords/phrases. You can't put all the text on the page in the title tag.

-   Headings should at least partially match the navigation.

### 4.6.3 Images

-   Alt-attribute must be registered for all pictures. You can't put more than 7 words in an alt attribute. As for images, they must be unique.

-   Only popular image extensions (JPEG and PNG) should be used.

### 4.6.4 Meta tags

-   It should be possible to edit meta tags and add text.

-   The \<title> tag must match the content of the page and include the main search queries, must include no more than 64 words.

-   The \<description> meta tag should be a brief and precise description of the content of the page, and should not be the same as the \<title> tag.
