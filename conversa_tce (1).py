import streamlit as st

def conversa_tce():
    st.title("Conversa sobre o Tribunal de Contas do Estado (TCE)")

    st.write("Olá! Vamos falar um pouco sobre o Tribunal de Contas do Estado.")

    st.write("Você está familiarizado com o Tribunal de Contas do Estado?")

    opcoes = ["Sim", "Não"]
    escolha = st.radio("Selecione uma opção:", opcoes)

    if escolha == "Sim":
        st.write("Ótimo! Então você já sabe sobre a importância do controle externo das contas públicas.")
    else:
        st.write("Sem problemas! O Tribunal de Contas do Estado é responsável por fiscalizar as contas públicas dos municípios e do próprio estado.")

    st.write("Você sabe qual é o papel principal do Tribunal de Contas do Estado?")

    papel_tce = st.text_input("Digite sua resposta aqui:")

    if papel_tce.lower() == "fiscalizar as contas públicas":
        st.write("Isso mesmo! Uma das funções principais do TCE é fiscalizar as contas públicas para garantir a transparência e o bom uso dos recursos.")
    else:
        st.write("Hmm, não é bem isso. O papel principal do TCE é fiscalizar as contas públicas para garantir a transparência e o bom uso dos recursos.")

    st.write("Você tem mais alguma pergunta sobre o Tribunal de Contas do Estado?")

    pergunta = st.text_input("Digite sua pergunta aqui:")

    if pergunta:
        resposta = processar_pergunta(pergunta)
        st.write(f"Sua pergunta: {pergunta}")
        st.write(f"Resposta do Chatbot: {resposta}")

def processar_pergunta(pergunta):
    # Dicionário de perguntas e respostas
    perguntas_respostas = {
        "Qual é a função do Tribunal de Contas do Estado?": "O Tribunal de Contas do Estado é responsável por fiscalizar as contas públicas para garantir a transparência e o bom uso dos recursos.",
        "Como posso entrar em contato com o Tribunal de Contas do Estado?": "Você pode entrar em contato com o Tribunal de Contas do Estado através do telefone (XX) XXXX-XXXX ou pelo e-mail contato@tce.gov.br.",
        "Qual é o papel principal do Tribunal de Contas do Estado?": "O papel principal do Tribunal de Contas do Estado é fiscalizar as contas públicas dos municípios e do próprio estado para garantir a transparência e o bom uso dos recursos."
    }

    resposta = perguntas_respostas.get(pergunta, "Desculpe, não entendi a sua pergunta.")
    return resposta

if __name__ == "__main__":
    conversa_tce()
