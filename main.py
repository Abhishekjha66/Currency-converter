import requests

def convert_curr():
    init_currency = input("Enter the initial currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()

    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                print('Amount needs to be greater than 0')
            else:
                break
        except ValueError:
            print('The amount needs to be numeric')

    api_key = "K8Pe9tKIlEJQAcX16IdJWXqBsWi0aF4Z"

    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    headers= {"apikey": api_key}

    response = requests.get(url, headers=headers)

    status_code = response.status_code

    if status_code != 200:
        print('Error:', response.text)
        return

    result = response.json()

    print('Conversion Result:', result['result'])

if __name__ == '__main__':
    convert_curr()
