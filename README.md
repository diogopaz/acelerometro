# Nível Digital com Celular e Python

Este projeto utiliza os sensores de acelerômetro de um smartphone para criar um nível digital em tempo real, que é exibido no terminal do computador.

A comunicação é feita via Wi-Fi com o auxílio do aplicativo **phyphox**, que transmite os dados do sensor para um script em Python.

## Pré-requisitos

1.  **No Computador:**
    * Python 3 instalado.
    * A biblioteca `requests`. Para instalar, execute:
        ```bash
        pip install requests
        ```

2.  **No Celular:**
    * O aplicativo **phyphox** (disponível para Android e iOS).

## Como Executar

1.  **No Celular:**
    * Abra o aplicativo **phyphox**.
    * Selecione o experimento **"Acelerômetro (com g)"**.
    * No menu (ícone ⋮), toque em **"Permitir acesso remoto"** e anote o endereço IP que aparecer (ex: `http://192.168.0.100:8080`).

2.  **No Computador:**
    * Abra o arquivo de script Python (ex: `main.py`).
    * Altere a variável `IP_DO_CELULAR` para o endereço IP que você anotou no passo anterior.
        ```python
        IP_DO_CELULAR = "192.168.0.100" # <-- Altere aqui
        ```
    * Abra um terminal ou prompt de comando.
    * Navegue até a pasta onde o script está salvo e execute-o:
        ```bash
        python main.py
        ```

3.  **Inicie o Experimento:**
    * Assim que o script estiver rodando no computador, **pressione o botão de play (▶)** no aplicativo phyphox em seu celular.

O nível digital aparecerá no terminal e reagirá em tempo real à inclinação do seu celular.
