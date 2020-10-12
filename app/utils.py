from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        EmailMessage(data['subject'], data['domain'], 'emailverification@test.com', [data['recipient_list']], False)
        print('messages sent:  ' + str(data))
