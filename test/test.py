# import os

# sonar_server = os.environ.get('SONARQUBE_URL', 'http://sonarqube.com')
# print(sonar_server)

from dotenv import load_dotenv

load_dotenv()
import os

x = os.getenv("SONARQUBE_URL")
print(x)