from flask import Flask
from dotenv import dotenv_values
import os

config = {
    **dotenv_values(".env"),  # load shared development variables
    **os.environ,  # override loaded values with environment variables
}

api = Flask(__name__)


@api.route('/', methods=['GET'])
def main_logic():
    return config.get('HelloMessage')


if __name__ == '__main__':
    # time.sleep(60)
    api.run(debug=False, host='0.0.0.0', port=8080)