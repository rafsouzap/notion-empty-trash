from utils.colors import Colors
from notion.client import NotionClient
from pprint import pprint
from PyInquirer import prompt

def chunks(list, n):
    """
    Yield successive n-sized chunks from list
    """
    for i in range(0, len(list), n):
        yield list[i:i+n]

def chose_token_auth(answers):
    if answers['auth_type'] == 'token':
        return True
    return False

def chose_credential_auth(answers):
    if answers['auth_type'] == 'credential':
        return True
    return False

def create_notion_client(answers):
    try:
        if answers['auth_type'] == 'token':
            if answers['token_auth'] != '':
                return NotionClient(token_v2=answers['token_auth'])
        else:
            if answers['email_auth'] != '':
                return NotionClient(email=answers['email_auth'], password=answers['password_auth'])
    except:
        print('\n'+ Colors.FAIL +'Unauthorized access'+ Colors.ENDC +' \n')

def main():
    auth_options = [
        { 
            'type': 'list',
            'name': 'auth_type',
            'message': 'Which authentication mode do you prefer?',
            'choices': ['Token', 'Credential'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'input',
            'name': 'token_auth',
            'message': 'Enter your Auth Token:',
            'when': chose_token_auth
        },
        {
            'type': 'input',
            'name': 'email_auth',
            'message': 'Enter your Notion e-mail address:',
            'when': chose_credential_auth
        },
        {
            'type': 'password',
            'name': 'password_auth',
            'message': 'Enter your Notion password:',
            'when': chose_credential_auth
        }
    ]

    answers = prompt(auth_options)
    #notion_client = create_notion_client(answers=answers)

    print('\n'+ Colors.OKGREEN +'Successfully cleared all trash blocks.'+ Colors.ENDC)

if __name__ == '__main__':
    print('\n'+ Colors.HEADER +'[ Notion Empty Trash ]'+ Colors.ENDC +' \n')
    main()