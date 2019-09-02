import speech_recognition as sr 
import playsound
import time
import os
from gtts import gTTS 

# funções
def falar(texto):
    tts = gTTS(text=texto, lang="pt-br")
    nomeArquivoSaida = "saida.mp3"
    tts.save(nomeArquivoSaida)
    playsound.playsound(nomeArquivoSaida)

# main
if __name__ == "__main__":
    falar("Este é um teste de implementação com a rotina de voz em python.")