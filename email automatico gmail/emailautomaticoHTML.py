import smtplib # permite enviar um email para o outro g mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# todas as bibliotecas para envio de email

#variaveis
fromaddr = "diego24hs@gmail.com"
toaddr = "diego_and.1@hotmail.com"

#variavel mensagem
msg = MIMEMultipart()

#quem esta enviando
msg['From'] = fromaddr

#quem esta recebendo
msg['To']= toaddr

#titulo da mensagem asunto
msg['Subject']='Venha aprender Python'

#fazendo um script em HTML body e o corpo do email p e o paragrafo br serve para pular linha
#para enviar link <a href=
html= """ 
<html>
    <body>
        <p>oi,<br>
        estou aqui mas uma ves para te convidar a vir aprender python<br>
        estamos aprendendo a colocar link de videos no e-mail<br>
        <a href="https://www.youtube.com/watch?v=rm0GYoZOFwo">Clique Aqui!!</a>
        para assistir esse clipe maguinifico.
             
       
        
        
        
        </p>
    </body>
<html>
"""

part1 = MIMEText(html, "html")
msg.attach(part1)
#configurar a porta do gmail fazendo a variavel
s= smtplib.SMTP('smtp.gmail.com', 587)
#variavel de conecção segura
s.starttls()

#fazer loggin
s.login(fromaddr, 'pfvdfoxjuqybkzla')

#transformar tudo em string
text = msg.as_string()
#mostra para quem vai enviar
s.sendmail(fromaddr, toaddr, text)

#fechar a coneccao com o email
s.quit()




