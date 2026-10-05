# Guida rapida — Sonos Remote Local 0.2.8

App Berry per **TC002, display 52×16**, con firmware AWTRIX NG ufficiale, versione 0.2.8 verificata su firmware 1.2.0. Comunica direttamente con Sonos sulla rete locale: durante l'uso non servono Home Assistant, MQTT o un computer.

## Installazione

[Pagina AWTRIX Hub](https://awtrix.de/flow/mH4KFyXKLosV) · [Release GitHub 0.2.8](https://github.com/lucaamo/tc002-sonos-local/releases/tag/v0.2.8). Includi i due moduli richiesti durante l’installazione dal catalogo. Per aggiornare, sostituisci entrambi i moduli (protocollo 0.2.4, UI 0.2.8) e l’app 0.2.8, mantenendo gli stessi nomi per conservare le impostazioni.

Nell'editor Scripts / Berry del TC002 salva, in questo ordine:

1. `modules/sonos_local_protocol.ax` con nome **sonos_local_protocol**.
2. `modules/sonos_local_ui.ax` con nome **sonos_local_ui**.
3. `apps/sonos_local_probe.ax` con nome **sonos_local_probe**.

Apri le impostazioni dell'app, inserisci l'IP di un lettore Sonos in **IP Sonos iniziale / Seed IP** e scegli **Lingua / Language → Italiano o English**. Salva e avvia **Sonos Remote Local**. Riavvia l'app quando cambi lingua. I nomi dei dispositivi e dei contenuti arrivano da Sonos.

## Uso

| Comando | Funzione |
| --- | --- |
| Ruota la ghiera nei menu | Scorre le voci |
| Clic breve sulla ghiera | Conferma; durante la riproduzione, play / pausa |
| Tieni premuta la ghiera | Indietro; dalla riproduzione apre il menu |
| Ruota la ghiera durante una playlist | Traccia precedente / successiva, se supportata dalla sorgente |
| Ruota la ghiera durante la radio | Stazione preferita precedente / successiva |
| Tasti superiori sinistro / destro | Volume − / + del lettore selezionato; pressione prolungata ripete |
| Tasto centrale breve | Guida ai comandi |
| Tasto centrale prolungato | Esce al carosello AWTRIX |

Nel menu **Player / Lettore** scegli la stanza. In **Playlists / Playlist** o **Radio** scegli il contenuto e premi la ghiera. **Now playing / In riproduzione** torna alla schermata di ascolto; **Refresh favorites / Aggiorna preferiti** rilegge i cataloghi.

Le playlist includono i preferiti dei servizi e le playlist salvate in Sonos. La schermata radio mostra nome e logo della stazione, con artista e titolo del brano sulla seconda riga quando disponibili. In assenza di metadati leggibili, oppure in pausa/arresto/avvio, mostra stanza, volume e stato; i nomi tecnici dei file audio restano nascosti. Dodici stazioni hanno simboli nativi 16×16; puoi disattivarli in **Loghi radio personali / Custom radio logos**.

Quando cambi radio mentre Sonos è occupato, l'ultima stazione richiesta resta visibile e viene avviata dopo la richiesta in corso. L'attesa massima è configurabile; i comandi audio non vengono ripetuti automaticamente dopo un errore.

## Limiti da conoscere

Le playlist vengono **aggiunte alla coda Sonos esistente**, senza svuotarla. L'app usa i gruppi già configurati, ma non crea gruppi, coppie stereo o configurazioni Sub / surround. Il volume agisce sulla stanza selezionata; i comandi di riproduzione sul coordinatore del gruppo. I servizi musicali mantengono i propri requisiti di account e connessione internet.

È una beta della comunità, basata sull'interoperabilità UPnP di Sonos. La disponibilità e la decodifica delle immagini dipendono dalla sorgente e dal firmware. L'avvio reale di una playlist è stato confermato; non tutte le combinazioni di servizi, gruppi e comandi audio sono state verificate. Il precedente progetto Sonos Remote con Home Assistant resta separato.

Consulta anche [installazione e problemi comuni](INSTALLATION.md) e [licenza](../LICENSE.md).
