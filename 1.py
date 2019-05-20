import numpy as np
import matplotlib.pyplot as plt
import statistics as xd

A = 1.2  # amplitude of signal
#poziom kwantyzacji
Q = 1/10  # quantization stepsize
N = 2000  # number of samples

def uniform_midtread_quantizer(x, Q):
    # limiter
    x = np.copy(x)
    idx = np.where(np.abs(x) >= 1)
    x[idx] = np.sign(x[idx])
    # linear uniform quantization
    xQ = Q * np.floor(x/Q + 1/2)

    return xQ

def plot_signals(x, xQ):
    e = xQ - x
    mses = xd.mean((xQ - x)**2)
    plt.figure(figsize=(10,6))
    plt.plot(x, label=r'discrete signal $x[k]$')
    plt.plot(xQ, label=r'quantized signal $x_Q[k]$')
    plt.plot(e, label=r'quantization error $e[k]$')
    plt.xlabel(r'$k$')
    plt.axis([0, N, -1.1*A, 1.1*A])
    plt.legend()
    plt.grid()
    plt.show()
    print("Błędy:",e,mses)

# generate signal
# dane
x = [1,312,3123,123,123,124,534534,5,34534,5345,345345,345]
#x = A * np.sin(2*np.pi/N * np.arange(N))
# quantize signal
xQ = uniform_midtread_quantizer(x, Q)
# plot signals
plot_signals(x, xQ)
