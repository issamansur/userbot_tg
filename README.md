# What is it?
Create a script for the user who calls the participants. Without the server! Unlike the usual bot, the user’s script is executed from the account of a real person, for example - from your account.
For use it is necessary: 
- Internet connection; 
- Account telegram (number + code); 
- Python (+ Pip); 
- Telethon, asyncio and other libraries.

# What to do first?
<h3>1. Install libraries: Telethon and asyncio.</h3>

pip install telethon

![изображение](https://user-images.githubusercontent.com/77580844/133887874-d0ba39c4-b1c9-4ade-bd60-ebe83292e892.png)

pip install asyncio

![изображение](https://user-images.githubusercontent.com/77580844/133887917-15d0c612-6333-408f-ba25-a418d1005c21.png)

<h3>2. Get data for the application.</h3>
Go to https://my.telegram.org/auth and login in system. Then choose "API development tools"

![изображение](https://user-images.githubusercontent.com/77580844/133888361-98520b22-2a37-47a5-9015-5ee710a7c8a3.png)

Fill in all the fields on the page (you don’t have to fill url and description) and click "Create application"
Copy and paste api_id and api_hash in file "config.ini" to folder of project as shown in figure.

Add name of group (where we will call participants)

<h3>3. All is ready!</h3>
