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

#corpo do email
body = '''IAE vim aqui te convidar, a vir embarcar
na area de python e muito divertido e facil de aprender
varias ferramentas dahoras valew e te espero este e-mail 
é automatico com um simples codigo de automação inclusive
o anexo '''

#funçao para enviar o texto da variavel body
msg.attach(MIMEText(body, 'plain'))

#CODIGOS PARA O ANEXO
filename= 'Diego Alex Mineiro Bonilla curriculum 2023.pdf'
anexo= open("Diego Alex Mineiro Bonilla curriculum 2023.pdf", "rb")
p= MIMEBase("aplication", "octet-stream")
p.set_payload((anexo).read())
encoders.encode_base64(p)
p.add_header('content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)

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




