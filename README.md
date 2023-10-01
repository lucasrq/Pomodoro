

# Pomodoro Timer em Python

Este é um simples Pomodoro Timer criado em Python que permite alternar entre períodos de estudo e pausa, com um intervalo entre eles.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter as seguintes bibliotecas instaladas:

- [pygame](https://www.pygame.org/): É usada para reproduzir um arquivo de áudio como um alarme quando o período de estudo ou pausa termina.

Você pode instalá-lo usando o pip:

```bash
pip install pygame
```

Além disso, você deve ter um arquivo de áudio (por exemplo, 'tudo.mp3') no mesmo diretório do código, ou você pode especificar o caminho correto para o seu arquivo de áudio no código.

## Uso

Para executar o programa, siga estas etapas:

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório onde o código Python está localizado.

3. Execute o programa digitando:

```bash
python pomodoro_timer.py
```

4. O programa começará a ser executado e você verá um menu com as seguintes opções:
   - Digite '1' para iniciar um período de pausa.
   - Digite '2' para iniciar um período de estudo.
   - Digite '3' para fechar o programa.

5. Siga as instruções no terminal para começar o período selecionado (pausa ou estudo). O programa reproduzirá um som de alarme quando o período terminar.

6. Após cada período (pausa ou estudo), você terá um intervalo definido antes de começar o próximo. Use esse tempo para descansar ou se preparar para o próximo período.

## Customização

Você pode personalizar o tempo dos períodos de estudo, pausa e intervalo, bem como o arquivo de áudio usado como alarme, modificando as variáveis no código-fonte.

```python
PomodoroPausa = 60 * 5  # Tempo da pausa em segundos
PomodoroEstudos = 60 * 25  # Tempo do estudo em segundos
PomodoroIntervalo = 60  # Tempo antes de começar o próximo período em segundos
```

Certifique-se de que o arquivo de áudio que você deseja usar esteja no mesmo diretório ou atualize o caminho do arquivo neste trecho:

```python
pygame.mixer.music.load('tudo.mp3')
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou recursos adicionais. Basta criar um fork deste repositório, fazer suas modificações e enviar um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

Espero que este README seja útil para você. Se você tiver alguma dúvida ou precisar de mais esclarecimentos, não hesite em perguntar.
