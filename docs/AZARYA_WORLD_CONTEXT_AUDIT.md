# Azarya — Contexto Mundial (Snapshot Técnico Revisado)

*Snapshot original: 2026-07-15. Revisão documental: 2026-07-17. Este arquivo preserva a auditoria quantitativa anterior, mas não é mais a fonte principal de canon. Em conflitos, prevalecem `docs/lore/00_CANON_RULES.md` e as decisões mais recentes do autor.*

> **Atenção:** os números 57 tags/506 estados pertencem ao snapshot anterior à expansão oriental. ORV, KAR, LIA e estados 507–509 estavam em implementação posterior e exigem nova agregação antes de atualizar os totais.

---

## 1. Resumo executivo

O mod tem **57 tags jogáveis confirmadas**, **57 arquivos de história de país** e **506 estados**. Cenário único: `common/bookmarks/1924.txt`, 1º de janeiro de 1924.

No snapshot original, o mundo tem desigualdade grande: **GYE (Gydian Empire)** concentra ~11% da população mundial e a maior indústria. Vários países (ATV, VAL, HEL, VAN, SAH, ELD e outros) têm população/indústria essencialmente zeradas — **por design nesta fase**: o autor confirmou que muitos países ainda são só divisão territorial, sem dados nem lore, servindo pra mapear como o mundo está dividido antes de decidir quem cada país vai ser.

Conteúdo narrativo mecânico (foco, decisões, eventos próprios) está concentrado em **THK** e **CZL**. O terremoto já está implementado como conteúdo real de jogo (não só conceito), com nome, data, epicentro e consequências políticas descritas. Há três efeitos `declare_war_on` encontrados nos arquivos de história. Eles indicam guerras pretendidas no início, mas ainda exigem validação em runtime (ver seção 6).

---

## 2. Fatos canônicos confirmados

*Fatos desta seção vêm diretamente do autor em conversa, não de inferência de arquivo.*

- **Nome do mundo**: o próprio **Azarya** (não um nome de planeta separado).
- **Geografia**: **2 grandes continentes**, mundo quase uma Pangeia, separados por um **estreito oceânico estreito** entre os dois, com **ilhas ao norte e ao sul**.
- **THK (Thiryn Kingdom)**: caminho canônico da árvore de foco é **Men of Pride** (`THK_MenOfPride`), não Royal Alternative nem Third Option.
- **Great Thiryn** (formação de nação) incorpora os territórios (estados) **86, 409 e 400**.
- **THK e Lesc (CZL)** ficam a uma distância moderada, cruzando parte de um oceano — não vizinhos diretos, mas não excessivamente longe. **Sem lore de rivalidade, história compartilhada ou relação definida ainda — em aberto por decisão do autor.**
- **"Czar" é um título de governo real em Lesc** (CZL), não só linguagem decorativa de texto.
- Muitos países (incluindo Helvaria) são **intencionalmente só território por enquanto** — sem população, indústria ou lore definidos. Isso é esperado nesta fase: o objetivo agora é mapear a divisão do mundo antes de decidir quem cada país vai ser.
- Os arquivos com nomes de países vanilla em `events/` (Germany.txt, Japan.txt, France.txt etc.) são **resíduo confirmado**, não uso intencional reservado.
- **Intenção de design para ideologias**: o autor quer dar profundidade às 4 ideologias principais (fascismo, neutralidade, democracia, comunismo) criando **sub-ideologias dentro de "neutrality"** — ex.: oligárquica, tribal, bandidos, etc. O padrão atual (34 de 57 países em "neutrality" com um governo customizado tipo oligarchism/centrism/polity/outlaws) é **reflexo de países ainda não desenvolvidos**, não uma declaração de lore intencional sobre o estado político do mundo — mas é exatamente o material bruto que essa expansão de sub-ideologias vai usar.

---

## 3. Números gerais do mundo no snapshot de 2026-07-15

