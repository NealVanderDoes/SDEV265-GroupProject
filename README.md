# 1. What your project does
 This project is called ByteThyme, and it creates a blog-like website using the Django framework, which allows users to browse and upload small recipes. Users can create their account, upload a recipe, edit their existing recipes, and leave comments on other recipes. Posts can have a picture to depict what the food item should look like, as well as a list of ingredients required to make it. This project aimed to create a website where recipes could be shared and interacted with through a comment system.

# 2. How to install it
- Step 1: Download the files from https://github.com/shamrockdvpr/SDEV265-Project/tree/master


- Step 2: Open the files with your Python IDE and install the libraries in requirements.txt. (Tested with VSCode & PyCharm)


- Step 3: Migrate the database: in the terminal of your IDE type "python manage.py migrate". This syncs the database so you can make posts, comments, and an admin account.


- Step 4: Create an admin account in the terminal: Type "python manage.py createsuperuser" in the terminal. Now, inside the terminal, you will create an admin account. Read the terminal in case of problems.
		
  - Create your username

  - Enter an email (forced by Django, but emails aren't used)

  - Create a password (will NOT show anything being typed, this is normal. Type the password as normal and click enter)

  - Confirm password (will NOT show anything being typed, this is normal. Type the same password as before)


- Step 5: Confirm migrations: run the commands "python manage.py makemigrations" and "python makemigrations blog". Finally, run "python manage.py migrate" one last time to make sure all database migrations are applied.


- Step 6: Run the website: type "python manage.py runserver" in the terminal. This runs a copy of the website on your local machine. The URL is http://127.0.0.1:8000/ in your browser. The website should be empty as posts, comments, and account information are NOT uploaded to GitHub as db.sqlite3 is excluded in the .gitignore file.


- Step 7: Click the lock icon on the top right of the site and enter the username and password you just created. (This is also where you can create normal user accounts by clicking "signup").


- Step 8: The website should be working now. There will be no posts on your local machine on setup, as the database is not uploaded to GitHub. You can now create posts, with the + button in the top right if logged in.


- Step 9: Closing the program: Read the terminal on terminating the website. (Ctrl Pause/Break for PyCharm, Ctrl C for VSCode)


- Step 10: After terminating, to reboot the site, type "python manage.py runserver" in the terminal.

# 3. Example usage
- Login/Logout: Click the lock icon in the top right to log in to an existing account or create a new one. To log out, click "Logout" in the top right to the left of the account name when logged in.


- Creating a post: Open the website and click the "+" icon in the top right. This will take you to the post-creation page.


- Uploading a post: Fill out the various required boxes for a post and click "save." This will save your post as a draft until you click "publish." If you want to access your drafts, click the pencil icon to the left of the "+" icon in the top right. 


- Viewing a post: Access the homepage by clicking the "ByteThyme" wording in the top left. All posts should be viewable on this page. Alternatively, you can search for posts with the search bar by typing a search request and clicking "Search." This will bring up any posts if they match your search request.


- Leaving a comment: View a post and click "Add comment" located at the bottom of the recipe. Leave your desired name in the author section and write your comment in the textbox, then hit send. Your comment will NOT automatically show up; it has to be okayed by the admin account first. If the admin account clicks the checkmark button next to the comment, the comment will be visible to anyone.

# 4. Changelog
- Latest update: Added Search Bar feature and attaching a Picture to posts. (Credit to Amy for the Search Bar feature)
  - Switched to uv for dependency management.

- Previous update: Added Logout feature, and users can create non-admin accounts which allow them to create, edit, and delete their posts.

# 5. License and author info
Authors: Amy Jarvis, Charles Shaneck, Cristian Escobedo, Marcin Brodowicz, Neal Vander Does | Contact us through IvyTech emails if necessary.
License: Apache License Version 2.0, January 2004 http://www.apache.org/licenses/
