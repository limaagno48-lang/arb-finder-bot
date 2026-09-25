import requests
import time

print("Bot de Arbitragem Iniciado!")

while True:
    try:
        binance = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT").json()
        preco_binance = float(binance['price'])
        
        coinbase = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
        preco_coinbase = float(coinbase['data']['amount'])
        
        diferenca = abs(preco_binance - preco_coinbase)
        porcentagem = (diferenca / preco_binance) * 100
        
        print(f"Binance: ${preco_binance:.2f} | Coinbase: ${preco_coinbase:.2f} | Diff: {porcentagem:.2f}%")
        
        if porcentagem > 1.0:
            print("!!! OPORTUNIDADE DE ARBITRAGEM !!!")
            
    except Exception as e:
        print(f"Erro: {e}")
    
    time.sleep(10)