| Métrica | Valor |
|---|---|
| Tags confirmadas | 57 |
| Estados totais | 506 |
| Estados sem dono (owner) | 160 (~32% do mapa) |
| População mundial (manpower somado) | 286.648.817 |
| Fábricas civis (mundo) | 344 |
| Fábricas militares (mundo) | 162 |
| Estaleiros (mundo) | 86 |
| Bases navais (mundo) | 188 níveis |
| Bases aéreas (mundo) | 97 níveis |

*Calculado via script agregando os 506 arquivos de `history/states/` (0 falhas de parse). Os 160 estados sem dono podem ser território ainda não distribuído entre os 57 países (mais provável, dado que vários países ainda são "só território") — não confirmado como ligado ao terremoto.*

---

## 4. Tabela resumida dos 57 países

Ordenado por população. `Governo` mistura `ruling_party` padrão com o token de ideologia customizado usado em `create_country_leader` (nomes próprios como Rexism, Oligarchism, Falangism, Outlaws, Constitutional_Monarchy — parte do sistema de sub-ideologias que o autor está desenvolvendo, ver seção 2).

| Tag | Nome | Capital | Governo | Estados | População | Civis | Militares | Estaleiros | Divisões | Navios | Conteúdo |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| GYE | Gydian Empire | 346 | fascism/Rexism | 25 | 31.288.550 | 50 | 23 | 11 | 33 | 0 | Médio |
| SIT | Sithius | 51 | neutrality/Const.Monarchy | 11 | 17.704.195 | 16 | 8 | 6 | 0 | 0 | Médio |
| LVD | Leovardia | 387 | neutrality/Const.Monarchy | 7 | 17.125.494 | 12 | 6 | 5 | 13 | 0 | Médio |
| BOM | Montia | 269 | fascism/falangism | 12 | 15.942.311 | 18 | 9 | 4 | 28 | 0 | Médio |
| KOZ | Kingdom of Zauern | 396 | neutrality/oligarchism | 9 | 13.827.519 | 15 | 9 | 4 | 21 | 25 | Médio — declara guerra em TOL |
| DTB | Durtenbach | 186 | neutrality/oligarchism | 15 | 12.757.620 | 16 | 11 | 7 | 0 | 0 | Baixo |
| NSA | Novasovia | 477 | communism/leninism | 13 | 12.295.335 | 16 | 11 | 5 | 0 | 0 | Baixo |
| **CZL** | **Czariado de Lesc** | **335** | **neutrality/oligarchism (Czar)** | **14** | **12.229.225** | **11** | **3** | **2** | **18** | **21** | **Alto** |
| SLU | Sollerium | 136 | fascism/Absolutism | 18 | 11.381.488 | 8 | 4 | 4 | 0 | 0 | Médio |
| ARD | Aeridor | 388 | democratic/conservatism | 11 | 11.227.452 | 7 | 3 | 3 | 12 | 0 | Médio |
| TOL | Torronese League | 449 | democratic/Conservatism | 12 | 11.212.554 | 13 | 6 | 5 | 15 | 18 | Médio |
| BKG | Blutkrieger | 10 | fascism/Absolutism | 14 | 9.116.522 | 11 | 7 | 3 | 0 | 0 | Baixo |
| UPG | United Provinces of Gengen | 430 | democratic/conservatism | 12 | 8.075.849 | 11 | 5 | 4 | 18 | 0 | Médio |
| VRD | Varadnia | 164 | communism/conservatism | 6 | 7.501.964 | 4 | 2 | 0 | 0 | 0 | Baixo |
| **THK** | **Thiryn Kingdom** | **382** | **neutrality/Const.Monarchy (Aurum)** | **7** | **6.904.586** | **9** | **3** | **1** | **8** | **14** | **Alto** |
| NIR | Nirisia | 368 | neutrality/Centrism | 4 | 6.530.975 | 7 | 2 | 2 | 6 | 0 | Médio |
| SVD | Serenvioled | 214 | democratic/Merchant Rep. | 8 | 6.524.304 | 12 | 5 | 4 | 0 | 0 | Médio |
| RFO | Ròsfhios | 168 | neutrality/Polity | 10 | 6.309.302 | 14 | 2 | 3 | 0 | 0 | Baixo |
| SLV | Sylvan | 336 | democratic/liberalism | 13 | 6.180.553 | 6 | 2 | 2 | 14 | 0 | Médio |
| LUQ | Luquitos | 175 | neutrality/Outlaws | 8 | 4.826.091 | 9 | 2 | 3 | 0 | 0 | Médio |
| ARK | Aurelia | 225 | neutrality/conservatism | 4 | 3.772.571 | 4 | 1 | 0 | 0 | 0 | Baixo |
| LUA | Luradia | 212 | neutrality/oligarchism | 5 | 3.718.782 | 8 | 5 | 0 | 0 | 0 | Baixo |
| AEI | Aelosia | 174 | democratic/conservatism | 7 | 3.423.901 | 6 | 2 | 1 | 0 | 0 | Médio |
| CBS | Cambelese Desert | 468 | neutrality/oligarchism | 5 | 3.321.955 | 6 | 3 | 0 | 17 | 0 | Médio |
| FVI | Fervonia | 343 | neutrality/Centrism | 3 | 3.216.667 | 5 | 2 | 0 | 4 | 0 | Baixo |
| BOK | Bokkan | 485 | neutrality/conservatism | 4 | 2.918.451 | 4 | 2 | 0 | 0 | 0 | Baixo |
| ATI | Attica | 47 | democratic/Centrism | 1 | 2.839.849 | 3 | 1 | 0 | 2 | 0 | Baixo |
| CMR | Cymranth | 412 | neutrality/Centrism | 6 | 2.728.379 | 3 | 1 | 1 | 3 | 0 | Baixo |
| BOA | Bolia | 15 | neutrality/Centrism | 4 | 2.699.409 | 5 | 3 | 1 | 0 | 0 | Baixo |
| DUH | Durnstad | 6 | neutrality/Const.Monarchy | 2 | 2.689.671 | 3 | 1 | 0 | 4 | 0 | Médio |
| MER | Mercadia | 474 | democratic/Merchant Rep. | 2 | 2.550.933 | 3 | 2 | 1 | 0 | 0 | Baixo |
| MOR | Mortdet | 188 | neutrality/conservatism | 3 | 2.283.700 | 0 | 0 | 0 | 0 | 0 | Baixo |
| DKG | Delp | 17 | neutrality/oligarchism | 9 | 2.200.061 | 0 | 0 | 0 | 0 | 0 | Baixo |
| INV | Ironvale | 469 | neutrality/Centrism | 3 | 2.132.544 | 4 | 0 | 0 | 0 | 0 | Baixo |
| KES | Kaesset | 236 | neutrality/conservatism | 1 | 2.098.598 | 2 | 1 | 1 | 0 | 0 | Baixo |
| GET | Griester | 223 | neutrality/Polity | 3 | 2.012.236 | 3 | 2 | 1 | 0 | 0 | Baixo — declara guerra em SVD |
| DRM | Draemir | 497 | neutrality/centrism | 1 | 1.992.940 | 2 | 1 | 0 | 4 | 0 | Baixo |
| RFB | Riofriolia | 80 | neutrality/Outlaws | 1 | 1.892.940 | 3 | 2 | 0 | 5 | 0 | Médio |
| EYD | Eryndale | 27 | democratic/Centrism | 5 | 1.777.764 | 2 | 2 | 2 | 0 | 0 | Baixo |
| TRD | Tridian | 496 | neutrality/Centrism | 1 | 989.862 | 2 | 1 | 0 | 2 | 0 | Baixo |
| SDB | SeddusBadlands | 22 | neutrality/Centrism | 3 | 957.944 | 2 | 1 | 0 | 3 | 0 | Baixo |
| RES | Red Scars | 465 | neutrality/Outlaws | 1 | 890.985 | 2 | 2 | 0 | 4 | 0 | Médio |
| KRT | Kareth | 502 | neutrality/Centrism | 1 | 812.501 | 2 | 1 | 0 | 0 | 0 | Baixo |
| EDR | Eldrina | 203 | neutrality/oligarchism | 5 | 796.189 | 0 | 0 | 0 | 0 | 0 | Baixo |
| MEK | Meronian | 217 | fascism/Rexism | 4 | 790.596 | 0 | 0 | 0 | 0 | 0 | Baixo |
| WIH | Wickia | 115 | democratic/conservatism | 8 | 624.827 | 0 | 0 | 0 | 0 | 0 | Baixo |
| ASV | Ash Vultures | 498 | neutrality/Outlaws | 1 | 452.501 | 1 | 1 | 0 | 3 | 0 | Médio |
| DKM | Duskmoor | 232 | neutrality/Centrism | 1 | 378.893 | 0 | 0 | 0 | 0 | 0 | Baixo |
| BLA | Black Knives | 499 | neutrality/Outlaws | 1 | 322.501 | 1 | 1 | 0 | 2 | 0 | Médio |
| SHT | Shattered | 500 | neutrality/Outlaws | 1 | 212.501 | 1 | 1 | 0 | 1 | 0 | Médio |
| TRB | Zandara | 270 | neutrality/conservatism | 3 | 101.894 | 0 | 0 | 0 | 0 | 0 | Baixo |
| ATV | Astravern | 242 | fascism/Rexism | 5 | 5 | 0 | 0 | 0 | 0 | 0 | Só território |
| VAL | Valeria | 216 | fascism/Rexism | 4 | 4 | 0 | 0 | 0 | 0 | 0 | Só território |
| HEL | Helvaria | 198 | neutrality/conservatism | 3 | 3 | 0 | 0 | 0 | 0 | 0 | Só território |
| VAN | Valanora | 163 | democratic/Centrism | 3 | 3 | 0 | 0 | 0 | 0 | 0 | Só território |
| SAH | Sahraza | 124 | neutrality/conservatism | 2 | 2 | 2 | 0 | 0 | 0 | 0 | Só território |
| ELD | Eldwyn | 207 | neutrality/Polity | 1 | 1 | 0 | 0 | 0 | 0 | 0 | Só território — declara guerra em SVD |

