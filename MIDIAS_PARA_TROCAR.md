# Mídias de exemplo para substituir

Todos os caminhos usados pelas páginas ficam em `js/media.js`. Para trocar uma mídia mantendo o nome do arquivo, substitua o arquivo correspondente; se mudar o nome ou a pasta, atualize `src` no mapa. Reexecute `python scripts/gerar_midias.py` para recriar os exemplos sintéticos.

| Arquivo | Uso | Substituição recomendada |
|---|---|---|
| `assets/img/processo-gravacao.png` | Início e módulo de conceitos | Foto/ilustração de microfone ou processo de gravação; atualizar `alt` e legenda no mapa. |
| `assets/img/equipamentos.png` | Galeria multimídia | Foto de equipamentos reais usados no trabalho. |
| `assets/img/capa-video.png` | Capa do vídeo | Uma imagem representativa do tutorial. |
| `assets/svg/onda-sonora.svg` | Conceitos | Diagrama vetorial de onda sonora. |
| `assets/svg/amostragem.svg` | Módulo de amostragem | Diagrama vetorial mostrando instantes de amostragem. |
| `assets/svg/quantizacao.svg` | Módulo de quantização | Diagrama vetorial de níveis de quantização. |
| `assets/audio/tom-8khz.wav`, `tom-22050hz.wav`, `tom-44100hz.wav` | Comparação de taxas | A mesma gravação da equipe exportada em mono a 8.000, 22.050 e 44.100 Hz. |
| `assets/audio/tom-8bits.wav`, `tom-16bits.wav` | Comparação de profundidade | A mesma gravação da equipe em mono, 48.000 Hz, exportada em PCM de 8 e 16 bits. |
| `assets/audio/tom-exemplo.wav` | Módulo WAV versus MP3 | Gravação da equipe em WAV. Use o mesmo áudio na versão MP3 para uma comparação justa. O gerador preserva esse arquivo se ele já existir. |
| `assets/audio/tom-exemplo.mp3` | Módulo WAV versus MP3 | A mesma gravação, exportada em MP3. O caminho já está configurado em `js/media.js`. |
| `assets/audio/antes-com-ruido.wav`, `depois-limpo.wav` | Antes/depois de tratamento | A mesma fala da equipe antes e depois da redução de ruído e ajuste de nível. O gerador preserva os arquivos se já existirem. |
| `assets/audio/trilha-midi-renderizada.wav` | Galeria MIDI | Renderização audível do arquivo MIDI original. |
| `assets/midi/trilha-exemplo.mid` | Download MIDI | Arquivo MIDI original, editável em software compatível. |
| `assets/video/tutorial-placeholder.mp4` | Vídeo da galeria | **Pendente:** nenhum codificador MP4 está instalado neste ambiente. Grave/exporte um MP4 H.264 com áudio opcional e salve com este nome, ou altere `src` em `js/media.js`. O player já está preparado. |

Os arquivos `tom-8khz.wav`, `tom-22050hz.wav`, `tom-44100hz.wav`, `tom-8bits.wav`, `tom-16bits.wav`, `tom-exemplo.wav`, `tom-exemplo.mp3`, `antes-com-ruido.wav` e `depois-limpo.wav` são gravações fornecidas pela equipe. A trilha MIDI e os desenhos PNG e SVG foram gerados pelo script local. O gerador preserva as gravações se elas já existirem.
