<<<<<<< HEAD
import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','yourpassword')
mail.inbox()
print(mail.unread())
=======
from O365 import Account
credentials = ('my_client_id', 'my_client_secret')
account = Account(credentials, auth_flow_type='credentials', tenant_id='my-tenant-id')
print()
>>>>>>> 7233963f4ee650a19db3a76b1c7570a246faabed
