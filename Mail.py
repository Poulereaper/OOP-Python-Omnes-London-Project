import os 
from email.message import EmailMessage
import ssl
import smtplib

def send_email(Mail, Name, Outbound_Flight_B, Inbound_Flight_B, Basket_Total_Price):
    email_sender = "oop.air.line@gmail.com"
    email_password = "hrkx jmpw yskb zbgf"
    email_receiver = Mail
    # HTML Content
    if Inbound_Flight_B == None:
        #body=("""Dear """+Name+""",\n Thank you for your order.\n Below is a summary of your order:\n Item\tDeparture\tArrival\tPassengers\tPrice\n Outbound\t"""+str(Outbound_Flight_B.Departure_Airport)+"""\t"""+str(Outbound_Flight_B.Arrival_Airport)+"\t"+str(Outbound_Flight_B.Passengers)+"\t£"+str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount)+" for Adulte\n Total Price: £"+str(Basket_Total_Price)+"\n Thank you for choosing OOP Air Line.\n Best regards,\n OOP Air Line""")
        body = """
        Hello
        """
    else:
        #body=("""Dear """+Name+""",\n Thank you for your order.\n Below is a summary of your order:\n Item\tDeparture\tArrival\tPassengers\tPrice\n Outbound\t"""+str(Outbound_Flight_B.Departure_Airport)+"""\t"""+str(Outbound_Flight_B.Arrival_Airport)+"\t"+str(Outbound_Flight_B.Passengers)+"\t£"+str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount)+" for Adulte\n Inbound\t"+str(Inbound_Flight_B.Departure_Airport)+"""\t"""+str(Inbound_Flight_B.Arrival_Airport)+"\t"+str(Inbound_Flight_B.Passengers)+"\t£"+str(Inbound_Flight_B.Passengers*Inbound_Flight_B.Discount)+" for Adulte\n Total Price: £"+str(Basket_Total_Price)+"\n Thank you for choosing OOP Air Line.\n Best regards,\n OOP Air Line""")
        body = """
        Hello deux 
        """

    em = EmailMessage()
    em['Subject'] = "Order Confirmation"
    em['From'] = email_sender
    em['To'] = email_receiver
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string)
        print("Email Sent")



def send_email_bis(Mail, Name, Outbound_Flight_B, Inbound_Flight_B, Basket_Total_Price):
    email_sender = "oop.air.line@gmail.com"
    email_password = "hrkx jmpw yskb zbgf"
    email_receiver = Mail

    em = EmailMessage()
    em['Subject'] = "Order Confirmation"
    em['From'] = email_sender
    em['To'] = email_receiver
     # HTML Content
    if Inbound_Flight_B == None:
        html_content="""
        <html>
        <head></head>
        <body>
            <p>Dear """, Name, """,</p>
            <p>Thank you for your order. </p>
            <p>Below is a summary of your order:</p>
            <table>
                <tr>
                    <th>Item</th>
                    <th>Departure</th>
                    <th>Arrival</th>
                    <th>Passengers</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <td>Outbound</td>
                    <td>""", str(Outbound_Flight_B.Departure_Airport), """</td>
                    <td>""", str(Outbound_Flight_B.Arrival_Airport), """</td>
                    <td>""", str(Outbound_Flight_B.Passengers), """</td>
                    <td>£""", str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount),""" for Adulte </td>
                </tr>
            </table>
            </br>
            <p>Total Price: £""", str(Basket_Total_Price), """</p>
            </br>
            </br>
            <p>Thank you for choosing OOP Air Line.</p>
            </br>
            <p>Best regards,<br>OOP Air Line</p>
        </body>
        </html>
        """
    else:
        html_content="""
        <html>
        <head></head>
        <body>
            <p>Dear """, Name, """,</p>
            <p>Thank you for your order. </p>
            <p>Below is a summary of your order:</p>
            <table>
                <tr>
                    <th>Item</th>
                    <th>Departure</th>
                    <th>Arrival</th>
                    <th>Passengers</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <td>Outbound</td>
                    <td>""", str(Outbound_Flight_B.Departure_Airport), """</td>
                    <td>""", str(Outbound_Flight_B.Arrival_Airport), """</td>
                    <td>""", str(Outbound_Flight_B.Passengers), """</td>
                    <td>£""", str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount),""" for Adulte </td>
                </tr>
                <tr>
                    <td>Inbound</td>
                    <td>""", str(Inbound_Flight_B.Departure_Airport), """</td>
                    <td>""", str(Inbound_Flight_B.Arrival_Airport), """</td>
                    <td>""", str(Inbound_Flight_B.Passengers), """</td>
                    <td>£""", str(Inbound_Flight_B.Passengers*Inbound_Flight_B.Discount),""" for Adulte </td>
                </tr>
            </table>
            </br>
            <p>Total Price: £""", str(Basket_Total_Price), """</p>
            </br>
            </br>
            <p>Thank you for choosing OOP Air Line.</p>
            </br>
            <p>Best regards,<br>OOP Air Line</p>
        </body>
        </html>
        """

    em.add_alternative(html_content, subtype='html', charset='utf-8')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string)
        print("Email Sent")
