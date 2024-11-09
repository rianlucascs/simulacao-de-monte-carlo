from os.path import dirname, abspath
from yfinance import download
import numpy as np
import pandas as pd
import sys

class MonteCarlo:
    """
    Classe MonteCarlo para simulação de retornos financeiros usando o método de Monte Carlo.

    A classe permite realizar simulações de retornos de ativos financeiros, levando em consideração
    variações nos preços ajustados e custos operacionais. O processo é baseado no uso de simulações
    de moedas para modelar os retornos.

    Atributos:
        ticker (str): Símbolo do ativo financeiro (exemplo: 'AAPL', 'GOOG').
        period (str): Período de dados financeiros a serem baixados (exemplo: '1y', '5d').
        path (str): Caminho absoluto do diretório onde o script está localizado.

    Métodos:
        _returns(): Calcula os retornos diários dos preços ajustados de fechamento.
        simulacao(numero_simulacao=100, custo_operacional=0.001): Realiza a simulação de Monte Carlo
            para os retornos, levando em conta o custo operacional.
    """

    def __init__(self, ticker: str, period: str):
        """
        Inicializa a classe MonteCarlo com os parâmetros fornecidos.

        Parâmetros:
            ticker (str): O ticker do ativo financeiro a ser analisado.
            period (str): O período para o qual os dados financeiros serão baixados (por exemplo, '1y', '5d').
        """
        self.ticker = ticker
        self.period = period
        self.path = dirname(abspath(__file__))

    def _returns(self) -> pd.DataFrame:
        """
        Calcula os retornos diários dos preços ajustados de fechamento.

        A função baixa os dados financeiros do ativo especificado (ticker) e calcula os retornos diários
        com base nos preços de fechamento ajustados. O retorno é uma série temporal de percentuais de variação.

        Retorna:
            pd.DataFrame: DataFrame contendo os preços ajustados e os retornos calculados.
        """
        df_data = download(self.ticker, period=self.period, progress=False)[['Adj Close']]
        df_data['Returns'] = df_data['Adj Close'].pct_change(1)  # Cálculo de retornos diários
        return df_data

    def simulacao(self, numero_simulacao: int = 100, custo_operacional: float = 0.001) -> pd.DataFrame:
        """
        Realiza a simulação de Monte Carlo para os retornos do ativo financeiro.

        A função realiza a simulação de Monte Carlo para o ativo financeiro especificado, gerando uma matriz de simulações
        de moedas (0 ou 1) que representam os retornos diários ajustados por um custo operacional.

        Parâmetros:
            numero_simulacao (int): O número de simulações a serem realizadas (padrão é 100).
            custo_operacional (float): O custo operacional a ser subtraído dos retornos simulados (padrão é 0.001).

        Retorna:
            pd.DataFrame: DataFrame contendo as simulações cumulativas dos retornos ao longo do tempo.
        """
        df_data = self._returns()  
        moedas = np.random.randint(0, 2, size = (df_data.shape[0], numero_simulacao))
        moedas = np.where(moedas == 0, -1, moedas)
        df_moedas = pd.DataFrame(moedas[:, 0] * df_data['Returns'] - custo_operacional).cumsum()
        for i in range(1, numero_simulacao):
            sys.stdout.write(f'\r {i/numero_simulacao*100:.3}%')
            df_moedas = pd.concat([df_moedas, pd.DataFrame(moedas[: , i] * df_data['Returns'] - custo_operacional).cumsum()], axis=1)
        return df_moedas
