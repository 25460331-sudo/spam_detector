import tkinter as tk
import spam_detector

def analizar_email():
    texto = entrada_email.get()
    if texto == "":
        etiqueta_resultado.config(text="Por favor escribe un email")
        return
    resultado = spam_detector.predecir_spam(texto,modelo,vectorizer)
    if resultado == "SPAM":
        etiqueta_resultado.config(text= "SPAM", fg= "red")
    else:
        etiqueta_resultado.config(text="NO SPAM", fg= "green")

def main():
    global modelo, vectorizer, entrada_email, etiqueta_resultado
    print("Entrenando modelo")
    modelo, vectorizer= spam_detector.entrenar_modelo()
    accuracy = spam_detector.evaluar_modelo(modelo,vectorizer)
    print(f"Precisión de modelo {accuracy:.2f}")
    ventana=tk.Tk()
    ventana.title("Detector de Spam")
    ventana.geometry("500x300")
    titulo=tk.Label(ventana,text="Detector de Spam", font=("Arial", 16, "bold"))
    titulo.pack(pady=20)
    entrada_email = tk.Entry (ventana, width=50)
    entrada_email.pack(pady=10)
    boton = tk.Button(ventana, text="Analizar", command=analizar_email,bg="#4caf50", fg="white", padx=20,pady=5)
    boton.pack(pady=10)
    etiqueta_resultado=tk.Label(ventana,text="",font=("Arial", 14))
    etiqueta_resultado.pack(pady=20)
    ventana.mainloop()
if __name__ == "__main__":
    main()