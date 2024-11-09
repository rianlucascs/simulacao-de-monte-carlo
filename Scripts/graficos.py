import matplotlib.pyplot as plt
import seaborn as sns
from numpy import where



class Grafico:

    def __init__(self, monaco):
        self.monaco = monaco

    def grafico1(self):
        final_returns = self.monaco.iloc[-1] * 100  # Convertendo para percentual
        plt.figure(figsize=(14, 4), dpi=300)
        self._distribuicao_1(final_returns)
        self._title_and_labels_1()
        plt.tight_layout()
        plt.show()

    def grafico2(self):
        for col in self.monaco.columns:
            self.monaco[col] = where(self.monaco[col] < -1, -1, self.monaco[col])

        with plt.style.context("seaborn-v0_8-whitegrid"):
            plt.figure(figsize = (14, 7), dpi=300)
            self._plot_line()
            self._title_and_labels_2()
            

    def _plot_line(self):
        plt.plot(self.monaco * 100, linewidth = 1)
        

    def _distribuicao_1(self, final_returns):
        sns.kdeplot(final_returns, color="dodgerblue", lw=2, fill=True, alpha=0.3)

    def _title_and_labels_1(self):
        plt.title('Distribuição dos Retornos', fontsize=18, fontweight='bold', color='black')
        plt.xlabel('Retornos (%)', fontsize=14, fontweight='bold')
        plt.ylabel('Densidade', fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7) 

    def _title_and_labels_2(self):
        plt.xlabel("Tempo", fontsize=14, fontweight='bold')
        plt.ylabel("Retorno Total (%)", fontsize=14, fontweight='bold')
        plt.title("Simulação", fontsize=16, fontweight='bold')

        plt.grid(True, linestyle='--', alpha=0.6)