*"Só território" = população/indústria placeholder (1-5 manpower), por design nesta fase (ver seção 2) — não é ausência de dado, é o estado esperado de um país ainda não desenvolvido.*

---

## 5. Rankings

**10 mais populosos**: GYE, SIT, LVD, BOM, KOZ, DTB, NSA, CZL, SLU, ARD.

**10 maiores indústrias (civ+mil)**: GYE (73), BOM (27), DTB (27), NSA (27), KOZ (24), SIT (24), TOL (19), BKG (18), LVD (18), SVD (17).

**Maiores exércitos (divisões)**: GYE (33), BOM (28), KOZ (21), UPG/CZL (18), SLV (14), TOL (15), CBS (17).

**Maior infraestrutura naval inicial (níveis de bases navais; não equivale a força da marinha)**: SIT e DTB (16 níveis cada), RFO (14), BKG (12), TOL (11), THK (10), NSA (10). Em contagem de navios no OOB: KOZ (25), CZL (21), TOL (18), THK (14).

**Maior infraestrutura aérea inicial (níveis de bases aéreas; não equivale a número de aeronaves)**: SLU e GYE (8 cada), NSA (7), SIT e DTB (6 cada).

---

## 6. Diplomacia e declarações de guerra no history

- **Nenhuma facção** existe no início do cenário.
- **Declarações de guerra encontradas nos arquivos de história** (`declare_war_on` em `history/countries/`). O início efetivo e a estabilidade dessas guerras precisam ser confirmados em runtime:
  - `ELD - Eldwyn.txt:70` → declara guerra em **SVD** (Serenvioled), CB `annex_everything`
  - `GET - Griester.txt:70` → declara guerra em **SVD** (Serenvioled), CB `annex_everything`
  - `KOZ - Kingdom of Zauern.txt:86` → declara guerra em **TOL** (Torronese League), CB `annex_everything`
  - Nota: ELD e GET miram o **mesmo alvo** (SVD) com o mesmo tipo de guerra total — dois países pequenos/médios tentando anexar o mesmo país já no cenário inicial. Gancho narrativo pronto, ainda sem explicação de lore.
