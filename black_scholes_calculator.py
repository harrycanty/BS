from black_scholes import BS
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Formatting helpers ----------
def fmt_money(x):   # prices, vega, theta, rho (cash)
    return f"{x:,.2f}"

def fmt_small(x):   # deltas/gammas
    return f"{x:.4f}"

# ---------- App ----------
class BSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HC Black–Scholes")
        self.geometry("520x420")
        self.minsize(520, 420)
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Root padding
        container = ttk.Frame(self, padding=12)
        container.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # Inputs frame
        inputs = ttk.LabelFrame(container, text="Inputs")
        inputs.grid(row=0, column=0, sticky="ew")
        for i in range(4):
            inputs.columnconfigure(i, weight=1)

        # Input variables
        self.var_spot = tk.StringVar(value="1800")
        self.var_strike = tk.StringVar(value="1800")
        self.var_rate = tk.StringVar(value="0.01")      # decimal
        self.var_days = tk.StringVar(value="30")        # days
        self.var_vol = tk.StringVar(value="0.20")       # decimal
        self.var_mult = tk.StringVar(value="100")       # contract multiplier

        # Row 0
        self._add_labeled_entry(inputs, "Spot", self.var_spot, 0, 0)
        self._add_labeled_entry(inputs, "Strike", self.var_strike, 0, 1)
        self._add_labeled_entry(inputs, "Rate (decimal)", self.var_rate, 0, 2)
        self._add_labeled_entry(inputs, "Days to Expiry", self.var_days, 0, 3)
        # Row 1
        self._add_labeled_entry(inputs, "Vol (decimal)", self.var_vol, 1, 0)
        self._add_labeled_entry(inputs, "Multiplier", self.var_mult, 1, 1)

        # Action row
        actions = ttk.Frame(container)
        actions.grid(row=1, column=0, sticky="ew", pady=(8, 0))
        actions.columnconfigure(0, weight=1)
        self.btn_calc = ttk.Button(actions, text="Calculate", command=self.on_calculate)
        self.btn_calc.grid(row=0, column=0, sticky="e")

        # Output grid
        outputs = ttk.LabelFrame(container, text="Results (per contract)")
        outputs.grid(row=2, column=0, sticky="nsew", pady=(8, 0))
        container.rowconfigure(2, weight=1)

        # Metrics and label store
        self.metrics = ["Price", "Delta", "Gamma", "Vega", "Theta (per yr)", "Rho (per 1%)"]
        self.call_labels = {}
        self.put_labels = {}

        # Header
        ttk.Label(outputs, text="").grid(row=0, column=0, padx=6)  # empty top-left
        ttk.Label(outputs, text="Call", font=("", 10, "bold")).grid(row=0, column=1, padx=6)
        ttk.Label(outputs, text="Put", font=("", 10, "bold")).grid(row=0, column=2, padx=6)

        # Rows
        for i, m in enumerate(self.metrics, start=1):
            ttk.Label(outputs, text=m).grid(row=i, column=0, sticky="w", padx=6, pady=2)
            self.call_labels[m] = ttk.Label(outputs, text="—")
            self.put_labels[m]  = ttk.Label(outputs, text="—")
            self.call_labels[m].grid(row=i, column=1, sticky="e", padx=6)
            self.put_labels[m].grid(row=i, column=2, sticky="e", padx=6)

        # Footer
        footer = ttk.Frame(container)
        footer.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        ttk.Label(footer, text="Made by Harry Canty").grid(row=0, column=0, sticky="w")

        # Bind Enter
        self.bind("<Return>", lambda e: self.on_calculate())

    def _add_labeled_entry(self, parent, label, var, row, col):
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=col, sticky="ew", padx=6, pady=4)
        frame.columnconfigure(1, weight=1)
        ttk.Label(frame, text=label).grid(row=0, column=0, sticky="w")
        ent = ttk.Entry(frame, textvariable=var, width=12)
        ent.grid(row=0, column=1, sticky="ew")
        return ent

    def _read_inputs(self):
        try:
            S = float(self.var_spot.get())
            K = float(self.var_strike.get())
            r = float(self.var_rate.get())
            days = float(self.var_days.get())
            vol = float(self.var_vol.get())
            mult = float(self.var_mult.get())
        except ValueError:
            raise ValueError("All inputs must be numeric.")
        if S <= 0 or K <= 0 or days <= 0 or vol <= 0 or mult <= 0:
            raise ValueError("Spot, Strike, Days, Volatility, and Multiplier must be > 0.")
        return S, K, r, days, vol, mult

    def on_calculate(self):
        try:
            S, K, r, days, vol, mult = self._read_inputs()
            bs = BS(S, K, r, days, vol, mult)

            # Prices (floats expected from BS), format for display here
            call_price = bs.call_price()
            put_price  = bs.put_price()

            # Greeks
            call_delta = bs.call_delta()
            put_delta  = bs.put_delta()
            gamma      = bs.gamma()
            vega       = bs.vega()
            call_theta = bs.call_theta()
            put_theta  = bs.put_theta()
            call_rho   = bs.call_rho() if hasattr(bs, "call_rho") else bs.call_rho()  # name safe
            put_rho    = bs.put_rho()

            # Update labels (formatting kept consistent)
            self.call_labels["Price"].config(text=fmt_money(call_price))
            self.put_labels["Price"].config(text=fmt_money(put_price))

            self.call_labels["Delta"].config(text=fmt_small(call_delta))
            self.put_labels["Delta"].config(text=fmt_small(put_delta))

            self.call_labels["Gamma"].config(text=fmt_small(gamma))
            self.put_labels["Gamma"].config(text=fmt_small(gamma))  # same for put

            self.call_labels["Vega"].config(text=fmt_money(vega))
            self.put_labels["Vega"].config(text=fmt_money(vega))    # same for put

            self.call_labels["Theta (per yr)"].config(text=fmt_money(call_theta))
            self.put_labels["Theta (per yr)"].config(text=fmt_money(put_theta))

            self.call_labels["Rho (per 1%)"].config(text=fmt_money(call_rho))
            self.put_labels["Rho (per 1%)"].config(text=fmt_money(put_rho))

        except Exception as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    app = BSApp()
    app.mainloop()
