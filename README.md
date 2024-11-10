# Monte Carlo

O código tem como objetivo simular os retornos de um ativo financeiro usando o método de Monte Carlo, que pode ser usado para calcular a probabilidade de diferentes cenários de preços futuros e para modelar o comportamento de ativos sob diferentes condições de mercado. Esse tipo de simulação é amplamente utilizado em finanças para precificação de derivativos, gestão de risco e projeção de resultados.

## Como usar

1. Instalação das bibliotecas
    ```bash
    python -m pip install -r https://github.com/rianlucascs/simulacao-de-monte-carlo/blob/master/requirements.txt
    ```

2. Acessar os dados
    ```python
    import requests

    # URL do script do GitHub
    url = 'https://raw.githubusercontent.com/rianlucascs/simulacao-de-monte-carlo/master/Scripts/monte_carlo.py'

    # Baixando o conteúdo do script
    response = requests.get(url)

    # Executando o conteúdo do script
    exec(response.text)

    # Agora a classe MonteCarlo está disponível, podemos instanciá-la
    monaco = MonteCarlo('VALE3.SA', '1y')

    # Chamar a simulação com 100 simulações e custo operacional de 0.001
    result = monaco.simulacao(numero_simulacao=100, custo_operacional=0.001)

    # Exibir o resultado
    print(result)
    ```

## Saídas

![output](https://github.com/user-attachments/assets/b0ca1c43-07c0-4196-9877-601ceaf7fb8d)

![output2](https://github.com/user-attachments/assets/75d1aabf-9786-498f-9aec-a7d8ff5cc038)

## Contato

Estou à disposição para esclarecer dúvidas ou fornecer mais informações. Você pode entrar em contato através das seguintes opções:

- **LinkedIn:** [Visite meu perfil no LinkedIn](www.linkedin.com/in/rian-lucas)
- **GitHub:** [Explore meu repositório no GitHub](https://github.com/rianlucascs)
- **Celular:** +55 61 96437-9500


Fico sempre aberto a colaborações e oportunidades de networking!
