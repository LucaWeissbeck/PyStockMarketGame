import requests

BASE_URL = "http://localhost:8080/api/"

def login(user_name_input: str, password_input: str) -> requests.Response:
        json = {'email': user_name_input,
            'password': password_input}

        return requests.post(BASE_URL + "user/login", json=json)

def register(first_name: str, name: str, mail: str, password: str, start_capital: float):
        json = {'firstName': first_name,
                'lastName': name,
                'email': mail,
                'password': password,
                'startingCapital': start_capital,
                'moneyAvailable': start_capital }

        return requests.post(BASE_URL + "user", json=json)

def get_first_name(auth_key: str) -> str:
        return requests.get(BASE_URL + "user", headers={"api_key":auth_key}).json()["firstName"]

def get_stock_names(auth_key: str) -> requests.Response:
        return requests.get(BASE_URL + "stock", headers={"api_key":auth_key})

def post_transaction(auth_key: str, symbol: str, amount : int, transactionType : str):
        json = {'symbol': symbol,
                "amount": amount,
                "transactionType": transactionType }

        return requests.post(BASE_URL + "portfolio/transaction", headers={"api_key":auth_key}, json = json)

def get_stock_description(auth_key: str, symbol: str):
        return requests.get(BASE_URL + f"stock/{symbol}/description", headers={"api_key":auth_key}).json()