- **Duas garantias**: `GYE = {give_guarantee = DUH}` e `GYE = {give_guarantee = FVI}` — GYE (maior potência) garante a independência de Durnstad e Fervonia, sugerindo papel de potência protetora regional.
- Nenhum sujeito/puppet no início.

---

## 7. Recursos estratégicos

| Recurso | Total mundial | Top produtores |
|---|---:|---|
| Aço | 432 | GYE=80, LVD=50, BOM=40, SIT=25, CZL=22 |
| Petróleo | 183 | SDB=50, GYE=30, SLV=20, MER=20, TRB=12 |
| Tungstênio | 148 | CMR=50, LUQ=30, TOL=15, SIT=12, FVI=12 |
| Alumínio | 139 | GYE=40, LUQ=16, TOL=12, DTB=12, NSA=10 |
| Borracha | 72 | MER=30, SLV=16, SIT=10, GET=8, DTB=4 |
| Cromo | 69 | LVD=18, TOL=12, GYE=12, SLV=10, ARD=10 |

Petróleo é o recurso mais concentrado num único país incomum (SDB — SeddusBadlands, país pequeno dominando 27% do petróleo mundial) — possível gancho narrativo, não confirmado como intencional.

---

## 8. Auditoria de THK (Thiryn Kingdom)

