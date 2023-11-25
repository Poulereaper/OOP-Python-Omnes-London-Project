import os 
from email.message import EmailMessage
import ssl
import smtplib

def send_email_bis(Mail, Name, Outbound_Flight_B, Inbound_Flight_B, Basket_Total_Price):
    email_sender = "oop.air.line@gmail.com"
    email_password = "hrkx jmpw yskb zbgf"
    email_receiver = Mail
    # HTML Content
    if Inbound_Flight_B == None:
        body=("""Dear """+Name+""",\n Thank you for your order.\n Below is a summary of your order:\n Item\tDeparture\tArrival\tPassengers\tPrice\n Outbound\t"""+str(Outbound_Flight_B.Departure_Airport)+"""\t"""+str(Outbound_Flight_B.Arrival_Airport)+"\t"+str(Outbound_Flight_B.Passengers)+"\t£"+str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount)+" for Adulte\n Total Price: £"+str(Basket_Total_Price)+"\n Thank you for choosing OOP Air Line.\n Best regards,\n OOP Air Line""")
    else:
        body=("""Dear """+Name+""",\n Thank you for your order.\n Below is a summary of your order:\n Item\tDeparture\tArrival\tPassengers\tPrice\n Outbound\t"""+str(Outbound_Flight_B.Departure_Airport)+"""\t"""+str(Outbound_Flight_B.Arrival_Airport)+"\t"+str(Outbound_Flight_B.Passengers)+"\t£"+str(Outbound_Flight_B.Passengers*Outbound_Flight_B.Discount)+" for Adulte\n Inbound\t"+str(Inbound_Flight_B.Departure_Airport)+"""\t"""+str(Inbound_Flight_B.Arrival_Airport)+"\t"+str(Inbound_Flight_B.Passengers)+"\t£"+str(Inbound_Flight_B.Passengers*Inbound_Flight_B.Discount)+" for Adulte\n Total Price: £"+str(Basket_Total_Price)+"\n Thank you for choosing OOP Air Line.\n Best regards,\n OOP Air Line""")

    em = EmailMessage()
    em['Subject'] = "Order Confirmation"
    em['From'] = email_sender
    em['To'] = email_receiver
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email Sent")


def send_email(Mail, Name, Outbound_Flight_B, Inbound_Flight_B, Basket_Total_Price):
    email_sender = "oop.air.line@gmail.com"
    email_password = "hrkx jmpw yskb zbgf"
    email_receiver = Mail

    em = EmailMessage()
    em['Subject'] = "Order Confirmation"
    em['From'] = email_sender
    em['To'] = email_receiver
     # HTML Content
    if Inbound_Flight_B == None:
        html_content=f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Order Confirmation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #fff7ea;
                    color: #722a39;
                }}

                h1 {{
                    color: #722a39;
                }}

                p {{
                    margin-bottom: 10px;
                }}

                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                    margin-bottom: 20px;
                }}

                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}

                th {{
                    background-color: #722a39;
                    color: white;
                }}

                .total {{
                    font-weight: bold;
                    font-size: 1.2em;
                    color: #722a39;
                }}

                .thank-you {{
                    margin-top: 20px;
                    font-style: italic;
                    color: #722a39;
                }}

                .best-regards {{
                    margin-top: 20px;
                }}

                .policy-section {{
                    margin-top: 30px;
                }}
            </style>
        </head>
        <body>
            <h1>Order Confirmation</h1>
            <p>Dear {Name},</p>
            <p>Thank you for your order. Below is a summary of your order:</p>
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
                    <td>{str(Outbound_Flight_B.Departure_Airport)}</td>
                    <td>{str(Outbound_Flight_B.Arrival_Airport)}</td>
                    <td>{str(Outbound_Flight_B.Passengers)}</td>
                    <td>£{str(Outbound_Flight_B.Price)} for Adulte</td>
                </tr>
            </table>
            <p class="total">Total Price: £{str(Basket_Total_Price)}</p>
            <p class="thank-you">Thank you for choosing OOP Air Line.</p>
            <div class="policy-section">
                <h2>Privacy Policy</h2>
                <p>Your privacy is important to us. We will handle your personal information securely and responsibly. For more details, please refer to our <a href="#">Privacy Policy</a>.</p>
                <h2>Insurance Information</h2>
                <p>All tickets purchased through OOP Air Line come with insurance coverage. In case of any unforeseen circumstances, your ticket is protected. For more details, please refer to our <a href="#">Insurance Policy</a>.</p>
            </div>
            <p class="best-regards">Best regards,<br>OOP Air Line</p>
        </body>
        </html>
        """
    else:
        html_content=f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Order Confirmation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #fff7ea;
                    color: #722a39;
                }}

                h1 {{
                    color: #722a39;
                }}

                p {{
                    margin-bottom: 10px;
                }}

                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                    margin-bottom: 20px;
                }}

                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}

                th {{
                    background-color: #722a39;
                    color: white;
                }}

                .total {{
                    font-weight: bold;
                    font-size: 1.2em;
                    color: #722a39;
                }}

                .thank-you {{
                    margin-top: 20px;
                    font-style: italic;
                    color: #722a39;
                }}

                .best-regards {{
                    margin-top: 20px;
                }}

                .policy-section {{
                    margin-top: 30px;
                }}
            </style>
        </head>
        <body>
            <h1>Order Confirmation</h1>
            <p>Dear {Name},</p>
            <p>Thank you for your order. Below is a summary of your order:</p>
            <table>
                <tr>
                    <th>Item</th>
                    <th>Departure</th>
                    <th>Arrival</th>
                    <th>Passengers</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <td>Inbound</td>
                    <td>{str(Outbound_Flight_B.Departure_Airport)}</td>
                    <td>{str(Outbound_Flight_B.Arrival_Airport)}</td>
                    <td>{str(Outbound_Flight_B.Passengers)}</td>
                    <td>£{str(Outbound_Flight_B.Price)} for Adulte</td>
                </tr>
                <tr>
                    <td>Outbound</td>
                    <td>{str(Inbound_Flight_B.Departure_Airport)}</td>
                    <td>{str(Inbound_Flight_B.Arrival_Airport)}</td>
                    <td>{str(Inbound_Flight_B.Passengers)}</td>
                    <td>£{str(Inbound_Flight_B.Price)} for Adulte</td>
                </tr>
            </table>
            <p class="total">Total Price: £{str(Basket_Total_Price)}</p>
            <p class="thank-you">Thank you for choosing OOP Air Line.</p>
            <div class="policy-section">
                <h2>Privacy Policy</h2>
                <p>Your privacy is important to us. We will handle your personal information securely and responsibly. For more details, please refer to our <a href="#">Privacy Policy</a>.</p>
                <h2>Insurance Information</h2>
                <p>All tickets purchased through OOP Air Line come with insurance coverage. In case of any unforeseen circumstances, your ticket is protected. For more details, please refer to our <a href="#">Insurance Policy</a>.</p>
            </div>
            <p class="best-regards">Best regards,<br>OOP Air Line</p>
        </body>
        </html>
        """

    em.add_alternative(html_content, subtype='html', charset='utf-8')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email Sent")
