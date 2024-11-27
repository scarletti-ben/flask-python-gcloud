The README below is primarily me learning how to deploy flask app via cmd / powershell on windows. In future I may clean it up, or make it more useful.

- Virtual environments
python -m venv env
then type env and hit tab, it will say PS E:\Documents\Scripts\HTML\venvA01> .\env\
do PS E:\Documents\Scripts\HTML\venvA01> .\env\Scripts\activate

may need 
PS E:\Documents\Scripts\HTML\venvA01> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS E:\Documents\Scripts\HTML\venvA01> .\env\Scripts\activate

- Flask is a mixed library used to get other libraries to help you run a web server

- For deployment you want to pass secret keys for databases or integrations like google sign up, so you need to pip install pythojn-dotenv so you can pass variables to your app on deployment. Then make .env file next to app.py

- Calling an API uses CORS (cross-origin), so import Flas-CORS, it's a web standard to make sure you're passing correct headers to the backend and the API, reduces chance of middleman attack

- gunicorn is production code for the flask app to deploy through

- Use pip freeze > requirements.txt to freeze the current requirements for the virtual environment in terms of imports, on deployment the google server needs this to know what to install

- Use pip list to check current installed packages

- You need app.yaml, runtime: python39 is python 3.9, google needs the yaml file to deploy

- Need google cli installer from https://cloud.google.com/sdk/docs/install, this will install a version of python 3.9 that google is using
    - Run gcloud init after checking with gcloud help

- After this add a dockerfile

- gunicorn is a tool where when you deploy on cloud you are using a cpu, the cpu has cores and you can limit the server to only use one or two cores for instance to save resources

- You also want a .dockerignore file to tell it to ignore things, such as compiled python code caches etc

- Ensure you are running via project id and not project number before running: gcloud run deploy --source .

- You will be asked to name the service
- You may be asked to enable some apis
- You will be asked what server you want to host on, chosen a western europe one
- You will be asked to allow unautheticated invocations, for testing maybe do yes, in production probably no
- MAKE SURE DOCKERFILE called Dockerfile

Building using Dockerfile and deploying container to Cloud Run service [cloud-test] in project [virtual-XXX-XXX-XX] region [europe-west1]
OK Building and deploying new service... Done.
  OK Uploading sources...
  OK Building Container... Logs are available at [...].
  OK Creating Revision...
  OK Routing traffic...
  OK Setting IAM Policy...
Done.
Service [cloud-test] revision [...] has been deployed and is serving 100 percent of traffic.
Service URL: https://cloud-test-XXX.europe-west1.run.app

- You will deploy, and can see access in the google cloud dashboard and in the cloud run list of services
- Best to delete the service after testing
