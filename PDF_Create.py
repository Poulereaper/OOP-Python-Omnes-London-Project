import jinja2
import pdfkit
from datetime import datetime
import os

def bill_pdf(client_name, client_mail, Outbound, Inbound, Out_Price, In_Price, Res_ID):
    total = Out_Price + In_Price
    today_date = datetime.today().strftime("%d %b, %Y")
    month = datetime.today().strftime("%B")
    item1 = "Outbound"
    item2 = "Inbound"

    context = {'client_name': client_name, 'client_mail': client_mail,
               'today_date': today_date, 
                'Res_ID': Res_ID,
                'total': f'${total:.2f}', 'month': month,
                'item1': item1, 'subtotal1': f'${Out_Price:.2f}',
                'item2': item2, 'subtotal2': f'${In_Price:.2f}'
                }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'bill.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    output_pdf = 'bill/bill_'+str(Res_ID)+'.pdf'
    #css_path = os.path.join(os.path.dirname(__file__), 'bill.css')
    pdfkit.from_string(output_text, output_pdf, configuration=config, css="bill.css")
    

bill_pdf("Mathis GRAS", "trashcan.ma@gmail.com", None, None, 2500, 3000, 14)