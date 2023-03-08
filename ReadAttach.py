import outlook
mail = outlook.Outlook()
mail.login('emailaccount@live.com','yourpassword')
mail.inbox()
print mail.unread()