import os

Host = "http://192.168.1.211/crm/index.php?m=user&a=login"

BASE_PATH = os.path.dirname(__file__).strip("config")
REPORT_PATH = os.path.join(BASE_PATH, 'report')
CASS_PATH = os.path.join(BASE_PATH, 'cases')
DATAS_PATH = os.path.join(BASE_PATH, 'datas')