# Guerra das Três Bandeiras

*Ver `00_CANON_RULES.md`, `02_MASTER_TIMELINE.md` e `04_CONTENT_IMPLEMENTATION_MATRIX.md`.*

## Resumo [CANON]

A Guerra das Três Bandeiras é o primeiro grande conflito internacional da campanha.

Começa entre **junho e setembro de 1924** e envolve três pretendentes à reunificação do antigo espaço helvariano:

| País | Tag | Projeto político |
|---|---|---|
| Durtenbach | `DTB` | reunificação monárquica e constitucional |
| Varadnia | `VRD` | reunificação socialista e revolucionária |
| Junta Helvariana | `HEL` | reunificação militar e centralizadora |

## Desambiguação obrigatória

- `DTB` — **Durtenbach**: participante da Guerra das Três Bandeiras.
- `DUH` — **Durnstad**: pequeno reino posteriormente invadido por Gydian.

Os dois países não podem ser confundidos em eventos, localisation, flags ou documentação.

## Situação em janeiro de 1924

Os três governos vivem uma paz armada.

- Durtenbach possui a estrutura monárquica e industrial mais estável.
- Varadnia controla um Estado socialista e milícias revolucionárias.
- A Junta controla o núcleo militar e institucional do antigo país.
- principados, ducados e Estados-tampão separam ou cercam os três concorrentes;
- nenhuma potência externa deseja uma reunificação independente e forte.

## Patrocinadores externos [CANON]

### Novasovia → Varadnia

Aproximadamente cinco meses após o início do cenário, Novasovia começa a fornecer:

- rifles e metralhadoras;
- munição;
- dinheiro;
- assessores;
- propaganda;
- organização clandestina.

Novasovia ainda se recupera de sua guerra civil e não envia inicialmente um Exército convencional.

### Gydian → Junta Helvariana

Gydian fornece:

- armamentos;
- crédito;
- assessores;
- inteligência;
- apoio logístico;
- possível apoio aéreo ou voluntários, conforme balanceamento.

Gydian espera que uma vitória da Junta produza uma Helvaria reunificada, mas dependente.

### Montia → Durtenbach

Montia atua secretamente por:

- financiamento;
- voluntários religiosos;
- hospitais e organizações de auxílio;
- propaganda;
- inteligência;
- redes paramilitares.

O extremismo religioso montiano pode gerar:

- conflitos sectários;
- repressão;
- escândalos internacionais;
- radicalização local.

O conteúdo deve permanecer político e histórico, sem descrição gráfica.

## Escalada durante 1924

### Janeiro–abril

- propaganda e infiltração aumentam;
- cada pretendente mobiliza fronteiras;
- Gydian aproxima-se da Junta;
- Montia estrutura auxílio clandestino;
- Novasovia avalia a capacidade de Varadnia.

### Maio–junho

- começam os carregamentos novasovianos;
- Durtenbach reprime células revolucionárias;
- Varadnia denuncia preparação de invasão;
- a Junta afirma que somente o Exército pode restaurar a unidade.

### Junho–setembro

O conflito começa após um incidente ainda não nomeado definitivamente.

**[PROPOSTA]** “Motim dos Arsenais Helvarianos” pode funcionar como estopim:

- arsenais antigos se rebelam ou mudam de lealdade;
- cada lado acusa outro de golpe;
- forças cruzam as antigas linhas de cessar-fogo;
- os três governos proclamam a reunificação.

O nome e a sequência exata permanecem TBD até aprovação.

## Rota histórica [CANON]

Durtenbach vence.

A vitória não deve ser uma simples anexação sem consequências. O processo histórico inclui:

1. desgaste de Varadnia;
2. cisão da Junta entre colaboracionistas gydianos e nacionalistas helvarianos;
3. aproximação entre Durtenbach e oficiais nacionalistas da Junta;
4. derrota dos setores colaboracionistas;
5. queda dos principais centros varadnianos;
6. formação de uma **Helvaria reunificada**;
7. concessões constitucionais, federais ou regionais para evitar nova guerra civil;
8. reorganização de um Exército veterano;
9. ruptura com a tutela gydiana.

A nova Helvaria torna-se o principal rival continental de Gydian.

## Vitórias alternativas [CANON]

### Vitória de Varadnia

Forma uma Helvaria socialista ou federativa revolucionária.

Consequências prováveis:

- aproximação com Novasovia;
- nacionalização;
- resistência monárquica;
- insurgência de antigos oficiais;
- ameaça revolucionária a Gydian e Montia.

O nome final e a estrutura constitucional permanecem TBD.

### Vitória da Junta

Forma uma Helvaria militar, centralizadora e autoritária.

Pode:

- permanecer subordinada a Gydian;
- romper com Gydian após a reunificação;
- perseguir monarquistas e socialistas;
- transformar-se num rival criado pelo próprio apoio gydiano.

## Relação com a Grande Guerra

Qualquer vencedor deve poder ocupar o papel funcional de rival continental de Gydian.

Na rota histórica, Durtenbach cumpre esse papel.

Nos caminhos alternativos:

- Varadnia pode liderar um bloco revolucionário;
- a Junta pode permanecer aliada a Gydian ou romper;
- a Crise de Astravern precisa possuir variantes para cada vencedor.

## Implementação recomendada

### Fase 1 — cadeia vertical mínima

1. inicializar variáveis de apoio;
2. iniciar apoio de Novasovia;
3. oferecer apoio gydiano à Junta;
4. ativar apoio secreto de Montia;
5. escalar tensão;
6. disparar o estopim;
7. iniciar a guerra uma única vez;
8. publicar uma notícia mundial.

### Fase 2 — resolução

- regras de capitulação;
- vencedor exclusivo;
- reunificação;
- integração de personagens e divisões;
- transferência segura de estados;
- remoção de guerras residuais;
- notícias de vitória;
- reação de Gydian, Montia e Novasovia.

## Flags conceituais

```text
az_three_banners_started
az_three_banners_ended
az_three_banners_winner_dtb
az_three_banners_winner_vrd
az_three_banners_winner_hel
az_helvaria_reunified
```

Somente uma flag de vencedor pode existir.

## Testes obrigatórios

- início entre junho e setembro;
- nenhum início duplicado;
- três lados corretos;
- patrocinadores não entram formalmente por engano;
- paz vanilla não encerra a guerra inadequadamente;
- vencedor único;
- reunificação após save/load;
- fallback se um beligerante for anexado por terceiro;
- variante da Crise de Astravern para cada vencedor.
