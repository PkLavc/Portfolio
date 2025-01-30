# Como Configurar e Executar Backup Automático no Windows usando xcopy

Para automatizar o processo de backup no Windows, você pode usar o comando `xcopy` no Prompt de Comando. Abaixo está um exemplo de como configurar e executar um backup de uma origem para um destino específico.

## Passos para Configurar o Backup Automático:

### 1. Definir Origem e Destino:

Abra o Bloco de Notas ou um editor de texto e defina as variáveis para a origem e o destino do backup:

@echo off
set origem=C:\Caminho\Para\Origem
set destino=E:\Destino

### 2. Executar o Comando xcopy:

Depois de definir as variáveis, adicione o comando `xcopy` para copiar os arquivos da origem para o destino:

xcopy "%origem%" "%destino%" /E /Y

### Exemplo:

@echo off  
set origem_backup=C:\Documentos\Backup  
set destino_backup=E:\Documentos  

set origem_diversos=C:\Users\MICRO\Desktop\Aula  
set destino_diversos=E:\Aula  

xcopy "%origem_backup%" "%destino_backup%" /E /Y  
xcopy "%origem_diversos%" "%destino_diversos%" /E /Y  

### 3. Explicação dos Comandos:

- `%origem%`: Substitua esta variável pelo caminho real da pasta que você deseja fazer backup.
- `%destino%`: Substitua esta variável pelo caminho real da pasta de destino onde você deseja armazenar o backup.
- `/E`: Copia diretórios e subdiretórios, incluindo diretórios vazios.
- `/Y`: Suprime a solicitação para confirmar a sobrescrita de um arquivo existente.
- 
### 4. Salvar o Arquivo de Configuração:

Após definir as variáveis no Bloco de Notas ou no seu editor de texto preferido, siga estas etapas para salvar o arquivo com uma extensão `.bat` para que o Windows reconheça e execute-o corretamente:

1. **Clique em "Arquivo"** no menu superior do Bloco de Notas.
2. **Selecione "Salvar Como..."** no menu suspenso.
3. **Nomeie o arquivo** com um nome descritivo, por exemplo, `ScriptDeBackup.bat`.
4. **Escolha a localização** onde deseja salvar o arquivo.
5. No campo **"Salvar como tipo"**, selecione **"Todos os arquivos (\*.\*)"**.
6. **Clique em "Salvar"** para salvar o arquivo.

Certifique-se de que a extensão do arquivo seja `.bat` para que o Windows reconheça como um script executável.

### Configurando o Backup Automático:

Você pode configurar o backup para iniciar automaticamente usando o Agendador de Tarefas do Windows. Aqui estão alguns cenários comuns:

#### Ao Iniciar o Computador:

1. **Criar uma Nova Tarefa no Agendador de Tarefas**:
   - Abra o Agendador de Tarefas (`taskschd.msc`).
   - Clique em "Criar Tarefa..." no painel direito.
   - Na guia "Geral", configure um nome para a tarefa, por exemplo, "Backup Automático".
   - Marque a opção "Executar com as permissões mais altas".
   
2. **Configurar o Disparador (Trigger)**:
   - Na guia "Disparadores", clique em "Novo...".
   - Escolha "Ao iniciar" em "Iniciar a tarefa".
   - Confirme e ajuste outras configurações conforme necessário (por exemplo, atraso).

3. **Configurar a Ação**:
   - Na guia "Ações", clique em "Novo...".
   - Configure a ação para iniciar o Prompt de Comando (`cmd.exe`).
   - No campo "Adicionar argumentos (opcional)", insira o caminho completo do seu script de backup:
     ```batch
     /c "C:\Caminho\Para\Seu\ScriptDeBackup.bat"
     ```

#### 5 Minutos Após o Início do Computador:

1. **Criar uma Nova Tarefa no Agendador de Tarefas**:
   - Repita os passos acima para criar uma nova tarefa.
   
2. **Configurar o Disparador (Trigger)**:
   - Escolha "Ao iniciar" em "Iniciar a tarefa".
   - Em "Configurações avançadas do disparador", defina um atraso de 5 minutos.

3. **Configurar a Ação**:
   - Repita os passos acima para configurar a ação com o script de backup.

#### Todos os Dias às 10:00:

1. **Criar uma Nova Tarefa no Agendador de Tarefas**:
   - Repita os passos acima para criar uma nova tarefa.
   
2. **Configurar o Disparador (Trigger)**:
   - Escolha "Diariamente" em "Iniciar a tarefa".
   - Configure o horário para 10:00 da manhã.
   
3. **Configurar a Ação**:
   - Repita os passos acima para configurar a ação com o script de backup.

Certifique-se de salvar e testar cada tarefa criada no Agendador de Tarefas para garantir que o backup automático esteja sendo executado conforme esperado.
