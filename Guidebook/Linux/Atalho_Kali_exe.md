# Como Criar um Atalho no Kali Linux para Executar um Comando

Para criar um atalho no Kali Linux que execute um comando específico, você pode usar um comando `sh -c`. Este comando permite que você execute uma sequência de comandos diretamente no terminal.

## Exemplo de Atalho para Executar um Jogo

Suponha que você deseja criar um atalho para executar o jogo "Grand Theft Auto", que está localizado em `/home/pc/Documentos/Jogos/GrandTheftAuto/`.

### Passos para Criar o Atalho:

1. **Abrir o Terminal:**

   Abra o terminal no Kali Linux.

2. **Criar o Atalho Usando `sh -c`:**

   Use o seguinte comando `sh -c` para criar um atalho que navega até o diretório do jogo e executa o arquivo executável:

   ```bash
   sh -c 'cd "/home/pc/Documentos/Jogos/GrandTheftAuto/" && GrandTheftAuto.exe'
