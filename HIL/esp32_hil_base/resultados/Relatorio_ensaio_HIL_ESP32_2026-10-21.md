# Relatório do primeiro ensaio HIL físico com ESP32

**Data:** 21/10/2026

**Placa:** ESP32 DevKit V1 de 30 pinos

**Chip identificado:** ESP32-D0WD-V3, revisão 3.0

**Interface USB:** CH9102 em COM5

**Taxa serial:** 921.600 bit/s

## Objetivo

Verificar o fluxo básico de uma simulação Hardware-in-the-Loop na qual o computador executa o modelo de uma planta e o ESP32 executa um controlador PI. O ensaio também mede a latência de ida e volta da comunicação serial e verifica o cumprimento do período solicitado.

## Configuração

- planta de primeira ordem no computador: `dy/dt = (-y + u)/0,1`;
- integração da planta pelo método de Euler;
- referência do controlador: 1,0;
- controlador PI no ESP32: `Kp = 1,2` e `Ki = 8,0`;
- saturação do controle: 0 a 3,3;
- período do ensaio: 10 ms;
- quantidade de ciclos: 1000;
- duração nominal: 10 s.

Antes de iniciar, o computador envia `RESET` e aguarda `RESET,OK`, zerando o integrador PI. Durante o ensaio, são enviadas mensagens no formato `MEAS,<sequência>,<medição>,<período_s>`. O ESP32 responde com `CTRL,<sequência>,<controle>,<tempo_us>`. O envio do período mantém a integração do controlador coerente com o passo usado no modelo da planta.

## Resultados

| Métrica | Resultado |
|---|---:|
| Amostras concluídas | 1000 |
| Duração real | 10,0009 s |
| Latência média | 3,5510 ms |
| Latência mediana | 3,6005 ms |
| Percentil 95 da latência | 4,1618 ms |
| Percentil 99 da latência | 4,3900 ms |
| Latência máxima | 4,8782 ms |
| Violações do prazo de 10 ms | 0 |
| Respostas ausentes, inválidas ou fora de sequência | 0 detectadas |
| Tempo nominal para atingir 90% da referência | 310 ms |
| Valor final da saída | 1,000000 |
| Valor máximo da saída | 1,000000 |

![Resposta da planta e latência observada](ensaio_serial_10ms.png)

Os dados completos estão disponíveis em [`ensaio_serial_10ms.csv`](ensaio_serial_10ms.csv).

## Interpretação

O protótipo executou o ciclo HIL completo e manteve todas as trocas seriais dentro do período de 10 ms. A resposta da planta foi estável, convergiu para a referência e não apresentou sobressinal no modelo utilizado.

Testes exploratórios mostraram que 1 ms não é compatível com a latência observada nesta combinação de Windows, Python, USB serial e firmware. Um período de 5 ms apresentou margem pequena. Por isso, 10 ms foi adotado como configuração inicial para os próximos experimentos.

## Limitações

Este resultado caracteriza apenas a configuração ensaiada. O Windows e a comunicação USB serial não fornecem garantia de tempo real rígido, e o teste não estabelece uma latência de pior caso. Ensaios futuros devem aumentar a duração, introduzir perturbações e avaliar estatisticamente jitter, perdas, repetibilidade e comportamento sob carga do computador.
