import pywhatkit as kit
import datetime

# Número de telefone no formato: +55DDDNUMERO
numero = "+5561984220205"

# Mensagem que o bot vai enviar
mensagem = "Olá! Esse é um bot do Pedro testando automação no WhatsApp 😎"

# Pega a hora atual e adiciona 1 minuto para dar tempo de abrir o navegador
agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute + 1

# Envia a mensagem
kit.sendwhatmsg(numero, mensagem, hora, minuto)

print("Mensagem agendada com sucesso!")



