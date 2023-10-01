# by-the-sea

# create .env file at root directory
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=bts_db_mysql
MYSQL_USER=bts_user
MYSQL_PASSWORD=bts_password
PHPADMIN_HOST=bts_db_mysql
PHPADMIN_USER=bts_user
PHPADMIN_PASSWORD=bts_password
OPENAI_API_KEY= ***own open ai api key***

# Go to server directory
python3 -m venv venv
source venv/bin/activate #For windows: venv\Scripts\activate.bat
pip install -r requirements.txt

# Exit virtual environment by using a new terminal

# Go to Root directory
# Run Docker

First build the image:
docker-compose build

When ready, run it:
docker-compose up

Close docker
docker-compose down -v


# If want to run frontend locally
client directory
npm install
npm run dev
