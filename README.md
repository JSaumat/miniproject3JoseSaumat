# miniproject3JoseSaumat

### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 3


# Mini Project 3

## Description

This project will be using a combination of Flaskr, BootStrap, HTML, and CSS to create a mini website.

## Getting Started

First clone the repository into your preferred IDE. Make sure to also create a virtual environment for the project.

### Dependencies

Step 1: Install required packages using the requirements.txt file. Copy and paste the code below into the terminal.

```
pip install -r requirements.txt
```
Step 2: Initialize the SQL database. Copy and paste the code below into the terminal.

```
flask --app flaskr init-db 
```

### Executing program

Step 3: Run the program. Copy and paste the code below into the terminal.

```
flask --app flaskr run
```

Step 4: In your terminal you should now see a hyperlink with the address below. Click that link to launch website in browser.

```
http://127.0.0.1:5000
```

### Output

This website should first display a modal asking you to confirm your age. If you are older than 18, you are allowed through.
If you are under 18, it will redirect you to Google.com because this website contains trailers for R rated movies. The site
will then display my top 10 favorite movies. When you click on the image tiles, it should redirect you to a YouTube page that 
contains that movie's trailer. You can also read the about page which contains a brief description of the site along with credit
for TMDB's use of their API for the movie posters. Then finally a blog where the community can comment. In order to post, 
you must register. The site also contains a fully functional registration, log in, and log out page.

## Authors

Contributors names and contact info

- Jose Saumat
- Jason Zeller (via Tutorials)

## Acknowledgments

Inspiration, code snippets, etc.
* [Jason Zeller](https://www.youtube.com/watch?v=mLS4_r_0VnE)
* [Jason Zeller](https://www.youtube.com/watch?v=7ckzzrLdqZc)
* [Jason Zeller](https://www.youtube.com/watch?v=WuT-bi6ctjc)
* [Jason Zeller](https://www.youtube.com/watch?v=mqsUg5kCghE)
* [Jason Zeller](https://www.youtube.com/watch?v=Fk1BXTtCejQ)
* [Jason Zeller](https://www.youtube.com/watch?v=hgksEFTvvUs)

API and Package documentation
* [TMDB API](https://www.themoviedb.org/)
* [Flask](https://documenter.getpostman.com/view/4016432/the-dog-api/RW81vZ4Z#26bd3f92-dd58-4569-bc13-22fa76396fe8)
* [Jinja](https://jinja.palletsprojects.com/en/stable/)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [W3 Schools HTML](https://www.w3schools.com/html/default.asp)
* [W3 Schools CSS](https://www.w3schools.com/css/default.asp)