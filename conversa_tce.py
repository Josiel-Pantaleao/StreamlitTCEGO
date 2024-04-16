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

if __name__ == "__main__":
    conversa_tce()
