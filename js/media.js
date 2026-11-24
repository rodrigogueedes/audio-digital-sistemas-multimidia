/* Mapa único de mídias. Preserve os IDs; substitua os arquivos ou atualize src. */
window.MEDIA = {
  recording:{src:'assets/img/processo-gravacao.png',title:'Estúdio de gravação',caption:'Ilustração de exemplo do processo de gravação.',alt:'Microfone em um estúdio com formas de onda ao fundo.'},
  gear:{src:'assets/img/equipamentos.png',title:'Equipamentos de áudio',caption:'Exemplo ilustrativo de equipamentos de áudio digital.',alt:'Ilustração de um microfone, fones e interface de áudio.'},
  wave:{src:'assets/svg/onda-sonora.svg',title:'Onda sonora',caption:'A amplitude varia continuamente ao longo do tempo.',alt:'Onda senoidal contínua em um gráfico de tempo e amplitude.'},
  sampling:{src:'assets/svg/amostragem.svg',title:'Amostragem',caption:'Pontos igualmente espaçados registram valores da onda.',alt:'Onda senoidal com pontos de amostragem espaçados regularmente.'},
  quantization:{src:'assets/svg/quantizacao.svg',title:'Quantização',caption:'Cada amostra é aproximada por um nível discreto.',alt:'Onda e amostras ajustadas a níveis de quantização.'},
  sample8:{src:'assets/audio/tom-8khz.wav',title:'Tom de exemplo · 8 kHz',caption:'Sinal de exemplo com taxa de amostragem de 8 kHz.',alt:''},
  sample22:{src:'assets/audio/tom-22050hz.wav',title:'Tom de exemplo · 22,05 kHz',caption:'Sinal de exemplo com taxa de amostragem de 22,05 kHz.',alt:''},
  sample44:{src:'assets/audio/tom-44100hz.wav',title:'Tom de exemplo · 44,1 kHz',caption:'Sinal de exemplo com taxa de amostragem de 44,1 kHz.',alt:''},
  bits8:{src:'assets/audio/tom-8bits.wav',title:'Tom quantizado · 8 bits',caption:'Exemplo de áudio representado com 8 bits por amostra.',alt:''},
  bits16:{src:'assets/audio/tom-16bits.wav',title:'Tom quantizado · 16 bits',caption:'Exemplo de áudio representado com 16 bits por amostra.',alt:''},
  wav:{src:'assets/audio/tom-exemplo.wav',title:'Exemplo WAV',caption:'Áudio PCM sem compressão, em formato WAV.',alt:''},
  mp3:{src:'assets/audio/tom-exemplo.wav',title:'Áudio de referência (MP3 pendente)',caption:'Exemplo WAV tocável. Substitua por MP3 real e atualize este caminho antes da entrega final.',alt:''},
  noisy:{src:'assets/audio/antes-com-ruido.wav',title:'Antes · com ruído',caption:'Tom acompanhado de ruído de fundo.',alt:''},
  clean:{src:'assets/audio/depois-limpo.wav',title:'Depois · ruído reduzido',caption:'O mesmo tom, com ruído reduzido e volume normalizado.',alt:''},
  midiRender:{src:'assets/audio/trilha-midi-renderizada.wav',title:'Trilha MIDI renderizada',caption:'Versão em áudio de uma melodia de exemplo criada em MIDI.',alt:''},
  midiFile:{src:'assets/midi/trilha-exemplo.mid',title:'Arquivo MIDI original',caption:'Baixe a sequência MIDI original para substituir ou abrir em um editor compatível.',alt:''},
  tutorial:{src:'assets/video/tutorial-placeholder.mp4',title:'Vídeo tutorial de exemplo',caption:'Placeholder MP4. Substitua pelo vídeo tutorial final.',alt:'Vídeo demonstrativo sobre áudio digital.'}
};
