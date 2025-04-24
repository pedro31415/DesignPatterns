class EmailAntigo:
    def enviar_email_antigo(self, mensagem):
        print(mensagem)

class EmailService:
    def enviar_mensagem_com_assunto(self, assunto, mensagem):
        print(assunto, mensagem)

class EmailAdpter:
    def __init__(self, mensagemAntiga: EmailAntigo):
        self.mensagem = mensagemAntiga
    
    def enviar_mensagem(self, mensagemNova):
        self.mensagem.enviar_email_antigo(mensagemNova)

    def enviar_mensagem_assunto(self, mensagemNova, assunto):
        mensagem_formatada = f"Assunto: {assunto}, messagem: {mensagemNova}"
        self.mensagem.enviar_email_antigo(mensagem_formatada)

if __name__ == "__main__":

    mensagem = EmailAntigo()
    messagemAdpter = EmailAdpter(mensagem)
    messagem2 = EmailAntigo()
    mensagemAdpter2 = EmailAdpter(mensagem)
    mensagem3 = EmailService()
    
    mensagem3.enviar_mensagem_com_assunto("Design Patterns", "Aula de padrão de projeto")
    mensagemAdpter2.enviar_mensagem_assunto("Design Patterns", "Aula de padrões de projeto")
    messagemAdpter.enviar_mensagem("Este email é para dizer que eu aprendi adapter")
    messagem2.enviar_email_antigo("Este é um segundo email")


    
