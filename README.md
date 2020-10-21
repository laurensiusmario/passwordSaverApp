# passwordSaverApp
Application (web and desktop app) for saving passwords securely.

Server : Python Flask, SQLAlchemy, Javascript
App : PyQt5

Guide :
1. Download TOTP Apps : freeTOTP
2. Install all the requirements in the virtual environment
3. Run the server locally
4. Run the desktop app
5. Create account/log in

Create account :
1. Input TOTP key into the TOTP Apps
2. Log in

Log in :
1. Input username and password
2. Input TOTP token from TOTP app, each token valid for 30 seconds.

App :
1. Input first data and encryption key
2. Then you can add, remove, view data using that key
3. User can also changes username, password, and encryption key
4. After finish using the app, log out from the account.
