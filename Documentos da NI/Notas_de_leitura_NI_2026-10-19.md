# Registro de leitura — National Instruments

Data: 19/10/2026.
Registro das anotações enviadas pelo autor e de sugestões de análise. Não altera a revisão bibliográfica nem define requisitos aprovados.

## Diretrizes do projeto

O DAQ deve ser modular, de hardware e software abertos e de baixo custo, baseado em microcontrolador ARM de 32 bits, com validação DAQ e demonstração HIL introdutória. A pasta principal definida pelo autor é C:\Users\pedri\OneDrive\Desktop\Uel\TCC\TCC_DAQ.
O autor está lendo materiais gerais da NI; ainda não estudou as referências de equipamentos anteriormente sugeridas.

## Anotações recebidas e conferidas na página da NI

- NI-MCal: correção de offset, ganho e não linearidade com polinômio de terceira ordem; a página descreve coeficientes por faixa armazenados em EEPROM.
- NI-PGIA 2: ganho programável para adequação do sinal ao ADC; o tempo de estabelecimento é relevante na aquisição multiplexada.
- Isolamento: separação elétrica entre o lado de medição e o restante do sistema; pode ser organizado por canal, grupos ou sistema.
- NI Signal Streaming: interface NI-DAQmx comum a diferentes barramentos, com abstração de aspectos de comunicação.

Fonte principal: https://www.ni.com/en/shop/data-acquisition/ni-data-acquisition--the-accuracy-and-performance-difference.html
Fonte complementar indicada pelo autor: https://www.ni.com/en/shop/data-acquisition/five-tips-to-reduce-measurement-noise.html

## Observações para a redação

- Na expressão sobre a importância do PGIA, “depois do ADC” é uma classificação de importância no texto do fabricante, não a posição elétrica do amplificador: o sinal condicionado é fornecido ao ADC.
- O ganho não aumenta o número nominal de bits do ADC.
- A interface de programação comum não demonstra latência ou vazão iguais entre barramentos.
- Conferir no manual de cada modelo a presença dessas tecnologias; não generalizar para todos os produtos NI.

## Sugestões para a revisão e para o projeto

A versão da revisão consultada em output/latex/main.tex da pasta anterior já aborda condicionamento, estabelecimento do sinal, isolamento versus buffer, correção de ganho/offset e limites de comunicação.
Complementar esses tópicos com exemplos NI, evitando repetir fundamentos ou transformar alegações comerciais em conclusões independentes.
Prioridades sugeridas: ganho programável e estabelecimento entre canais; organização do isolamento; separação entre API, protocolo e transporte; correção de erros com validação independente do ajuste.
Para o protótipo, estudar coeficientes por módulo/canal/faixa, interfaces de expansão documentadas e módulos de condicionamento. A ordem do polinômio e a necessidade de isolamento serão decididas por requisitos e ensaios, considerando custo. Essas são propostas, não decisões de implementação.

## PDFs indicados — leitura pendente

- C:\Users\pedri\OneDrive\Desktop\Uel\TCC\TCC_DAQ\Documentos da NI\Tradução\The_Complete_Guide_to_Building_a_Measurement_System_NI(Tradução).pdf
- C:\Users\pedri\Downloads\758450_EMR-NI_DAQ_Fundamentals_Guide_en_WR.pdf

Os PDFs foram registrados como referências fornecidas; seu conteúdo não foi analisado nesta atualização. Novas anotações podem ser acrescentadas a este registro.
