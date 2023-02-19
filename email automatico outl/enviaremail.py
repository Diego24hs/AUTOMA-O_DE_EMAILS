import win32com.client as win32


outlook= win32.Dispatch('outlook.application')


email= outlook.CreateItem(0)

email.To= 'suka_suelen2006@hotmail.com'
email.subject= 'e-mail automatico do Python'
email.HTMLBody= ''' 
<p>Oi Amor!!</p> 

<p>Só estou enviando esse e-mail, para poder fazer um teste</p>
<p>para ver se chega certinho</p> 
<p>obrigado pela compreenção</p> 
<p> Te amo muito e um otimo dia!!</p>

<p>!!!Minha Linda!!</p> 
'''
email.Send()
