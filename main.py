# This is a simple script that calls an API and checks if a password has been violated or not!!
import requests
import hashlib  # is a Python library that allow to hash data

usr_input = input('Please insert your password: ')


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f'Error Fetching: {response.status_code}, check the API and try again')
    print(response)
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1_password[:5], sha1_password[5:]
    print(f'sh1 password: {sha1_password}')
    print(f'first 5 characters: {head}')
    print(f'tail of the string: {tail}')
    print('I an calling tha APi...')
    result = request_api_data(head)
    return get_password_leaks_count(result, tail)


def main(inp):
    count = pwned_api_check(inp)
    if count:
        print(f'{inp} has been hacked {count} times!')
    else:
        print(f'{inp} was NOT found. You are secure for now!')


if __name__ == "__main__":
    main(usr_input)
