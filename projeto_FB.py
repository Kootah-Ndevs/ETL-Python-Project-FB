import pandas as pd
import os


def extrair():
    print("--- Etapa 1: Localizando e lendo arquivo ---")
    
    
    caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
   
    caminho_completo = os.path.join(caminho_da_pasta, 'personagens_FB.csv')
    
    print(f"Buscando em: {caminho_completo}")
    return pd.read_csv(caminho_completo)


def transformar(df):
    print("--- Etapa 2: Transformando dados (Lógica do Zodíaco) ---")
    
    def gerar_mensagem(linha):
        nome = linha['Nome']
        signo = linha['Signo']
        
        maldicao = str(linha['Maldicao_Ativa']).strip().lower()
        
        if maldicao == 'sim':
            return f"{nome} ainda carrega o espírito do {signo}."
        else:
            return f"Que alegria! {nome} está livre do vínculo com o {signo}!"

    
    df['Mensagem_Personalizada'] = df.apply(gerar_mensagem, axis=1)
    return df


def carregar(df_final):
    print("--- Etapa 3: Salvando o resultado final ---")
    
    caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
    caminho_saida = os.path.join(caminho_da_pasta, 'final_Sohma.csv')
    
    
    df_final.to_csv(caminho_saida, index=False)
    print(f"Sucesso! Arquivo criado em: {caminho_saida}")


if __name__ == "__main__":
    try:
       
        dados_brutos = extrair()
        
        
        dados_transformados = transformar(dados_brutos)
        
        
        print("\n--- PRÉVIA DOS DADOS ---")
        print(dados_transformados[['Nome', 'Mensagem_Personalizada']])
        
        
        carregar(dados_transformados)
        
        print("\nPipeline de Fruits Basket finalizado com sucesso!")
        
    except FileNotFoundError:
        print("\n[ERRO]: O arquivo 'personagens_FB.csv' não foi encontrado na pasta.")
    except Exception as e:
        print(f"\n[ERRO INESPERADO]: {e}")