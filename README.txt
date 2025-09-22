# Sistema de Análise de Dados Meteorológicos INMET

## Descrição

Este projeto é uma aplicação em Python desenvolvida para análise de microdados meteorológicos fornecidos pelo INMET (Instituto Nacional de Meteorologia). O sistema permite carregar, processar e analisar dados climáticos de estações meteorológicas espalhadas pelo Brasil, oferecendo funcionalidades para visualização de dados, cálculo de estatísticas, filtros por data e exportação de relatórios.

## Funcionalidades

### **1. Carregamento de Dados**
- Leitura automática de arquivos CSV do INMET organizados por ano
- Suporte aos anos de 2020 a 2024
- Validação e tratamento de dados inconsistentes
- Feedback detalhado do processo de carregamento

### **2. Visualização de Estações**
- Exibição de informações completas de todas as estações carregadas
- Dados incluem: nome, código, localização, coordenadas e altitude
- Contador de registros por estação

### **3. Cálculo de Estatísticas**
- **Métricas calculadas para todas as estações**:
  - Temperatura média (°C)
  - Umidade máxima (%)
  - Precipitação total (mm)
- Estatísticas calculadas automaticamente para cada estação carregada

### **4. Filtro Avançado por Data**
- **Formatos de data aceitos**: YYYY/MM/DD ou DD/MM/YYYY
- **Funcionalidades do filtro**:
  - Filtrar registros por período específico
  - Menu interativo para dados filtrados
  - Visualizar informações das estações no período
  - Calcular estatísticas apenas do período filtrado
  - Ver exemplos de registros do período

### **5. Exportação de Relatórios**
- Relatórios completos de todas as estações carregadas
- Relatórios específicos de períodos filtrados (com nomenclatura automática)
- Formato de saída em arquivo de texto (.txt)
- Codificação UTF-8 para caracteres especiais
- Inclui estatísticas e exemplos de registros

## Requisitos

- Python 3.x (apenas bibliotecas padrão)
- Arquivos CSV do INMET no formato especificado

## Como Executar

1. Certifique-se de que você tem Python 3.x instalado
2. Clone ou baixe o projeto
3. Navegue até o diretório do projeto
4. Execute o comando:

```bash
python main.py
```

## Menu de Opções

Ao executar o programa, você verá o seguinte menu:

```
MENU:

1. Carregar arquivos da pasta 
2. Exibir dados da(s) estação(ões)
3. Exibir estatísticas (média, máximo etc.)
4. Filtrar dados por data
5. Exportar relatório
6. Sair
```

### Exemplo de Execução no Terminal

```
PS C:\projeto> python main.py
MENU:

1. Carregar arquivos da pasta
2. Exibir dados da(s) estação(ões)
3. Exibir estatísticas (média, máximo etc.)
4. Filtrar dados por data
5. Exportar relatório
6. Sair

Escolha uma opção: 1
Digite o ano (2020-2024): 2023
Encontrados 15 arquivos CSV
Processando: BRASILIA_A001.csv
Estação BRASILIA: 8760 registros carregados
...
Total de estações carregadas: 15
15 estação(ões) carregada(s).

Escolha uma opção: 3
BRASILIA:
 > Temperatura média: 22.45°C
 > Umidade máxima: 98.00%
 > Precipitação total: 1250.50mm

SAO PAULO:
 > Temperatura média: 19.80°C
 > Umidade máxima: 95.00%
 > Precipitação total: 1450.20mm

Escolha uma opção: 4

=== FILTRAR DADOS POR DATA ===
Formatos aceitos: YYYY/MM/DD ou DD/MM/YYYY
Exemplos: 2023/01/15 ou 15/01/2023

Digite a data de início: 01/01/2023
Digite a data de fim: 31/01/2023

Filtrando registros...

3 estação(ões) com registros no período.
Total de 2232 registros encontrados.

O que deseja fazer com os dados filtrados?
1. Ver informações das estações
2. Ver estatísticas do período
3. Ver alguns registros de exemplo
4. Exportar relatório do período filtrado
5. Voltar ao menu principal

Escolha uma opção: 2

=== ESTATÍSTICAS DO PERÍODO ===

BRASILIA:
 > Registros no período: 744
 > Temperatura média: 22.45°C
 > Umidade máxima: 98.00%
 > Precipitação total: 125.50mm
```

## Formato dos Dados

O sistema lê arquivos CSV do INMET com a seguinte estrutura:
- **Cabeçalho**: Informações da estação (região, UF, nome, código, coordenadas)
- **Dados**: Registros horários com temperatura, umidade, precipitação e outros parâmetros

## Classes Principais

- **RegistroMeteorologico**: Representa um registro individual de dados meteorológicos
- **EstacaoMeteorologica**: Representa uma estação meteorológica e seus registros
- **Estatisticas**: Calcula estatísticas dos registros meteorológicos

## Tratamento de Erros

O sistema inclui tratamento para:
- Arquivos não encontrados ou pastas inexistentes
- Dados inválidos ou corrompidos nos CSVs
- Entradas de usuário inválidas
- Erros de conversão de tipos (string para float)
- Formatos de data inválidos

## Observações

- O sistema utiliza apenas bibliotecas padrão do Python
- Os dados são processados em memória
- Arquivos CSV devem estar codificados em Latin-1
- O separador usado nos CSVs é o ponto e vírgula (;)
- Valores decimais podem usar vírgula, que são convertidos automaticamente

## Funcionalidades Técnicas Implementadas

### **Programação Orientada a Objetos**
- **Encapsulamento**: Propriedades privadas com getters/setters
- **Composição**: Estações contêm listas de registros meteorológicos
- **Validação de dados**: Tratamento de tipos e valores inválidos

### **Tratamento de Erros Robusto**
- Validação de formato de datas com múltiplos formatos aceitos
- Tratamento de arquivos corrompidos ou inexistentes
- Conversão segura de tipos de dados (float, string)
- Validação de entradas do usuário

### **Funcionalidades Avançadas**
- **Filtros temporais** com validação de períodos
- **Menu interativo** para dados filtrados
- **Relatórios customizáveis** por período
- **Sistema de nomenclatura automática** para arquivos de relatório

## Limitações Conhecidas

- Sistema funciona apenas com arquivos no formato específico do INMET
- Processamento em memória pode ser limitado para arquivos muito grandes
- Filtro por data depende da consistência do formato de data nos arquivos CSV

## Dados
Este repositório inclui apenas arquivos CSV de exemplo. 
Para usar o sistema completo, adicione seus próprios dados do INMET na pasta `inmet/ANO/`.

## Desenvolvido por

Projeto desenvolvido como atividade acadêmica da disciplina Tópicos Especiais - Turma 3INFO-2025 pelos alunos íkaro Nogueira Rossotti e Kezia Luiza do Bomfim Oliveira.
