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

    def simulacao(self, n_simulacao: int = 100, custo_operacional: float = 0.001) -> pd.DataFrame:
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
        retornos = self._returns()  
        s = np.random.randint(0, 2, size = (retornos.shape[0], n_simulacao))
        s = np.where(s == 0, -1, s)
        df_s = pd.DataFrame(s[:, 0] * retornos['Returns'] - custo_operacional).cumsum()
        for i in range(1, n_simulacao):
            sys.stdout.write(f'\r {i / n_simulacao * 100:.3}%')
            df_s = pd.concat(
                [
                    df_s, 
                    pd.DataFrame(
                        s[: , i] * retornos['Returns'] - custo_operacional
                        ).cumsum()
                    ], 
                    axis=1)
        return df_s
    
    def loc_sim(self, simulacao, column_number=1):
        """
        Localiza uma coluna específica em um DataFrame de simulações de Monte Carlo.

        A função seleciona e retorna uma coluna do DataFrame de simulações, representando
        uma trajetória específica dos retornos simulados.

        Parâmetros:
            simulacao (pd.DataFrame): DataFrame contendo os resultados das simulações de Monte Carlo.
                Cada coluna representa uma trajetória simulada de retornos.
            column_number (int): Número da coluna a ser localizada. O índice é baseado em zero.
                Padrão: 1.

        Retorna:
            pd.Series: Série contendo os valores da coluna especificada.
        """
        return simulacao.iloc[:, column_number]

