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
| `assets/audio/tom-8khz.wav`, `tom-22050hz.wav`, `tom-44100hz.wav` | Comparação de taxas | Áudios equivalentes gravados nas respectivas taxas. |
| `assets/audio/tom-8bits.wav`, `tom-16bits.wav` | Comparação de profundidade | Mesmo áudio quantizado nas profundidades indicadas. |
| `assets/audio/tom-exemplo.wav` | Demonstração WAV | Exemplo WAV/PCM para apresentar o formato. |
| `assets/audio/antes-com-ruido.wav`, `depois-limpo.wav` | Antes/depois de tratamento | Gravação original e versão tratada; mantenha o mesmo conteúdo para comparar. |
| `assets/audio/trilha-midi-renderizada.wav` | Galeria MIDI | Renderização audível do arquivo MIDI original. |
| `assets/midi/trilha-exemplo.mid` | Download MIDI | Arquivo MIDI original, editável em software compatível. |
| `assets/video/tutorial-placeholder.mp4` | Vídeo da galeria | **Pendente:** nenhum codificador MP4 está instalado neste ambiente. Grave/exporte um MP4 H.264 com áudio opcional e salve com este nome, ou altere `src` em `js/media.js`. O player já está preparado. |
| MP3 real | Módulo de formatos | **Pendente:** o ambiente não tem codificador MP3. Exporte um arquivo MP3 real, coloque-o em `assets/audio/` e atualize o registro `mp3` em `js/media.js`. O exemplo WAV atual é rotulado como tal para não fingir ser MP3. |

Os desenhos PNG e SVG, WAVs sintéticos e arquivos MIDI deste protótipo foram gerados pelo script local e não representam gravações reais.
