# Grande Guerra Continental

*Ver `00_CANON_RULES.md`, `02_MASTER_TIMELINE.md` e `03_GEOPOLITICAL_BLOCKS.md`.*

## Resumo [CANON]

A Grande Guerra Continental começa aproximadamente em **1927**.

Ela não é uma cópia direta da Segunda Guerra Mundial real. Nasce das crises próprias de Azarya:

- expansão diplomática e territorial gydiana;
- Guerra das Três Bandeiras;
- formação de uma Helvaria reunificada;
- submissão de Astravern;
- guerra e ocupação de Durnstad;
- aproximação de Zauern, Gengen e Sithius com Gydian;
- disputa por Estados-tampão;
- entrada posterior de Novasovia;
- expansão de Karyō contra Liangor.

## Rival principal [CANON]

Na rota histórica, o principal rival continental de Gydian é a Helvaria reunificada sob liderança de Durtenbach.

A guerra não começa porque Novasovia invade ou lidera uma coalizão. Novasovia entra depois e decide a escala do conflito.

## Estopim histórico — Crise de Astravern [CANON]

Astravern torna-se aliado subordinado ou fantoche de Gydian durante 1924–1926.

Em 1927:

1. opositores removem ou tentam remover ministros pró-Gydian;
2. o governo astraverniano tenta sair da dependência ou sofre uma revolta interna;
3. Gydian envia tropas para “restaurar a ordem”;
4. Helvaria mobiliza, pois Astravern funciona como plataforma de invasão;
5. ocorre confronto de fronteira;
6. Gydian apresenta ultimato;
7. Helvaria recusa;
8. começa a guerra.

O nome exato do incidente e o texto final do ultimato permanecem TBD.

## Exigências possíveis do ultimato

- desmobilização helvariana;
- reconhecimento do governo pró-Gydian;
- expulsão de refugiados astravernianos;
- fim do apoio a opositores;
- direito permanente de passagem;
- desmilitarização de regiões fronteiriças.

A lista final deve ser aprovada antes da implementação.

## Bloco gydiano histórico provável

- Gydian;
- Astravern subordinado;
- Fervonia integrada ou fantoche;
- Durnstad ocupado;
- Zauern sob pressão;
- Gengen inclinado ao bloco;
- Sithius como aliado oportunista;
- outros Estados menores dependentes.

A composição deve ser dinâmica. Nenhum país deve entrar apenas por data se seguiu rota alternativa.

## Resistência continental histórica provável

- Helvaria reunificada;
- Estados-tampão que rejeitaram Gydian;
- países garantidos por Helvaria;
- possíveis remanescentes de Torronese;
- Thiryn ou Gengen em rotas alternativas;
- apoio indireto de Novasovia;
- apoio clandestino ou político de Montia.

## Thiryn e Gengen

### Oferta a Thiryn

Gydian promete devolver:

- Mominches;
- Doia;
- Haifa;

em troca de adesão, acesso e alinhamento.

### Pressão sobre Gengen

Gydian exige:

- base em Haifa;
- acesso ferroviário em Doia;
- união econômica;
- presença militar;
- alinhamento contra Helvaria.

Gengen tende historicamente a aceitar ou entrar no bloco, mas pode perceber a perda de soberania.

### Caminhos

- Gengen com Gydian;
- Thiryn com Gydian;
- resistência conjunta;
- neutralidade;
- nova guerra regional.

## Sithius

Na rota histórica, Sithius entra como aliado menor e oportunista de Gydian.

Motivos:

- recuperar prestígio;
- reivindicar portos e ilhas;
- revisar perdas territoriais;
- obter ajuda para modernizar a Marinha;
- acreditar numa vitória gydiana rápida.

Pode também resistir ou ser anexado.

## Montia

Montia não precisa liderar a guerra.

Pode:

- apoiar Helvaria;
- provocar conflitos religiosos;
- cometer excessos por forças voluntárias;
- negociar separadamente;
- permanecer formalmente distante;
- aproveitar a guerra para expandir influência.

## Novasovia — quem decide a escala [CANON]

Novasovia não começa a Grande Guerra.

Inicialmente:

- fornece equipamentos;
- financia remanescentes varadnianos;
- apoia Helvaria de forma indireta;
- mobiliza;
- influencia revoltas.

Entra posteriormente após:

- pressão gydiana;
- incidente fronteiriço;
- ataque preventivo;
- tentativa gydiana de destruir bases ou movimentos apoiados por Novasovia.

Quando Novasovia entra, abre novo front e transforma a guerra numa mobilização continental de massa.

O gatilho e a data exatos permanecem TBD.

## Continente oriental

A guerra oriental não precisa começar ao mesmo tempo que a Crise de Astravern.

### Karyō

Aproveita a distração de Hesperon para ampliar a guerra contra Liangor.

### Liangor

Tenta centralizar governadores e resistir.

### Orvena

Permanece neutra, fornece recursos e depois entra quando rotas, ilhas, navios ou bases são atacados.

A entrada de Orvena transforma a Grande Guerra Continental na **Grande Guerra de Azarya**.

## Vencedores alternativos da Guerra das Três Bandeiras

A Grande Guerra deve funcionar com:

### Helvaria de Durtenbach

Principal rota histórica anti-gydiana.

### Helvaria varadniana

Pode liderar bloco revolucionário ligado a Novasovia.

### Helvaria da Junta

Pode:

- permanecer no bloco gydiano;
- romper e tornar-se rival;
- causar uma Grande Guerra com composição diferente.

Portanto, o estopim de 1927 precisa de variantes e fallbacks.

## Condições técnicas recomendadas

A guerra histórica não deve depender apenas de `date > 1927.1.1`.

Condições sugeridas:

- Gydian existe;
- existe um Estado helvariano reunificado ou rival funcional;
- Astravern está subordinado, ocupado ou em crise;
- a Grande Guerra ainda não começou;
- ao menos parte da expansão gydiana ocorreu;
- não existe guerra equivalente já ativa entre os blocos.

## Fallbacks

Caso Astravern não esteja sob Gydian:

- crise em Fervonia;
- tentativa de completar anexação de Durnstad;
- ultimato a um Estado das Marchas;
- pressão sobre Helvaria;
- crise em Haifa ou Doia.

Astravern continua sendo o estopim histórico principal.

## Flags conceituais

```text
az_great_war_started
az_great_war_astravern_trigger
az_great_war_fallback_trigger
az_nsa_entered_great_war
az_orv_entered_world_war
```

## Regras de implementação

1. formar facções dinamicamente;
2. adicionar apenas países elegíveis;
3. respeitar rotas alternativas;
4. aplicar declarações uma única vez;
5. publicar notícias depois da guerra iniciar;
6. não usar `news` vanilla;
7. impedir paz branca automática inadequada;
8. prever tags anexadas ou governos trocados;
9. testar save/load;
10. permitir início antecipado apenas por cadeias específicas.

## Testes obrigatórios

- rota histórica de Durtenbach;
- vitória de Varadnia;
- vitória da Junta pró-Gydian;
- vitória da Junta anti-Gydian;
- Astravern independente;
- Astravern fantoche;
- Gengen gydiano;
- Thiryn gydiano;
- resistência conjunta;
- Sithius neutro, aliado ou anexado;
- entrada tardia de Novasovia;
- guerra oriental separada;
- entrada de Orvena;
- nenhuma declaração duplicada;
- nenhuma facção com país inexistente.
