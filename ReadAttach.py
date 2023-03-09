from O365 import Account
credentials = ('my_client_id', 'my_client_secret')
account = Account(credentials, auth_flow_type='credentials', tenant_id='my-tenant-id')
print()