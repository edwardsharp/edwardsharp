# zomg hiiiiii 🦦

ohey, i'm 3dwardsharp and i've been hackin' away for ...a while now; this my codez.

_see also:_ [edwardsharp.com](https://edwardsharp.com) | [edwardsharp.org](https://edwardsharp.org)

<!-- regenerate this index with: python3 update_index.py -->
<!-- featured-index:start -->
<table>
<tr><td rowspan="4" valign="top">2026</td><td><a href="#freqhole-tomb">freqhole tomb <img height="16" src="https://avatars.githubusercontent.com/u/223163300?s=60&v=4" alt=""></a></td><td><code>XL</code></td><td><code>cross-platform tauri app</code> <code>p2p</code> <code>Rust</code> <code>TypeScript</code></td></tr>
<tr><td><a href="#skein">freqhole skein 🧶</a></td><td><code>L</code></td><td><code>p2p</code> <code>canvas</code> <code>tauri</code> <code>Rust</code> <code>TypeScript</code></td></tr>
<tr><td><a href="#freqhole-playlistz">freqhole playlistz</a></td><td><code>L</code></td><td><code>p2p</code> <code>web-components</code> <code>TypeScript</code></td></tr>
<tr><td><a href="#pinkweather">pinkweather</a></td><td><code>L</code></td><td><code>microcontroller</code> <code>eink</code> <code>Python</code></td></tr>
<tr><td rowspan="3" valign="top">2025</td><td><a href="#ratcoord-">ratcoord 🐀</a></td><td><code>L</code></td><td><code>dev-tools</code> <code>TUI</code> <code>Rust</code></td></tr>
<tr><td><a href="#modelz">modelz</a></td><td><code>L</code></td><td><code>3d-printing</code> <code>microcontroller</code> <code>Eurorack</code></td></tr>
<tr><td><a href="#toidz">toidz</a></td><td><code>L</code></td><td><code>microcontroller</code> <code>audio</code> <code>data-viz</code> <code>JavaScript</code></td></tr>
<tr><td rowspan="3" valign="top">2024</td><td><a href="#emergency-index">Emergency Index</a></td><td><code>XL</code></td><td><code>performance art</code> <code>web archive</code> <code>$paid</code></td></tr>
<tr><td><a href="#youoke-">YOUOKE 🎤</a></td><td><code>L</code></td><td><code>Rust</code> <code>TypeScript</code> <code>websockets</code> <code>karaoke</code></td></tr>
<tr><td><a href="#estimate-schema">estimate-schema</a></td><td><code>M</code></td><td><code>dev-tools</code> <code>data</code> <code>TypeScript</code> <code>Zod</code></td></tr>
<tr><td rowspan="1" valign="top">2023</td><td><a href="#versionz">versionz</a></td><td><code>M</code></td><td><code>dev-tools</code> <code>experiment</code> <code>JavaScript</code></td></tr>
<tr><td rowspan="1" valign="top">2022</td><td><a href="#redux-key-nav">redux-key-nav</a></td><td><code>M</code></td><td><code>accessibility</code> <code>UI</code> <code>Redux</code> <code>TypeScript</code></td></tr>
<tr><td rowspan="1" valign="top">2021</td><td><a href="#marsh-coop">MARSH COOP</a></td><td><code>XL</code></td><td><code>e-commerce</code> <code>web</code> <code>React</code> <code>Ruby</code> <code>digitalocean infra</code> <code>$sweat-equity</code></td></tr>
<tr><td rowspan="3" valign="top">2018</td><td><a href="#ecotopiatoday-learning-from-cascadia">ecotopia.today: Learning from Cascadia</a></td><td><code>L</code></td><td><code>maps</code> <code>art</code> <code>Vue</code> <code>$paid</code></td></tr>
<tr><td><a href="#a-player">a-player</a></td><td><code>L</code></td><td><code>video</code> <code>accessibility</code> <code>web-components</code> <code>$paid</code></td></tr>
<tr><td><a href="#rebel-cricket">Rebel Cricket</a></td><td><code>L</code></td><td><code>e-commerce</code> <code>web</code> <code>$paid</code></td></tr>
<tr><td rowspan="1" valign="top">2014</td><td><a href="#binseq-objective-c">binseq: objective-c</a></td><td><code>L</code></td><td><code>apps</code> <code>audio</code> <code>Objective-C</code></td></tr>
</table>
<!-- featured-index:end -->

## 2026

### freqhole tomb <img height="16" src="https://avatars.githubusercontent.com/u/223163300?s=60&v=4" alt="">

`XL` `cross-platform tauri app` `p2p` `Rust` `TypeScript`

<i>self-hosted music + video library && web, android, and desktop clientz that talk http or p2p</i> <b><i>$FREE</i></b>

<p align="right">
  <a href="https://freqhole.net">freqhole.net</a><br>
  <a href="https://spume.freqhole.net">spume.freqhole.net</a><br>
</p>

<p>a music + video player that uses <a href="https://github.com/n0-computer/iroh">iroh</a> for peer-to-peer networking; web browser, mac, ios, android, windows, and linux builds. share yr music + video with yr friendz without a centralized server; workz great on raspberry pi.</p>

<p>i spent way way too much time building, i guess some kinda plex/spotify/subsonic/jellyfin/etc. clone. peer-to-peer is cool!</p>

**the mono repo:** [freqhole/tomb](https://github.com/freqhole/tomb) — server, shared libraries, web player, desktop/mobile clients, CLI, and a whole lot of sqlite migrations.

<a name="skein"></a>

### freqhole skein 🧶

`L` `p2p` `canvas` `tauri` `Rust` `TypeScript`

skein is, like, a miro clone? like a shared canvas-type-of thing that i used to share filez, collaborate on some mixtapez and weird star trek voyager re-editz. arrange things together on a interactive canvas with peer-to-peer netz.

the browser, desktop app, and optional always-on hub share Automerge documents and iroh blob transfers. it borrows identity, storage, and transport libraries from tomb, so these projects are very much tangled together.

<p align="right"><a href="https://github.com/freqhole/skein">source</a> / <a href="https://skein.freqhole.net">skein.freqhole.net</a></p>

### freqhole playlistz

`L` `p2p` `web-components` `TypeScript`

make some music playlistz in yr browser! a standalone playlist editor and player, for when the full media-library app is more than you need.

there are views for editing tracks, arranging playlists, adding covers, and sharing. it can build into a standalone HTML app or an embeddable web component, and shares libraries with the rest of freqhole.

<p align="right"><a href="https://github.com/freqhole/playlistz">source</a> / <a href="https://playlistz.freqhole.net">playlistz.freqhole.net</a></p>

### pinkweather

`L` `microcontroller` `eink` `Python`

yet another weather display for e-ink, in a lil' pink cloud i 3D printed. indoor temperature and humidity, a weather forecast, and severe-weather alertz, running on a Raspberry Pi Pico 2 W.

the project spans the microcontroller code, display layouts, weather-data plumbing, and a browser preview for trying out the screen without repeatedly flashing the hardware. the enclosure lives over in modelz.

<p align="right"><a href="https://github.com/edwardsharp/pinkweather">source</a> / <a href="https://edwardsharp.github.io/modelz/pinkweather/">case + CAD filez</a></p>

<table>
  <tr>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/model.jpeg"><img src="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/model.jpeg" height="160" alt="a side view of the pink cloud-shaped weather display"></a><br>
      the little cloud
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/model0.jpeg"><img src="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/model0.jpeg" height="160" alt="the pinkweather enclosure showing an e-ink forecast"></a><br>
      the forecast
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/current_image400x300.png"><img src="https://raw.githubusercontent.com/edwardsharp/pinkweather/main/misc/current_image400x300.png" height="160" alt="a preview of the pinkweather forecast screen"></a><br>
      the screen preview
    </td>
  </tr>
</table>

<hr/> 
<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/lichenbouboushian.work">lichenbouboushian.work</a></strong> <code>M</code></td>
    <td><code>art</code> <code>web</code></td>
    <td>a portfolio and archive for Lichen Bouboushian's work. <a href="https://edwardsharp.github.io/lichenbouboushian.work/">Pages</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/dvd-iso-rippr">dvd-iso-rippr</a></strong> <code>M</code></td>
    <td><code>video</code> <code>CLI</code> <code>Python</code></td>
    <td>turn DVD ISO / IMG filez into H.264/AAC MP4s with FFmpeg. interactive ripping, setup helpers, and tests.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/googy-slideshow-raspi-kiosk">googy-slideshow-raspi-kiosk</a></strong> <code>S</code></td>
    <td><code>raspberry pi</code> <code>Python</code></td>
    <td>googy slidez on a Raspberry Pi. use Raspberry Pi Imager app to build an sd card + add your google slides url to slideshow.txt; then plug into a raspberry pi and you're all set, easy peasy!</td>
  </tr>
</table>

## 2025

### ratcoord 🐀

`L` `dev-tools` `TUI` `Rust`

coordinate yr rat nest of code? i wanted to run a frontend app, a couple of linked packages, and a backend dev server without juggling a pile of terminals, so i cobbled together this process-orchestration thingy.

built with Ratatui: stdout and stderr become one timestamped, color-coded stream, with per-process visibility and log searching. each process has setup and teardown commands; regex matches in one process's output can trigger restart signals in another.

<table>
  <tr>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/ratcoord/main/assets/demo2x.gif"><img src="https://raw.githubusercontent.com/edwardsharp/ratcoord/main/assets/demo2x.gif" alt="a screen recording of the ratcoord terminal ui application"></a><br>
      tui demo gif
    </td>
    </td>
  </tr>
</table>

<p align="right"><a href="https://github.com/edwardsharp/ratcoord">source</a></p>

### modelz

`L` `3d-printing` `microcontroller` `Eurorack`

<i>a collection of artifacts from my semi-charmed 3d printing life.</i>

<p align="right"><a href="https://github.com/edwardsharp/modelz">source + print filez</a> / <a href="https://edwardsharp.github.io/modelz/">browse the models</a></p>

<table>
  <tr>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/performer-bttnz/index.jpeg"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/performer-bttnz/index.jpeg" height="160" alt="pink 3D-printed buttons installed on a Westlicht Performer sequencer"></a><br>
      <a href="https://edwardsharp.github.io/modelz/performer-bttnz/">performer buttonz</a>
    </td>
    <td align="center">
    <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/coffin-button/coffin-button.png"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/coffin-button/coffin-button.png" height="160" alt="CAD rendering of a coffin-shaped coat button"></a><br>
      <a href="https://edwardsharp.github.io/modelz/coffin-button/">a button for my coat</a>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/toidz/toidz.png"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/toidz/toidz.png" height="160" alt="CAD rendering of the coffin-shaped toidz enclosure and lid"></a><br>
      <a href="https://edwardsharp.github.io/modelz/toidz/">a coffin for toidz</a>
    </td>
  </tr>
</table>

<details>
<summary>more little objects</summary>

<table>
  <tr>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/midi2cv-face-plate/midi2cv-face-plate.png"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/midi2cv-face-plate/midi2cv-face-plate.png" height="160" alt="CAD rendering of the MIDI-to-CV module faceplate"></a><br>
      <a href="https://edwardsharp.github.io/modelz/midi2cv-face-plate/">MIDI-to-CV faceplate</a>
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/cord-comb/cord-comb.png"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/cord-comb/cord-comb.png" height="160" alt="CAD rendering of a patch-cable holder"></a><br>
      <a href="https://edwardsharp.github.io/modelz/cord-comb/">patch cable comb</a>
    </td>
    <td align="center">
       <a href="https://raw.githubusercontent.com/edwardsharp/modelz/main/performer-bttnz/8mm_hex.png"><img src="https://raw.githubusercontent.com/edwardsharp/modelz/main/performer-bttnz/8mm_hex.png" height="160" alt="CAD rendering of an 8 mm hex tool for Eurorack jack nuts"></a><br>
      <a href="https://edwardsharp.github.io/modelz/performer-bttnz/">a jack-nut tool</a>
    </td>
  </tr>
</table>

</details>

related code: [midi2cv](https://github.com/edwardsharp/midi2cv) / [toidz](https://github.com/edwardsharp/toidz) / [pinkweather](https://github.com/edwardsharp/pinkweather)

### toidz

`L` `microcontroller` `audio` `data-viz` `JavaScript`

some fiddlez with hardware sensors and software audio and graph viz. record movement with BNO08x sensors, then feed the logs into a browser to see and hear what happened.

the <a href="https://edwardsharp.github.io/toidz/bno08xviz/">web visualizer</a> combines D3 graphs, a Three.js view of orientation and acceleration, FFT analysis, and Web Audio experiments. example recordings are included, so you can poke around without first building the hardware. modelz has a little coffin-shaped enclosure for it.

<table>
  <tr>
  <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz.jpeg
      "><img src="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz.jpeg
      " alt="a picture of various electronic components mounted inside an altoids tin"></a><br>
      gutz
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz1.jpeg
      "><img src="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz1.jpeg
      " alt="a picture of accelerometer visualizations on an oled screen mounted in an altoids tin"></a><br>
      oled; toggle button, rgb led, & rotary encoder ui
    </td>
    <td align="center">
      <a href="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz2.jpeg
      "><img src="https://raw.githubusercontent.com/edwardsharp/toidz/main/bno08xviz/toidz2.jpeg
      " alt="a zoomed in view of accelerometer visualizations on an oled screen mounted in an altoids tin"></a><br>
      accelerometer viz
    </td>
  </tr>
</table>

<p align="right"><a href="https://github.com/edwardsharp/toidz">source</a> / <a href="https://edwardsharp.github.io/toidz/bno08xviz/">visualizer</a> / <a href="https://edwardsharp.github.io/toidz/">Pages</a> / <a href="https://edwardsharp.github.io/modelz/toidz/">enclosure</a></p>

<hr/> 
<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/peedeeeff">peedeeeff</a></strong> <code>S</code></td>
    <td><code>web-components</code> <code>JavaScript</code></td>
    <td>built for <a href="https://geoz.one/">geoz.one</a>; PDF pages become WebP images; a carousel web component lets you flip through them. <a href="https://edwardsharp.github.io/peedeeeff/">try it</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/futuredeathagency">futuredeathagency</a></strong> <code>S</code></td>
    <td><code>art</code> <code>web</code></td>
    <td>futuredeath.agency. <a href="http://futuredeath.agency/">site filled mostly with music + photo documentation from some select performances.</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/carp.rodeo">carp.rodeo</a></strong> <code>M</code></td>
    <td><code>web</code> <code>audio</code></td>
    <td>carp.rodeo, some data, and a mixtape page. <a href="http://carp.rodeo/">site</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/wild_ai_adventure">wild_ai_adventure</a></strong> <code>L</code></td>
    <td><code>experiment</code> <code>AI-assisted</code> <code>Rust</code></td>
    <td>my first claude adventure that started as a passkey demo grew into freqhole.</td>
  </tr>
</table>

## 2024

### Emergency Index

`XL` `performance art` `web archive` `$paid`

<i>an annual document of performance practice.</i>

started in 2017, this was a paid project funded through a New York State Council on the Arts grant. the work brought the publication's performance documentation onto the web, with an archive site, ways to browse the material, and a submission form for the last 4 volumes.

the main site uses Jekyll and Liquid to turn structured project content into static pages on GitHub Pages. the other repos also trace experiments in Rails, Angular, React, and SolidJS; the submission app uses React and Material UI and glitch hosting (rip 😔).

- **[emergencyindex/emergencyindex.com](https://github.com/emergencyindex/emergencyindex.com)** — the main site and publication archive. [site](https://emergencyindex.com/)
- **[emergency-index-submission](https://github.com/emergencyindex/emergency-index-submission)** — the project-submission form, built for editing and hosting on Glitch. [deployment](https://emergency-index-submission-2020.glitch.me/)
- **[edwardsharp/emergencyindex.com](https://github.com/edwardsharp/emergencyindex.com)** `fork` — my fork of the Jekyll site. [Pages](https://index.alveol.us/)
- **[emergencyindex_solid](https://github.com/edwardsharp/emergencyindex_solid)** — the SolidJS experiment. [site](https://solid.alveol.us)
- **[emergencyindex_react](https://github.com/edwardsharp/emergencyindex_react)** — the React prototype and component previews. [Pages / Storybook](https://edwardsharp.github.io/emergencyindex_react/)
- **[emergencyindex](https://github.com/edwardsharp/emergencyindex)** — earlier Angular and Rails implementations.
- **[alveol.us](https://github.com/edwardsharp/alveol.us)** `archived` — an earlier site and content archive, before the move to the main Emergency Index repo. [Pages](https://edwardsharp.github.io/alveol.us/) / [solidjs prototype demo](http://alveol.us)

### YOUOKE 🎤

`L` `Rust` `TypeScript` `websockets` `karaoke`

<i>karatube? youaoke? karayouoketube?? dunno. create a queue of youtube videos, maybe they're karaoke videoz. maybe you got a mic. ...maybe</i>

<p align="right"><a href="https://youoke.party">youoke.party</a><br><a href="https://github.com/edwardsharp/youoke/">github.com/edwardsharp/youoke</a></p>

<p>mostly a fun & funny way to yodel with frenz</p>

### estimate-schema

`M` `dev-tools` `data` `TypeScript` `Zod`

a functional-programming-inspired utility for figuring out what shape an API's data actually has. give it a bunch of sample records and it collects the keys, observed types, distinct values, and how often each field appears.

that gives you clues for writing a schema: a field present in every record is a different proposition from one that only appears sometimes, or switches between strings and numbers. the output is a guide for building something like a Zod schema, not a claim that the samples describe every possible response.

<p align="right"><a href="https://github.com/edwardsharp/estimate-schema">source + example</a></p>

<hr/> 
<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/midi2cv">midi2cv</a></strong> <code>L</code></td>
    <td><code>hardware</code> <code>MIDI</code> <code>Eurorack</code></td>
    <td>USB MIDI in, control voltages and gates out; a DIY Eurorack module. <a href="https://edwardsharp.github.io/modelz/midi2cv-face-plate/">printed panel</a></td>
  </tr>

</table>

## 2023

### versionz

`M` `dev-tools` `experiment` `JavaScript`

a lil' prototype exploring versioned exports! import several versions of the same package side by side, a bit like versioned HTTP imports in Deno, but using Node.js package subpaths.

the experiment keeps versioned builds under separate export paths and updates the package's export map as versions are added. old and new implementations can coexist in one program without pretending they're the same module. you probably shouldn't do this; still a fun thing to poke at.

<p align="right"><a href="https://github.com/edwardsharp/versionz">source + examples</a></p>

## 2022

### redux-key-nav

`M` `accessibility` `UI` `Redux` `TypeScript`

an opinionated proof-of-concept & demo for handling arrow-key navigation in React + Redux apps. more an exploration of a particular problem space than a finished, handles-everything library.

instead of inspecting the rendered DOM and guessing where focus should go, the app explicitly declares navigable rows, columns, and their exits. navigation state follows Redux's data flow, leaving room for application-specific rules and awkward edge cases.

<p align="right"><a href="https://github.com/edwardsharp/redux-key-nav">source</a> / <a href="https://edwardsharp.github.io/redux-key-nav/">demo</a></p>

## 2021

### MARSH COOP

`XL` `e-commerce` `web` `React` `Ruby` `digitalocean infra` `$sweat-equity`

<p align="right"><a href="https://marshlifeart.wordpress.com/">marshlifeart.wordpress.com</a></p>

my friends bought + renovated a building in St. Louis, MO that was previously a diner + industrial kitchen with three apartments above. they started a grocery coop and i helped build their e-commerce website where their members could browse both local inventory (local grown produce, restaurant items, etc) and a huge aggregation from various wholesale product catalog (UNFI and others) that needed a lot of data sanitization, formatting, and rules applied before members could order. really took off in the pandemic where all their members needed to order online and schedule pickup or delivery.

a storefront shopping cart, back-office tools, APIs, and product-data experiments spread across several repos.

- **[sorta-cart](https://github.com/marshlife-art/sorta-cart)** — the customer-facing React client. [site](https://marshcoop.org/)
- **[sorta-cart-admin](https://github.com/marshlife-art/sorta-cart-admin)** — the shop's admin UI. [deployment](https://admin.marshcoop.org/)
- **[sorta-cart-server](https://github.com/marshlife-art/sorta-cart-server)** — an Express API with authentication, Sequelize models, and PostgreSQL migrations.
- **[sorta-cart-services](https://github.com/marshlife-art/sorta-cart-services)** — shared abstractions for fetching data from local or remote services.
- **[react-marsh](https://github.com/marshlife-art/react-marsh)** `archived` — an earlier React prototype.
- **[spree](https://github.com/marshlife-art/spree)** `archived` — the earlier Spree store.
- **[spree_stockr](https://github.com/marshlife-art/spree_stockr)** — a Spree extension for creating products from uploaded XLSX and CSV files.
- **[csvdiffr](https://github.com/edwardsharp/csvdiffr)** `M` — match a smaller product list against a larger price sheet by the first column, returning the corresponding rows. [Glitch project](https://glitch.com/~descriptive-seeder) / [Docker image](https://hub.docker.com/r/3dwardsharp/csvdiffr/)
- **[edwardsharp/sorta-cart](https://github.com/edwardsharp/sorta-cart)** — a related Next.js, Supabase, and Square prototype. [deployment](https://sorta-cart.vercel.app)

## 2020

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/lorenebouboushian.org">lorenebouboushian.org</a></strong> <code>M</code></td>
    <td><code>art</code> <code>web</code> <code>fork</code></td>
    <td>an earlier artist site for Lorene Bouboushian, with Jekyll pages and image carousels.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/helloworld">helloworld</a></strong> <code>S</code></td>
    <td><code>dev-tools</code> <code>Docker</code></td>
    <td>a tiny Express HTTP server for checking container environment variables. <a href="https://hub.docker.com/r/3dwardsharp/helloworld/">image</a></td>
  </tr>
</table>

## 2019

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/edwardsharp.org">edwardsharp.org</a></strong> <code>S</code></td>
    <td><code>web</code> <code>Vue</code></td>
    <td>i was a tumblr once but now i'm here. <a href="http://edwardsharp.org">site</a> / <a href="https://edwardsharp.github.io/edwardsharp.org/">Pages</a> / <a href="https://edwardsharp.github.io/edwardsharp.org/storybook/">Storybook</a></td>
  </tr>
   <tr>
    <td><strong><a href="https://github.com/edwardsharp/edwardsharp.com">edwardsharp.com</a></strong> <code>S</code></td>
    <td><code>web</code> <code>links</code></td>
    <td>may these hyperlinkz reveal my digital self. <a href="http://edwardsharp.com">site</a></td>
  </tr>
</table>

## 2018

### ecotopia.today: Learning from Cascadia

`L` `maps` `art` `Vue` `$paid`

a paid project and collaboration with Brian Holmes. [ecotopia.today](http://ecotopia.today) brings together cartographic projects and writing about political ecology, at the intersection of art, science, philosophy, and activism.

i helped most with the Cascadia map visualization: a Vue and OpenLayers interface for exploring watersheds, dams, energy infrastructure, and the places and histories around them. the work combines map layers with text, image galleries, and navigation through Brian's research.

**[Learning from Cascadia](https://cascadia.ecotopia.today/#/watershed/acknowledgement)** is the atlas; the [project site](http://ecotopia.today) connects it to Brian's other maps and texts.

- **[ecotopia-today](https://github.com/edwardsharp/ecotopia-today)** — the Vue / OpenLayers app and map components. [Pages](https://edwardsharp.github.io/ecotopia-today/)
- **[ecotopia-today-mapseed](https://github.com/edwardsharp/ecotopia-today-mapseed)** — an earlier Mapseed API and container-setup prototype.

### a-player

`L` `video` `accessibility` `web-components` `$paid`

a paid, subcontracted gig to build an accessible video player for Spectrum help documentation. packaged as a web component so it could be emedded without making the surrounding site adopt a whole app framework. works in IE 💀

built around JWPlayer, with captions, searchable interactive transcripts, chapter support, and audio-description options. the work was about making help videos easier to navigate and use, not just getting a video rectangle onto the page.

<p align="right"><a href="https://github.com/edwardsharp/a-player">source</a> / <a href="https://edwardsharp.github.io/a-player/">demo</a> / <a href="https://www.webcomponents.org/element/@edwardsharp/a-player">component</a></p>

<a name="rebel-cricket"></a>

### Rebel Cricket

`L` `e-commerce` `web` `$paid`

paid work for Rebel Cricket screen printing. the code covers several generations of the site and shop experiments, with Angular, Rails, Polymer, and Sinatra implementations collected together.

the related apparel-design demo uses React and Fabric.js to place graphics on a garment template: a small canvas-based tool for trying out a design before it becomes something printed.

- **[rebelcricket](https://github.com/edwardsharp/rebelcricket)** — the site and application implementations.
- **[demo-gfx](https://github.com/edwardsharp/demo-gfx)** `M` — the apparel graphics editor. my first real React app. [demo](https://edwardsharp.github.io/demo-gfx/)

<hr/>
<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/puredata">puredata</a></strong> <code>M</code></td>
    <td><code>audio</code> <code>visuals</code> <code>Pure Data</code></td>
    <td>a patch collection: synths, samplers, controllers, video, and workshop experiments.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/lacuna">lacuna</a></strong> <code>M</code><br><a href="https://github.com/lacunaclub/wiki">lacunaclub/wiki</a></td>
    <td><code>art</code> <code>web</code></td>
    <td>LACUNA CLUB, plus a directory of wonderful thingz. <a href="http://lacuna.club/">site</a> / <a href="https://lacunaclub.github.io/wiki/">wiki</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/nginx-certbot">nginx-certbot</a></strong> <code>S</code></td>
    <td><code>infra</code> <code>Docker</code></td>
    <td>an Nginx proxy with Let's Encrypt certificate setup, renewal, and reloads in one container. <a href="https://hub.docker.com/r/3dwardsharp/nginx-certbot/">image</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/sched-datepicker">sched-datepicker</a></strong> <code>M</code></td>
    <td><code>UI</code> <code>web-components</code> <code>Polymer</code></td>
    <td>yet another datepicker. <a href="https://edwardsharp.github.io/sched-datepicker/">Pages</a> / <a href="https://edwardsharp.github.io/sched-datepicker/components/sched-datepicker/demo/index.html">component demo</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/notes">notes</a></strong> <code>S</code></td>
    <td><code>notes</code> <code>infra</code></td>
    <td>some notez on this and that and that other thing(z).</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/shrine-gdrive_storage">shrine-gdrive_storage</a></strong> <code>M</code></td>
    <td><code>storage</code> <code>Ruby</code> <code>fork</code></td>
    <td>Google Drive storage for Shrine, using a Google API service account. <a href="http://shrinerb.com/">Shrine</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/processing">processing</a></strong> <code>M</code></td>
    <td><code>art</code> <code>visuals</code> <code>Processing</code></td>
    <td>sketches, performance visuals, clocks, and occasional Android appz.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/schleifer">schleifer</a></strong> <code>M</code></td>
    <td><code>video</code> <code>realtime</code></td>
    <td>a YouTube TV experiment with Faye WebSockets on Heroku.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/python">python</a></strong> <code>M</code></td>
    <td><code>utility</code> <code>collection</code> <code>Python</code></td>
    <td>assorted scripts and experiments.</td>
  </tr>
</table>

## 2017

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/dotfilez">dotfilez</a></strong> <code>S</code></td>
    <td><code>dev-tools</code> <code>shell</code></td>
    <td>rc filez for making the terminal feel like home.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/javascript">javascript</a></strong> <code>M</code></td>
    <td><code>utility</code> <code>collection</code> <code>JavaScript</code></td>
    <td>this and that scripts that do weird, but sometimes handy, things.</td>
  </tr>
</table>

## 2016

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/been_said">been_said</a></strong> <code>S</code></td>
    <td><code>web</code> <code>tiny-thing</code></td>
    <td>it's all been said before... a tiny repo mostly based on <a href="https://jsfiddle.net/edwardsharp/1kqux0cb/">JSFiddle experiment</a>.</td>
  </tr>
</table>

## 2015

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/ruby-caldav">ruby-caldav</a></strong> <code>S</code></td>
    <td><code>calendar</code> <code>Ruby</code> <code>fork</code></td>
    <td>a Ruby CalDAV library, based on earlier implementations.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/bash">bash</a></strong> <code>M</code></td>
    <td><code>utility</code> <code>video</code> <code>shell</code></td>
    <td>scripts for video conversion, file management, and other handy thingz.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/example_sinatra_form">example_sinatra_form</a></strong> <code>S</code></td>
    <td><code>web</code> <code>Ruby</code> <code>fork</code></td>
    <td>a little Sinatra + Haml form, database writes, and emailed results. based on a paid client project.</td>
  </tr>
</table>

## 2014

### binseq: objective-c

`L` `apps` `audio` `Objective-C`

binseq is binary clock visualization (using processing.js) that was an iPhone app in the app store for a while.

this is the earlier app-making corner of my code archive: sequencers, clocks, interface experiments, and other crude projects.

<p align="right"><a href="https://github.com/edwardsharp/objective-c">source / app archive</a></p>

<hr/>
<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/quneo">quneo</a></strong> <code>S</code></td>
    <td><code>audio</code> <code>controllers</code></td>
    <td>some Quneo presetz.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/one_pager">one_pager</a></strong> <code>S</code></td>
    <td><code>web</code></td>
    <td>single-file HTML pages, one little piece of content at a time. <a href="http://edwardsharp.github.io/one_pager/">Pages</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/PPL_PD">PPL_PD</a></strong> <code>S</code></td>
    <td><code>audio</code> <code>workshops</code> <code>Pure Data</code></td>
    <td>patches from pure-data workshops at [Panoply Performance Lab.](http://panoplylab.org/)</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/touchOSC">touchOSC</a></strong> <code>S</code></td>
    <td><code>audio</code> <code>controllers</code></td>
    <td>a collection of TouchOSC modules.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/heroku_lumen00">heroku_lumen00</a></strong> <code>S</code></td>
    <td><code>API</code> <code>PHP</code> <code>experiment</code></td>
    <td>a little PHP app using the Twilio API and SDK.</td>
  </tr>
</table>

## 2013

<table>
  <tr>
    <td><strong><a href="https://github.com/micronemez/120todo">micronemez/120todo</a></strong> <code>S</code></td>
    <td><code>performance</code> <code>web</code></td>
    <td>a countdown timer for 120 todoz, made for a Future Death Toll performance at Panoply Performance Lab in 2013. <a href="http://120todo.micronemez.com/">site</a></td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/faye00">faye00</a></strong> <code>S</code></td>
    <td><code>audio</code> <code>realtime</code> <code>archived</code></td>
    <td>tune a synth sound with jsfx, then send it to everyone else connected via Faye (ruby web-sockets library).</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/micronemez">micronemez</a></strong> <code>L</code></td>
    <td><code>web</code> <code>audio</code> <code>experiment</code></td>
    <td>Rails-era site code, radio/streaming experiments, and assorted earlier implementations.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/raspi-puppet">raspi-puppet</a></strong> <code>S</code></td>
    <td><code>hardware</code> <code>infra</code></td>
    <td>Puppet manifests to bootstrap a Raspberry Pi.</td>
  </tr>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/esnet_">esnet_</a></strong> <code>S</code></td>
    <td><code>web</code></td>
    <td> some processing.js visualizations for <a href="http://edwardsharp.net/">edwardsharp.net</a></td>
  </tr>
</table>

## 2012

<table>
  <tr>
    <td><strong><a href="https://github.com/edwardsharp/midi">midi</a></strong> <code>S</code></td>
    <td><code>MIDI</code></td>
    <td>BCR2000 presets and MIDI configuration filez.</td>
  </tr>
</table>

[back to the top](#zomg-hiiiiii)
