# BS

Black-Scholes Option Pricer (GUI)

A simple Python desktop app that calculates European call and put option prices using the Black-Scholes model. The app has a graphical user interface built with `tkinter`.

<img width="1435" height="854" alt="image" src="https://github.com/user-attachments/assets/93ca55a4-7f43-4094-96c4-b9dae59f9e4e" />
<img width="1440" height="900" alt="Screenshot 2025-08-10 at 23 22 13" src="https://github.com/user-attachments/assets/ecc8b477-53c8-4f59-bcc2-f836a31cea94" />


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
    git clone https://github.com/harrycanty/BS.git
    cd BS
    ```

2. Install dependencies:

    ```bash
    pip install numpy
    ```

3. Run the app:

    ```bash
    python black_scholes_calculator.py 
    ```

---

This app uses the **Black-Scholes model**, a standard mathematical model for pricing European-style options. It assumes:

- No dividends
- Constant volatility
- Constant interest rates
- Log-normally distributed asset returns

---

Author

**Harry Canty**  
Finance student | Aspiring investment analyst

Built this project to learn Python and gain a practical understanding of options and derivatives.  
Feel free to reach out with suggestions or comments.
