import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filepath = "/Users/jordihohmann/Desktop/V2 Auswertung/Versuch2.csv"
data = pd.read_csv(filepath, sep=";")


def Ftauswertung(data):
    ll = []

    for i in range(3):
        ll.extend([data.iloc[:, i].astype(float).tolist()])

    Ft = []
    for a in ll[1]:
        Ft.append(a / ll[1][-1])

    tau = 1.8 / 19.97
    Ftref = [1 - (np.e) ** (-t / tau) for t in ll[0]]

    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.plot(ll[0], Ft, label="F(t)-Kurve des einzelnen Reaktors", marker="x")
    plt.ylabel("F(t) = (W - W(0))/(W(max) - W(0))")
    plt.xlabel("Zeit [min]")
    plt.legend()
    plt.savefig("/Users/jordihohmann/Desktop/V2 Auswertung/V2 grafik.png")
    # plt.show()


def FtTheoretisch(data):
    ll = []

    for i in range(3):
        ll.extend([data.iloc[:, i].astype(float).tolist()])

    Ft = []
    for a in ll[1]:
        Ft.append(a / ll[1][-1])

    tau = 1.8 / (19.97 / 60)
    Ftref = [1 - (np.e) ** (-t / tau) for t in ll[0]]

    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.plot(
        ll[0], Ftref, label=f"Theor. F(t)-Kurve des einzelnen Reaktors mit Tau = {tau}"
    )
    plt.ylabel("F(t) = (W - W(0))/(W(max) - W(0))")
    plt.legend()
    plt.xlabel("Zeit [min]")
    plt.savefig("/Users/jordihohmann/Desktop/V2 Auswertung/V2 Theoretische Kurve")
    # plt.show()


def FtTheoretischÜber(data):
    ll = []

    for i in range(3):
        ll.extend([data.iloc[:, i].astype(float).tolist()])

    Ft = []
    for a in ll[1]:
        Ft.append(a / ll[1][-1])

    tau = 1.8 / (19.97 / 60)
    Ftref = [1 - (np.e) ** (-t / tau) for t in ll[0]]

    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.plot(ll[0], Ft, label=f"Experimentelle Kurve")
    plt.plot(ll[0], Ftref, label=f"Theoretische Kurve mit Tau = {tau}")
    plt.ylabel("F(t) = (W - W(0))/(W(max) - W(0))")
    plt.xlabel("Zeit [min]")
    plt.legend()
    plt.savefig(
        "/Users/jordihohmann/Desktop/V2 Auswertung/V2 Kurvenübereinanderlegen.png"
    )
    # plt.show()


def Polynomial(data):
    ll = []

    for i in range(3):
        ll.extend([data.iloc[:, i].astype(float).tolist()])

    Ft = []
    for a in ll[1]:
        Ft.append(a / ll[1][-1])

    tau = 1.8 / (19.97 / 60)
    Ftref = [1 - (np.e) ** (-t / tau) for t in ll[0]]

    c = np.polyfit(ll[0], Ft, 6)
    c2 = np.polyfit(ll[0], Ftref, 6)
    x = np.linspace(0, 40, 1000)

    curve = np.poly1d(c)
    curve2 = np.poly1d(c2)
    inte = (1 - curve).integ()
    xplot = np.linspace(0, max(ll[0]), 1000)
    plt.figure(figsize=(10, 6))
    # plt.plot(ll[0], Ft, label=f"Experimentelle Kurve")
    plt.grid(True)
    plt.plot(ll[0], Ft, label=f"Experimentelle Kurve")
    plt.plot(
        xplot,
        curve(xplot),
        label=f"-5.176e-09 x^6 + 6.872e-07 x^5 - 3.745e-05 x^4 + 0.001096 x^3 - 0.01895 x^2 + 0.1957 x",
    )
    plt.ylabel("Polynom/F(t)")
    plt.xlabel("Zeit [min]")
    plt.legend()
    plt.savefig(
        "/Users/jordihohmann/Desktop/V2 Auswertung/V2 Polynomübereinanderlegung.png"
    )
    print(curve)


def PolynomialIntegral(data):
    ll = []

    for i in range(3):
        ll.extend([data.iloc[:, i].astype(float).tolist()])

    Ft = []
    for a in ll[1]:
        Ft.append(a / ll[1][-1])

    tau = 1.8 / (19.97 / 60)
    Ftref = [1 - (np.e) ** (-t / tau) for t in ll[0]]

    c = np.polyfit(ll[0], Ft, 6)
    c2 = np.polyfit(ll[0], Ftref, 6)
    x = np.linspace(0, 40, 1000)

    curve = np.poly1d(c)
    curve2 = np.poly1d(c2)
    inte = (1 - curve).integ()
    xplot = np.linspace(0, max(ll[0]), 1000)
    plt.figure(figsize=(10, 6))
    # plt.plot(ll[0], Ft, label=f"Experimentelle Kurve")
    plt.grid(True)
    plt.plot(
        xplot,
        inte(xplot),
        label=f"wert bei konstanz (t = {max(ll[0])}) = {inte(max(ll[0]))}",
    )
    plt.ylabel("1 - F(t)")
    plt.xlabel("Zeit [min]")
    plt.legend()
    plt.savefig("/Users/jordihohmann/Desktop/V2 Auswertung/V2 polyIntegral.png")
    print(curve)


filepath = "/Users/jordihohmann/Desktop/V2 Auswertung/Versuch2.csv"
data = pd.read_csv(filepath, sep=";")
# FtTheoretisch(data)
# Ftauswertung(data)
# FtTheoretischÜber(data)
Polynomial(data)
