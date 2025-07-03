HOW TO FIX AND USE THIS APP:

1. Unzip this file.
2. Go to https://render.com and create a new web service.
3. Connect your GitHub repo or upload this folder to GitHub.
4. Set your start command on Render to: gunicorn main:app
5. Make sure 'templates' folder is in the same location as main.py.
6. Set your build environment to Python 3 and add these environment variables:
   - WEB_CONCURRENCY = 1
7. Click Deploy. Your app will auto-run and show a login page.

Default login:
  Username: calvin
  Password: 1234