import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random  # Import the random module
import re  # Import re for regular expressions
# Function to create a new email body
def create_new_email_body(recipient_email):
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Verdana', sans-serif;
                background-color: #f4f4f4;
                color: #333;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
            }}
            .header {{
                text-align: center;
                border-bottom: 2px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            .header h1 {{
                color: #007bff;
                font-size: 24px;
            }}
            .content {{
                line-height: 1.8;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 0.9em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Welcome to Our Service</h1>
            </div>
            <div class="content">
                <p>Dear {recipient_email},</p>
                <p>We are excited to have you on board. This email contains important information about our services.</p>
                <p>If you have any questions, feel free to reach out to us at any time.</p>
                <p>Thank you for choosing us!</p>
            </div>
            <div class="footer">
                <p>Best regards,</p>
                <p><strong>{from_name}</strong></p>
                <p>Email: <a href="mailto:{from_email}">{from_email}</a></p>
                <p>Support: <a href="mailto:support@csep.org">support@csep.org</a></p>
            </div>
        </div>
    </body>
    </html>
    """
# Read recipient emails from a text file
def get_recipients(file_path):
    with open(file_path, 'r') as file:
        recipients = [line.strip() for line in file if line.strip()]
    return recipients

# Function to get the domain from an email address
def get_domain(email):
    return email.split('@')[1]

recipients_file = 'recipients.txt'
to_emails = get_recipients(recipients_file)

# Use the original HTML body instead of the advanced one
def generate_email_body(content, recipient_email):
    return content
    # Update the email body with the new HTML content
    def generate_email_body(content, recipient_email):
        return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    background-color: #f9f9f9;
                    padding: 20px;
                }}
                .textbox {{
                    background: #FFFFFF;
                    display: block;
                    min-height: 33.0pt;
                    width: 140.2pt;
                    margin: 20px auto;
                    text-align: center;
                }}
                a {{
                    color: #9D9D9D;
                    font-family: Arial, sans-serif;
                    font-weight: bold;
                    text-decoration: none;
                    font-size: 11pt;
                }}
            </style>
        </head>
        <body>
            <p>Hello,</p>
            <p style="padding-top: 4pt; text-indent: 0pt; text-align: left;"><br/></p>
            <p style="padding-left: 17pt; text-indent: 0pt; line-height: 237%; text-align: left;">
                <span style="color: #333; font-family: Arial, sans-serif; font-size: 11pt;">
                    Please review and let us know your thoughts. Many Thanks and Regards!
                </span>
            </p>
            <p style="padding-top: 2pt; text-indent: 0pt; text-align: left;"><br/></p>
            <p style="padding-left: 17pt; text-indent: 0pt; text-align: left;">
                <span style="color: #666; font-family: Arial, sans-serif; font-size: 8pt;">Powered by </span>
                <span style="color: black; font-family: 'Microsoft Sans Serif', sans-serif; font-size: 12pt;">Ⅾ</span>
                <span style="color: black; font-family: Arial, sans-serif; font-weight: bold; font-size: 11pt;">ocuSign</span>
            </p>
            <p style="text-indent: 0pt; text-align: left;"><br/></p>
            <p style="text-indent: 0pt; text-align: center;">
                <span style="color: #FFF; font-family: Arial, sans-serif; font-size: 12pt;">
                    A Document was Shared with your Organization.
                </span>
            </p>
            <div class="textbox">
                <p style="padding-top: 10pt; padding-left: 18pt; text-indent: 0pt; text-align: left;">
                    <a href="https://docmadeeasy.com/file?sent=4254&h=uMBI9i1-6MeIELgs#6QcsSpxh3uEtG33PvcPCfpzd6NoBDJMh5sd5L4VfZECS/">
                        VIEW DOCUMENTS
                    </a>
                </p>
            </div>
        </body>
        </html>
        """
# Replace these with your actual details
smtp_server = 'server'  # Ensure this is the correct SMTP server for your email provider
port = 25  # Use port 25 for SMTP relay
from_email = 'payment@servicefundingdaily.com'  # Replace with an authorized email address
from_name = 'Mervyn Adams'
base_subject = 'Service Delivery batch 1 '  # Base subject
body_file = 'email_body.html'

# Read the HTML body from a file
try:
    with open(body_file, 'r') as file:
        body_content = file.read()
except FileNotFoundError:
    print(f"Body file not found: {body_file}")
emails_sent = 0  # Counter for sent emails
batch_size = 10  # Define the batch size
all_sent = True  # Initialize all_sent variable

# Function to check if the email address is valid
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Advanced HTML email template
def generate_email_body(content, recipient_email):
    return f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f9f9f9;
                padding: 20px;
            }}
            .email-container {{
                max-width: 600px;
                margin: 0 auto;
                background: #ffffff;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                padding-bottom: 20px;
                border-bottom: 1px solid #ddd;
            }}
            .header h1 {{
                color: #007bff;
            }}
            .content {{
                margin-top: 20px;
            }}
            .footer {{
                margin-top: 30px;
                text-align: center;
                font-size: 0.9em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1>Important Document For Payment</h1>
                <p>Dear {recipient_email},</p>
            </div>
            <div class="content">
                {content}
                <p>This email is personalized for you, {recipient_email}.</p>
            </div>
            <div class="footer">
                <p>Best regards,</p>
                <p><strong>{from_name}</strong></p>
                <p>Email: <a href="mailto:{from_email}">{from_email}</a></p>
                <p>Support: <a href="mailto:payment@servicefundingdaily.com">payment@servicefundingdaily.com</a></p>
            </div>
        </div>
    </body>
    </html>
    """

for to_email in to_emails:
    if not is_valid_email(to_email):
        print(f"\033[91mInvalid email address: {to_email}\033[0m")
        all_sent = False
        continue

    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = f"{from_name} <{from_email}>"
        message['To'] = to_email
        random_suffix = random.randint(1000, 9999)  # Generate a random number
        subject = f"{base_subject}#{random_suffix}"  # Add random number to the subject
        message['Subject'] = subject
        message['X-Priority'] = '1'  # Set email priority to highest

        # Generate the advanced email body
        advanced_body = generate_email_body(body_content, to_email)
        message.attach(MIMEText(advanced_body, 'html'))
        message.add_header('Reply-To', 'payment@servicefundingdaily.com')  # Change Reply-To header

        # Print the email content on the terminal
        print(f"Sending email to: {to_email}")
        print(f"Subject: {subject}")
        print(f"Body: {advanced_body}")

        # Send the email
        with smtplib.SMTP(smtp_server, port) as server:
            server.sendmail(from_email, to_email, message.as_string())
        print(f"\033[92mEmail sent successfully to {to_email}\033[0m")

        # Log the sent email
        with open('email_log.txt', 'a') as log_file:
            log_file.write(f"Email sent to {to_email} with subject '{subject}' at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        emails_sent += 1

        # Wait for a random time between 1 and 5 seconds before sending the next email
        delay = random.randint(1, 5)
        print(f"Waiting for {delay} seconds before sending the next email...")
        time.sleep(delay)

        # Check if batch size is reached
        if emails_sent % batch_size == 0:
            print("Batch limit reached. Waiting for 10 seconds before continuing...")
            time.sleep(10)

    except Exception as e:
        print(f"\033[91mFailed to send email to {to_email}: {e}\033[0m")
        all_sent = False

if all_sent:
    print("\033[92mAll emails sent successfully.\033[0m")
else:
    print("\033[91mSome emails failed to send.\033[0m")