### Confirmado
- Monarquia constitucional, casa de **Aurum**. Governante: **Rainha Elara Lorenthia**.
- Capital: **Eldoria** (estado 382), uma das áreas mais atingidas pelo terremoto. O epicentro geológico exato permanece TBD até validação direta da localisation.
- Árvore de foco: **75 focos** (`common/national_focus/Thiryn.txt`). **Caminho canônico: Men of Pride** (confirmado pelo autor).
- `Great Thiryn`: a formação incorpora os estados **86, 409 e 400** (canon). A notícia precisa ser revalidada no repositório atual: uma auditoria anterior registrou uso de `news.59` vanilla, enquanto este snapshot registrou um evento próprio. Não tratar nenhum dos dois como resolvido sem inspeção.
- Decisões próprias: `common/decisions/THK.txt` (242 linhas), desbloqueadas após completar `THK_RoyalAlternative`.
- Terremoto ("Great Earthquake", fim de 1922) atingiu Eldoria diretamente, ligado à derrota militar de Thiryn e à crise da coroa Aurum.
- Marinha: 10 níveis de base naval, 14 navios no OOB.

### Referenciado, mas não explicado
- Sucessão exata da coroa Aurum além de Elara Lorenthia.
- Composição completa da família real.
- `THK_ThirdOption` e `THK_MenOfPride` como caminhos alternativos existem na árvore, mas Men of Pride é o único confirmado como canônico — o que os outros dois representam narrativamente não foi detalhado.

### Perguntas em aberto
- Linha sucessória completa da dinastia Aurum.
- Ministros/generais nomeados além dos personagens de retrato já conhecidos (Thaddeus Ironwood, Adric Von Drachen, Lysandra Ardent, Magnus Goldcrest).

---

## 9. Auditoria de CZL (Czariado de Lesc)

