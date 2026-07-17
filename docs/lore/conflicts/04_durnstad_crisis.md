# Crise de Durnstad

*Ver `00_CANON_RULES.md`, `gydian_expansion_doctrine.md` e `04_CONTENT_IMPLEMENTATION_MATRIX.md`.*

## Desambiguação obrigatória

- `DUH` — **Durnstad**: alvo da intervenção gydiana.
- `DTB` — **Durtenbach**: participante da Guerra das Três Bandeiras.

## Regra de conteúdo [CANON]

O genocídio em Durnstad deve ser tratado de forma histórica, política e não gráfica.

Pode ser representado por:

- censura;
- deportações;
- desaparecimentos;
- refugiados;
- destruição e falsificação de registros;
- relatórios diplomáticos;
- testemunhos;
- responsabilidade de autoridades;
- consequências internas e internacionais.

## Resumo [CANON]

Durnstad é a única anexação gydiana anterior à Grande Guerra que exige uma campanha militar realmente aberta.

A guerra não contradiz a garantia inicial de Gydian.

A garantia é parte do mecanismo de dominação.

## Progressão histórica

### 1. Proteção

Gydian garante formalmente Durnstad.

A garantia é vendida como defesa contra:

- revolução;
- Estados vizinhos;
- instabilidade helvariana;
- ameaças econômicas.

### 2. Dependência

Gydian amplia controle sobre:

- armas;
- crédito;
- treinamento;
- ferrovias;
- defesa;
- política externa;
- inteligência.

### 3. Exigências

Gydian exige:

- bases;
- conselheiros permanentes;
- controle alfandegário;
- repressão de opositores;
- alinhamento diplomático;
- acesso a infraestrutura estratégica.

### 4. Ruptura

O rei, governo, oficiais ou parlamento de Durnstad tenta recuperar soberania.

Pode:

- expulsar conselheiros;
- cancelar tratados;
- nacionalizar concessões;
- buscar garantia externa;
- prender colaboradores.

### 5. Pretexto

Gydian acusa Durnstad de:

- violar a garantia;
- ameaçar cidadãos pró-Gydian;
- colaborar com inimigos;
- permitir terrorismo;
- destruir a estabilidade regional.

### 6. Intervenção

Antes da declaração:

- Gydian remove ou abandona a garantia;
- apresenta ultimato;
- mobiliza tropas;
- bloqueia comunicações.

A guerra deve ser curta na expectativa gydiana, mas pode oferecer resistência real.

### 7. Ocupação

Após a vitória, Gydian:

- anexa ou submete Durnstad;
- reorganiza administração;
- prende opositores;
- desloca populações;
- destrói ou altera registros;
- encobre o genocídio.

## Encobrimento [CANON]

A informação pública inicial apresenta:

- “pacificação”;
- “restauração constitucional”;
- “proteção de civis”;
- “eliminação de terroristas”;
- “reintegração administrativa”.

Outros países recebem informações incompletas.

## Revelação gradual [PROPOSTA COERENTE COM O CANON]

O encobrimento pode falhar através de:

- refugiados;
- diplomatas;
- soldados desertores;
- documentos;
- fotografias ou registros;
- investigação de Helvaria;
- imprensa estrangeira;
- redes religiosas ou humanitárias.

A revelação não deve ocorrer automaticamente no mesmo dia da ocupação.

Ela pode aumentar:

```text
az_gye_continental_alarm
```

e produzir:

- perda de opinião;
- garantias contra Gydian;
- radicalização anti-gydiana;
- pressão em Sithius e Gengen;
- apoio à Helvaria;
- justificativa moral para coalizões.

## Cronologia

A crise ocorre antes da Grande Guerra Continental, provavelmente entre 1924 e 1925.

A data exata em relação à Guerra das Três Bandeiras permanece TBD.

Para evitar congestionamento narrativo, recomenda-se:

- dependência e ruptura durante 1924;
- intervenção ou ocupação em 1925;
- revelações entre 1925 e 1927.

Isso é recomendação de pacing, não data canônica definitiva.

## Caminhos alternativos

### Durnstad aceita tutela

- vira fantoche;
- evita guerra imediata;
- sofre erosão de soberania;
- pode rebelar-se durante a Grande Guerra.

### Durnstad encontra proteção externa

- Helvaria, Montia ou outro país intervém;
- Gydian recua ou amplia a crise;
- a Grande Guerra pode começar antecipadamente.

### Intervenção gydiana fracassa

- grande perda de prestígio;
- revoltas em Estados subordinados;
- fortalecimento precoce do bloco anti-gydiano.

## Implementação recomendada

### Flags

```text
az_duh_gydian_protection_active
az_duh_dependency_stage
az_duh_break_with_gydian
az_duh_ultimatum_rejected
az_duh_war_started
az_duh_occupation_active
az_duh_genocide_concealed
az_durnstad_truth_exposed
```

### Ordem técnica

1. remover garantia;
2. validar existência dos países;
3. criar war goal ou declarar guerra;
4. registrar início;
5. resolver ocupação uma vez;
6. aplicar encobrimento;
7. disparar notícia propagandística;
8. iniciar sistema separado de revelação.

## Testes obrigatórios

- garantia removida antes da guerra;
- Durnstad não confundido com Durtenbach;
- guerra não se repete;
- ocupação não dispara sem vitória;
- notícia não revela o genocídio imediatamente;
- revelação exige encobrimento prévio;
- save/load preserva estágio;
- alternativa de fantoche funciona;
- fallback se DUH for anexado por terceiro.
