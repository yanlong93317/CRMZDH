import os

Host = "http://192.168.1.179"

BASE_PATH = os.path.dirname(__file__).strip("config")
REPORT_PATH = os.path.join(BASE_PATH, 'report')
CASS_PATH = os.path.join(BASE_PATH, 'cases')
DATAS_PATH = os.path.join(BASE_PATH, 'datas')
