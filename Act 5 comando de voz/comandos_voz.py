import speech_recognition as sr
import serial
import time


arduino = serial.Serial('COM6', 9600)

time.sleep(0.5)

reconocedor = sr.Recognizer()


print("Sistema de voz iniciado")
print("Di un comando...")

go = True
while go:

    try:
   
        with sr.Microphone() as fuente:

            reconocedor.adjust_for_ambient_noise(fuente, duration=1)

            print("\nEscuchando...")

            audio = reconocedor.listen(fuente)


        texto = reconocedor.recognize_google(
            audio,
            language="es-MX"
        )

        texto = texto.lower()

        print("Dijiste:", texto)


        # LED 1
        if "enciende led uno" in texto:
            arduino.write(b'A')
            print("LED 1 encendido")


        elif "apaga led uno" in texto:
            arduino.write(b'a')
            print("LED 1 apagado")


        # LED 2
        elif "enciende led dos" in texto:
            arduino.write(b'B')
            print("LED 2 encendido")


        elif "apaga led dos" in texto:
            arduino.write(b'b')
            print("LED 2 apagado")

        # Todos
        elif "enciende todos" in texto:
            arduino.write(b'T')
            print("Todos encendidos")


        elif "apaga todos" in texto:
            arduino.write(b't')
            print("Todos apagados")

        elif "cerrar" in texto:
            arduino.write(b't')
            print("Bye byeee.")
            time.sleep(2)
            arduino.close()
            go = False


        else:
            print("Comando no reconocido")


    except sr.UnknownValueError:
        print("No entendí la voz")


    except sr.RequestError:
        print("Error con el servicio de reconocimiento")