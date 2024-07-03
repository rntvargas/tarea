import streamlit as st
import time

memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fibonacci(n - 1) + fibonacci(n - 2)
    memo[n] = result
    return result

def print_fibonacci_series(n):
    series = [fibonacci(i) for i in range(n)]
    return series


def main():
    st.title('Calculadora de serie fibonacci')
    
    num_sequences = st.number_input('ingrese el numero de secuencias fibonacci que decea generar y mostrar', min_value=1, value=5, step=1)
    
    start_time = time.time()
    for i in range(1, num_sequences + 1):
        st.header(f'Secuencia {i}:')
        series = print_fibonacci_series(i)
        st.write(series)
        st.write('---')
    
    end_time = time.time()
    execution_time = end_time - start_time
    st.write(f'Tiempo de ejecución total: {execution_time:.4f} segundos')

if __name__ == '__main__':
    main()
