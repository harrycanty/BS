# BS

Black-Scholes Option Pricer (GUI)

A simple Python desktop app that calculates European call and put option prices using the Black-Scholes model. The app has a graphical user interface built with `tkinter`.

---

Features

- Input fields for:
  - Spot price
  - Strike price
  - Risk-free rate
  - Time to maturity (in days)
  - Volatility
  - Option multiplier
- Outputs:
  - Call and Put prices
  - Greeks: Delta, Gamma, Vega, Theta, Rho
- User interface built with `tkinter`
- Pressing 'calculate' runs the model

---

How to Run


1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/option-pricer.git
    cd option-pricer
    ```

2. Install dependencies:

    ```bash
    pip install numpy
    ```

3. Run the app:

    ```bash
    python main.py
    ```

---

Financial background

This app uses the **Black-Scholes model**, a standard mathematical model for pricing European-style options. It assumes:

- No dividends
- Constant volatility
- Constant interest rates
- Log-normally distributed returns

---

Author

**Harry Canty**  
Finance student | Aspiring investment analyst

Built this project to learn Python and gain a practical understanding of options and derivatives.  
Feel free to reach out with suggestions or comments.
