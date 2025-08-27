# allaboutdjango

## Quick Start Locally on Linux / MacOS
### Clone the repo
Use `git` to clone the repo and `cd` into it.
```
git clone git@github.com:shcsed/allaboutdjango.git
cd allaboutdjango
```
### Weather API & Dot Env Files
#### Backend
To try out this project, firstly you need a free weather API key from [weatherapi.com](https://www.weatherapi.com/).

Copy `sample.env` to `.env` in the `allaboutdjango` directory.
```
cp allaboutdjango/sample.env allaboutdjango/.env
```

Put your weather API key in `allaboutdjango/.env`:
```
...
WEATHERAPI_KEY=your-api-key
```

#### Frontend
Copy `sample.env` to `.env` in the `fe` directory.
```
cp fe/sample.env fe/.env
```
### Install dependencies
#### Backend
Make sure [`uv`](https://docs.astral.sh/uv/#installation) is installed, and then run this command to install backend dependencies.
```
uv sync
```
#### Frontend
As for frontend, make sure `nodejs` and `npm` are installed and move into the `fe` directory and run the following command to install frontend dependencies.
```
npm i
```

### Run the servers
#### Backend
Make sure `GNU Make` is installed. For example, you can install `make` on Ubuntu or debian using this command.
```
sudo apt-get install make -y
```
Run this command to start a development server on port 8000.
```
make bedev
```
#### Frontend
Run this command to start a development server on port 3000.
```
make fedev
```

Now you are can navigate to `http://localhost:3000` to see the results.

### Access the admin dashboard
Move into the `allaboutdjango` directory where `manage.py` is located, and run the following command to create a super user account.
```
uv run manage.py createsuperuser
```
Now you are able to use the account to login on `http://localhost:8000/admin-dashboard/`

The `admin-dashboard` part of the url can be edited in the dotenv file (`allaboutdjango/.env`).

Now you can add devlogs and books using the admin dashboard. Then you can access `http://localhost:3000` again to see the results.
