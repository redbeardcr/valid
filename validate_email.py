import re
import smtplib
import dns.resolver


def checkmail(mail):
    code = 123
    message = 'start'
    # Address used for SMTP MAIL FROM command
    fromAddress = 'test@test.com'

    # Simple Regex for syntax checking
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

    # Email address to verify
    inputAddress = mail
    addressToVerify = str(inputAddress)

    # Syntax check
    match = re.match(regex, addressToVerify)
    if match is None:
        # print('Bad Syntax')
        # raise ValueError('Bad Syntax')
        code = 999
        message = 'Bad Syntax'
        return code, message
        raise ValueError('Bad Syntax')

    # Get domain for DNS lookup
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
    # print('Domain:', domain)

    # MX record lookup
    try:
        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

    except:
        code = 998
        message = 'Something went wrong with the MX record lookup'
        return code, message

    try:
        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP(timeout=5)
        server.set_debuglevel(1)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(server.local_hostname)  ### server.local_hostname(Get local server hostname)
        server.mail(fromAddress)
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
        # try:
        #    server.quit()
        # except:
        #    print(message)

        # return code, message
    except:
        code = 999
        message = "something towards the end broke"

    return code, message
    # print(message)

    # Assume SMTP response 250 is success
    # if code == 250:
    # print('Success')
    # else:
    # print('Bad')