### Confirmado
- Capital: estado 335. **"Czar" é um título de governo real** (confirmado pelo autor), não decorativo.
- Agitação civil nas províncias do norte, autoridade do Czar contestada (lore de bookmark já existente).
- Possui árvore de foco própria (`common/national_focus/Lesc.txt`) e 3 ideias próprias.
- Possui 21 navios no OOB e 18 divisões, colocando Lesc entre as maiores forças iniciais, mas não como líder isolada: KOZ aparece com 25 navios e GYE/BOM/KOZ possuem mais divisões.
- Distância de THK: moderada, cruzando parte de um oceano — não vizinhos diretos.

### Em aberto (decisão do autor)
- Relação entre Lesc e Thiryn — **sem rivalidade, história ou vínculo definido ainda**. Registrado como aberto, sem sugestão.
- Conteúdo detalhado da árvore de foco de Lesc (não lido nesta rodada).

---

## 10. Países ainda só-território (por design)

O autor confirmou que **vários países são intencionalmente só divisão territorial nesta fase** — sem população real, indústria ou lore — servindo para mapear como o mundo está dividido antes de decidir quem cada país vai ser. Isso inclui pelo menos: **ATV, VAL, HEL (Helvaria), VAN, SAH, ELD**, e provavelmente outros na faixa "Baixo" de conteúdo da tabela da seção 4.

**Helvaria (HEL)** especificamente já tem um sistema de nomes por ideologia definido ("Fascist Directorate of Helvaria", "Republic of Helvaria", "Helvarian Military Junta") mesmo sem dados técnicos — sugerindo que o autor já pensou em múltiplos caminhos de governo possíveis para esse país, a serem desenvolvidos depois.

---

## 11. Outros países com alguma identidade narrativa

5 países têm texto de "briefing" nacional e descrição de bookmark própria, mas ainda nenhuma mecânica de jogo (foco/decisão/ideia):

- **SIT** (Sithius) — remanescente do antigo "Império de Victorium", monarquia marítima.
- **LUQ** (Luquitos/Federal State of Lucafis) — república jovem, união frágil entre clãs de montanha e mercadores costeiros.
- **SLU** (Sollerium) — império de mandato divino, casta governante antiga, ameaça de rebelião.
- **SLV** (Sylvan) — nota: a chave de loc (`SLV_AZARYA_DESC`) descreve "Nicollonia", não "Sylvan" — inconsistência de nome ainda não resolvida. Democracia estável, história de comércio e colonização.
- **SVD** (Serenvioled) — república mercantil, guildas de comércio, neutralidade sob pressão — **e agora também o alvo de duas guerras de anexação simultâneas (ELD e GET, ver seção 6)**, o que dá um gancho narrativo imediato pra esse país.

---

## 12. O terremoto

**Confirmado como conteúdo de jogo real**, não só conceito de bastidores.

- **Nome**: "The Great Earthquake" (`localisation/AZ_lore_l_english.yml`).
- **Data**: fim de 1922.
- **Área central da narrativa**: Eldoria, capital de Thiryn (estado 382), incluindo o bairro "the Shattered Quarter". O epicentro geológico exato permanece TBD.
- **Consequências**: expôs fraturas políticas já existentes; ligado diretamente à derrota militar de Thiryn e à crise da coroa Aurum.
- Sistema de entrega: "Crônicas" (`AZ_CHRONICLE_*`) e lore por estado (`AZ_LORE_TEXT_<id>_N`), acessível via `common/scripted_guis/AZ_lore_atlas.txt` — usa as 2 texturas placeholder já carregadas numa rodada anterior (`AZ_lore_icon_TEMP.dds`/`AZ_lore_mapicon_TEMP.dds`, precisam de arte própria antes de lançamento público).
- Uma entrada da Crônica (`AZ_CHRONICLE_TEXT_5`) diz explicitamente que o registro histórico é "deliberadamente inacabado": a Crônica cobre até o terremoto e a derrota militar de Thiryn, e entrega a narrativa ao jogador a partir de 1924.
- **Em aberto**: quais países além de Thiryn foram atingidos — o texto menciona "peninsula" e "reached well beyond any single kingdom's borders" sem nomear outros países.

