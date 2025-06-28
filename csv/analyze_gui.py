import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Product Analyzer")
        self.geometry("400x200")

        tk.Label(self, text="CSV de entrada:").pack(anchor='w', padx=10, pady=5)
        self.entry_input = tk.Entry(self, width=40)
        self.entry_input.pack(anchor='w', padx=10)
        tk.Button(self, text="Buscar", command=self.browse_input).pack(anchor='w', padx=10, pady=2)

        tk.Label(self, text="CSV de salida:").pack(anchor='w', padx=10, pady=5)
        self.entry_output = tk.Entry(self, width=40)
        self.entry_output.pack(anchor='w', padx=10)
        tk.Button(self, text="Buscar", command=self.browse_output).pack(anchor='w', padx=10, pady=2)

        tk.Label(self, text="Columna de descripcion:").pack(anchor='w', padx=10, pady=5)
        self.entry_column = tk.Entry(self, width=40)
        self.entry_column.insert(0, 'descripcion')
        self.entry_column.pack(anchor='w', padx=10)

        tk.Button(self, text="Procesar", command=self.run).pack(pady=10)

    def browse_input(self):
        path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
        if path:
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, path)

    def browse_output(self):
        path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])
        if path:
            self.entry_output.delete(0, tk.END)
            self.entry_output.insert(0, path)

    def run(self):
        entrada = self.entry_input.get()
        salida = self.entry_output.get() or 'productos_con_parametros.csv'
        columna = self.entry_column.get() or 'descripcion'
        if not entrada:
            messagebox.showerror('Error', 'Debes seleccionar un archivo de entrada')
            return
        try:
            df = pd.read_csv(entrada)
            if columna not in df.columns:
                raise ValueError(f"La columna '{columna}' no existe en el CSV")
            df[['color', 'tamano']] = df[columna].apply(lambda d: pd.Series(extraer_parametros(d)))
            df.to_csv(salida, index=False)
            messagebox.showinfo('Exito', f'Archivo guardado en {salida}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    app = App()
    app.mainloop()
