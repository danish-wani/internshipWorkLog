import re

def fun(s):

    
    if len(s) > 0:
        if ( '@' in s and '.' in s):
            print(' @ and . found')
            if (s.count('@') == 1 and s.count('.') == 1):
                print('at most 1 each @ and . ')
                extensionLen = len(s[s.rfind('.')+1:len(s)])
                print('extension length',extensionLen)
                if(extensionLen  > 0 and extensionLen <= 3):
                    website = s[s.index('@') + 1:s.index('.')]
                    if(website.isalnum()):
                        print('website name is valid')
                        username = s[0:s.index('@')]
                        print(username)
                        p = re.compile('[^a-zA-Z0-9\-_]')
                        if p.search(username) == None:
                           return True 






def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