---


## 13. Delta de canon posterior ao snapshot

As seguintes decisões foram consolidadas depois da auditoria quantitativa e devem prevalecer:

- Durnstad (`DUH`) e Durtenbach (`DTB`) são países diferentes.
- A garantia gydiana a Durnstad é parte da cadeia proteção → dependência → ruptura → invasão, não uma contradição.
- A Guerra das Três Bandeiras começa entre junho e setembro de 1924.
- Novasovia começa a armar Varadnia aproximadamente cinco meses após o início do cenário.
- Gydian apoia a Junta Helvariana; Montia apoia Durtenbach secretamente.
- A rota histórica dá vitória a Durtenbach e forma uma Helvaria reunificada, principal rival continental de Gydian.
- A Grande Guerra Continental começa aproximadamente em 1927 por uma crise envolvendo Astravern e Helvaria.
- Gengen tende inicialmente ao bloco gydiano.
- Sithius tende historicamente a atuar como aliado menor e oportunista de Gydian.
- Orvena, Karyō e Liangor foram aprovados como base canônica do continente oriental e estão em implementação.
- Doia, Haifa e Mominches devem ser descritos como contendo aproximadamente **1,7 milhão** de habitantes no total.

## 14. Inconsistências técnicas conhecidas

- **`events/` provavelmente ainda tem bastante resíduo vanilla** (confirmado pelo autor): arquivos com nomes de países reais (Germany, Japan, France, Poland, SovietUnion, Spain, China, Hungary, Bulgaria, Ethiopia, Turkey, Finland, Mexico, Paraguay, Britain, Yugoslavia, Greece) e dezenas prefixadas por DLC ainda estão na pasta ativa. Candidato a limpeza futura (fora do escopo desta rodada).
- **`SLV_AZARYA_DESC` descreve "Nicollonia"**, não "Sylvan" — nome de chave e conteúdo do texto divergem.
- Sistema de lore/crônicas depende de 2 texturas temporárias copiadas de outro mod (já carregadas como placeholder, precisam de arte própria antes de release).

---

## 15. Perguntas de lore ainda em aberto

- Sucessão completa da dinastia Aurum em THK.
- Quais países além de Thiryn foram atingidos pelo terremoto.
- Que caminho os 34 países "neutrality" vão tomar quando as sub-ideologias (oligárquica, tribal, bandidos etc.) forem desenvolvidas — quais desses países já têm um destino em mente vs. quais estão totalmente em aberto.
- O que motiva ELD e GET a declararem guerra simultânea em SVD — coincidência de dados ou gancho narrativo pretendido?
- Relação entre THK e CZL (Lesc) — deliberadamente em aberto por enquanto.

---

## 16. Arquivos mais importantes consultados

- `common/country_tags/00_countries.txt` (57 tags)
- `history/countries/*.txt` (57 arquivos — capital/partido/líder/ideias/guerras)
- `history/states/*.txt` (506 arquivos — população/indústria/recursos, agregado via script)
- `history/units/*.txt` (divisões/navios por país)
- `common/national_focus/Thiryn.txt`, `Lesc.txt`
- `common/decisions/THK.txt`
- `events/NewsEvents.txt`, `events/AZ_formables.txt`
- `localisation/AZ_countries_l_english.yml`, `AZ_bookmarks_l_english.yml`, `AZ_country_briefings_l_english.yml`, `AZ_lore_l_english.yml`, `AZ_formables_l_english.yml`
- `common/bookmarks/1924.txt`

*Avisos: números de população/indústria/recursos foram **calculados** via script a partir dos arquivos reais. Contagens de divisões/navios são aproximadas (contagem de blocos, não leitura de equipamento/prontidão). A seção 2 contém decisões de lore fornecidas diretamente pelo autor — tratadas como canônicas a partir de agora.*
