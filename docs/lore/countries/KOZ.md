# Kingdom of Zauern (`KOZ`)

*Ver `00_CANON_RULES.md` e `02_zauern_torronese_war.md`.*

## Status

- guerra contra Torronese: **IMPLEMENTADO PARCIALMENTE**;
- apoio gydiano e cessão de Karleston: **CANON**;
- início real no runtime: **A VALIDAR**.

## Dados técnicos

No snapshot:

- 9 estados;
- 13.827.519 de manpower;
- 15 fábricas civis;
- 9 militares;
- 25 navios no OOB;
- `declare_war_on` contra TOL no history.

A afirmação antiga de “segunda maior marinha” estava errada; 25 navios era a maior contagem do snapshot.

## Guerra contra Torronese

Zauern recebe de Gydian:

- armas;
- equipamento;
- crédito;
- trabalhadores;
- assessores;
- logística.

Em troca, promete Karleston (361).

## Rota histórica

- aceita o apoio;
- vence ou obtém resultado favorável;
- entrega Karleston;
- torna-se dependente;
- pode entrar no bloco gydiano sob pressão.

## Alternativas

- Torronese vence;
- paz limitada;
- Zauern recusa cessão;
- Gydian promove golpe;
- Zauern muda de patrocinador.

## Implementação

- confirmar guerra no boot;
- definir condição de vitória;
- transferência segura de Karleston;
- reação doméstica;
- entrada condicional na facção;
- impedir repetição.
