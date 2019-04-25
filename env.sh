# This file sets the environment variables for the Superdesk virtual environment. Copy to server as /opt/superdesk/env.sh

MAIL_FROM=notify@thetriangle.org
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME=apikey
MAIL_PASSWORD=useApiKeyFromSendGrid #do not commit the api key to the repository
MAIL_DEFAULT_SENDER=notify@thetriangle.org
ADMINS=['']