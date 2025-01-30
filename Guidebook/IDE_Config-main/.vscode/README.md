<!-- *************************************************java.json**************************************************** -->
# java.json 

Adiciona automaticamente, via snippets, um método `main` com um parâmetro `String[] args` ao digitar 'main' e pressionar Tab.

## Como configurar snippets no VS Code

Siga os passos abaixo para adicionar ou modificar os snippets de Java no Visual Studio Code:

1. Vá para **File** > **Preferences** > **Configure User Snippets**.
2. Selecione a linguagem **Java** para começar a editar o arquivo de snippets específico dessa linguagem.
3. Adicione o código ao seu arquivo. 

<!-- ************************************************** Bar ***************************************************** -->

  <img src="https://github.com/PkLavc/PkLavc/blob/94f67aca0f96f0e9cef748c2c27877c02586f77d/resources/Rainbow.gif" width="100%">
  
<!-- *************************************************settings.json**************************************************** -->
# settings.json

Configuração do arquivo `settings.json` para personalizar o ambiente de desenvolvimento, aparência e comportamento de várias extensões, como o Code Runner.

## Como começar

Para abrir o arquivo `settings.json` no Visual Studio Code:

1. Vá para **Manage** > **Settings** > **Open Settings (JSON)**.

## Configuração Detalhada

### Tema da Interface do Usuário

- `"workbench.colorTheme": "Default Dark Modern"`
  - Define o tema de cores para a interface do usuário do VS Code. "Default Dark Modern" é o tema de cores aplicado, modificando a aparência visual do editor, painéis, barra de status e outros elementos da UI para esse tema escuro.

### Comportamento do Explorador de Arquivos

- `"explorer.compactFolders": false`
  - Controla se o Explorador de Arquivos deve compactar pastas que contêm apenas uma subpasta em uma única linha. Definir isso como `false` significa que cada pasta e subpasta é exibida em sua própria linha, facilitando a visualização da estrutura de diretórios.

### Tema de Ícones

- `"workbench.iconTheme": "material-icon-theme"`
  - Define o tema de ícones para o Explorador de Arquivos no Visual Studio Code. O "material-icon-theme" fornece um conjunto de ícones inspirados no design Material, alterando os ícones de arquivos e pastas para melhorar a navegação visual e a intuitividade.

### Configurações de Execução de Código

- `"code-runner.executorMap":`
  - Uma configuração específica para a extensão Code Runner que permite definir comandos personalizados para a execução de código em diferentes linguagens de programação.
    - `"python": "clear ; python -u"`
      - Especifica o comando para executar código Python. `clear` limpa o terminal antes de executar o script, e `python -u` executa o script Python em modo não bufferizado, garantindo que as saídas sejam exibidas prontamente.
    - `"java": "clear && javac $fileName && java $fileNameWithoutExt"`
      - Para Java, o comando limpa o terminal (`clear`), compila o arquivo Java (`javac $fileName`), e executa o código compilado (`java $fileNameWithoutExt`). `$fileName` representa o nome atual do arquivo, e `$fileNameWithoutExt` é o nome do arquivo sem sua extensão.

### Executar no Terminal Integrado

- `"code-runner.runInTerminal": true`
  - Esta configuração permite que o Code Runner execute o código diretamente no terminal integrado do VS Code, em vez de usar o painel de saída padrão na parte inferior. Isso é benéfico para programas que requerem interação durante a execução ou que se beneficiam de um ambiente de terminal completo.

### Ignorar Seleção ao Executar

- `"code-runner.ignoreSelection": true`
  - Quando ativado, o Code Runner executará sempre o arquivo inteiro, independente de qualquer seleção. Se definido como `false`, o Code Runner tentaria executar apenas a parte do código selecionada.
    
<!-- ************************************************** Bar ***************************************************** -->

  <img src="https://github.com/PkLavc/PkLavc/blob/94f67aca0f96f0e9cef748c2c27877c02586f77d/resources/Rainbow.gif" width="100%">
  
<!-- ****************************************************************************************************************** -->


