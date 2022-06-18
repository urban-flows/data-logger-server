
from email.mime.text import MIMEText
import smtplib

def send_email(filename, login):
    
    """
    Parameters
    ----------
    filename : textfile with the message to be sent
    login : textfile containing login detail; first line must have the username and second line must contain the password
    Returns
    -------
    None.

    """
    
    login = "name of .txt file containing the login details"
    filename = "name of .txt file containing the message to be sent"
    
    with open(filename, 'r') as fp:
    # Create a  message
        msg = MIMEText(fp.read())
        
    with open(login) as f:
    # dictionary comprehension to create dictionary containing user and password
        login_dict = dict(line.rstrip().split(":") for line in f)
        

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()  # identify ourselves to smtp gmail client
    s.starttls()  # secure our email with tls encryption
    s.ehlo()  # identify ourselves to smtp gmail client

    s.login(login_dict['username'], login_dict['password'])
    s.sendmail("email address to send from", ["email address to send to","email address to send to"], msg.as_string())
    s.quit()
    

if __name__ == "__main__":

    # Send the message via  SMTP server
    send_email("name of .txt file containing the message to be sent", "name of .txt file containing the login details")

    

    
   


