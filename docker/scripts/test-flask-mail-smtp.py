import argparse, sys
from pybossa.core import create_app
from flask_mail import Mail
from flask_mail import Message


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', '--from', dest='sender')
    arg_parser.add_argument('-t', '--to')
    args = arg_parser.parse_args()

    sender = "info@pybossa.com"
    recipient = "info@pybossa.com"
    if args.sender:
        sender = args.sender
    if args.to:
        recipient = args.to

    # next line is how to properly load PYBOSSA_SETTINGS=settings_from_env.py
    app = create_app(run_as_server=False)
    mail = Mail(app)

    with app.app_context():
        msg = Message("Hello", sender=sender, recipients=[recipient])
        msg.body = "Hi, This is a test to see if Flask-Mail is able to send mail."
        mail.send(msg)

    print "Sent From: {} To: {}".format(sender, recipient)
