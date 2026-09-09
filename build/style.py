# -*- coding: utf-8 -*-
"""Hoja de estilo del deck — molde de capacitacion-gemini-payjoy con los tokens
reales de Casa de las Baterias (mercadeocasabat/src/styles/global.css)."""

CSS = r"""
  :root{
    /* Identidad de Casa de las Baterias — tomada de
       casabat-comparador-cliente/app/globals.css y del logotipo. */
    --brand:#1C5C92;       /* azul del logotipo — acento sobre papel */
    --brand-br:#4E9BD6;    /* el mismo azul aclarado para leerse sobre tinta */
    --brand-dark:#14456E;
    --brand-light:#E8F1F9;
    --red:#C0392B;         /* rojo del techo y de #SomosEnergia */
    --red-br:#E0685A;

    --ink:#0E2A43;         /* tinta: el azul de marca llevado a fondo */
    --ink-2:#14456E;
    --bone:#EDF3F9;
    --bone-2:#A9C2D8;
    --paper:#F4F7FB;       /* --canvas del comparador */
    --graphite:#0F172A;    /* --foreground del comparador */
    --graphite-2:#334155;
    --muted-d:#7D9AB5;
    --muted-l:#5B6B81;     /* --color-slate-500 */
    --rule-d:#1D4E7A;
    --rule-l:#D3DEEA;

    --pad-x: 96px;
    --pad-top: 80px;

    --display: 'Antonio', 'Arial Narrow', 'Helvetica Neue', sans-serif;
    --sans: 'Inter', system-ui, -apple-system, sans-serif;
    --mono: 'IBM Plex Mono', 'Menlo', monospace;
  }

  html,body{margin:0;background:#000;font-family:var(--sans);}

  deck-stage > section{
    background:var(--ink);
    color:var(--bone);
    font-family:var(--sans);
    overflow:hidden;
  }
  section.paper{background:var(--paper);color:var(--graphite);}

  .frame{
    width:100%;height:100%;
    padding:var(--pad-top) var(--pad-x) 120px;
    box-sizing:border-box;
    display:flex;flex-direction:column;
    position:relative;
  }

  /* === Footer === */
  .footer{
    position:absolute;
    left:var(--pad-x);right:var(--pad-x);bottom:36px;
    display:flex;justify-content:space-between;align-items:center;
    font-size:24px;
    letter-spacing:0.28em;
    text-transform:uppercase;
    color:var(--muted-d);
  }
  section.paper .footer{color:var(--muted-l);}
  .footer .lhs{display:flex;gap:36px;align-items:center;white-space:nowrap;}
  .footer .lhs span, .footer .rhs{white-space:nowrap;}
  .footer .dot{width:5px;height:5px;background:var(--brand-br);border-radius:50%;flex-shrink:0;}
  section.paper .footer .dot{background:var(--brand);}
  .footer .rhs{letter-spacing:0.3em;font-variant-numeric:tabular-nums;}

  /* === Top rail === */
  .top-rail{
    display:flex;align-items:center;justify-content:space-between;
    font-size:24px;font-weight:500;
    letter-spacing:0.25em;text-transform:uppercase;
    color:var(--muted-d);gap:24px;
  }
  .top-rail > span{white-space:nowrap;}
  section.paper .top-rail{color:var(--muted-l);}
  .top-rail .sep{width:24px;height:1px;background:currentColor;display:inline-block;margin:0 14px;vertical-align:middle;opacity:.6;}

  h1.display, h2.display{
    font-family:var(--display);
    font-weight:600;line-height:1.0;
    letter-spacing:-0.01em;margin:0;
  }

  .label{
    font-size:24px;letter-spacing:0.28em;text-transform:uppercase;
    font-weight:500;color:var(--muted-d);
  }
  section.paper .label{color:var(--muted-l);}
  .label.acc{color:var(--brand);}
  section:not(.paper) .label.acc{color:var(--brand-br);}

  /* La marca va sobre una placa blanca: el logotipo original tiene fondo blanco
     y sobre la tinta azul se leería como un recorte sucio. */
  .marca{
    position:absolute;top:58px;right:var(--pad-x);
    width:168px;height:168px;background:#fff;padding:13px;
    box-sizing:border-box;object-fit:contain;
  }

  /* ===== Portada ===== */
  .cover .frame{justify-content:space-between;}
  .cover h1{
    font-family:var(--display);
    font-size:250px;line-height:0.95;letter-spacing:-0.01em;
    font-weight:700;color:var(--bone);margin:0;
  }
  .cover h1 .acc{color:var(--brand-br);}
  .cover .eyebrow{
    font-size:24px;letter-spacing:0.4em;text-transform:uppercase;
    color:var(--brand-br);margin-bottom:64px;font-weight:500;
  }
  .cover .sub{
    font-family:var(--sans);font-size:34px;line-height:1.3;font-weight:300;
    color:var(--bone-2);max-width:1300px;margin-top:60px;
  }

  /* ===== Agenda ===== */
  .agenda-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px 64px;margin-top:36px;}
  .ag-block{padding:20px 0 0;border-top:1px solid var(--rule-d);}
  section.paper .ag-block{border-top-color:var(--rule-l);}
  .ag-block .bnum{
    font-family:var(--mono);font-size:22px;color:var(--brand-br);
    letter-spacing:0.18em;text-transform:uppercase;font-weight:500;margin-bottom:14px;
  }
  section.paper .ag-block .bnum{color:var(--brand);}
  .ag-block h3{
    font-family:var(--display);font-size:40px;line-height:1.05;
    font-weight:600;margin:0 0 14px;letter-spacing:0;
  }
  .ag-block ul{margin:0;padding:0;list-style:none;}
  .ag-block li{
    font-size:23px;padding:7px 0;
    display:flex;justify-content:space-between;align-items:baseline;
    border-bottom:1px solid var(--rule-d);color:var(--bone-2);
  }
  section.paper .ag-block li{border-bottom-color:var(--rule-l);color:var(--graphite-2);}
  .ag-block li:last-child{border-bottom:none;}
  .ag-block li span{color:var(--muted-d);font-variant-numeric:tabular-nums;letter-spacing:0.15em;font-size:22px;white-space:nowrap;flex-shrink:0;margin-left:16px;}
  section.paper .ag-block li span{color:var(--muted-l);}

  /* Lista de materiales: archivo a la izquierda, para qué sirve a la derecha */
  ul.files{margin:0;padding:0;list-style:none;}
  ul.files li{
    display:block;padding:10px 0;border-bottom:1px solid var(--rule-d);
    color:var(--bone-2);font-size:22px;
  }
  section.paper ul.files li{border-bottom-color:var(--rule-l);color:var(--graphite-2);}
  ul.files li:last-child{border-bottom:none;}
  ul.files li code{
    font-family:var(--mono);font-size:19px;background:none;padding:0;
    color:var(--brand);display:block;margin-bottom:3px;
    overflow-wrap:anywhere;
  }
  section:not(.paper) ul.files li code{color:var(--brand-br);}
  ul.files li span{display:block;line-height:1.3;font-size:21px;}

  /* ===== Divider de bloque ===== */
  .section-div .frame{padding-top:96px;padding-bottom:96px;}
  .section-div .block-no{
    font-family:var(--display);font-size:560px;line-height:0.78;
    letter-spacing:-0.03em;color:var(--brand-br);font-weight:700;margin:0;
  }
  .section-div h1{
    font-family:var(--display);font-size:112px;line-height:1.02;
    letter-spacing:-0.01em;font-weight:600;color:var(--bone);margin:0;max-width:1500px;
  }
  .section-div .layout{display:grid;grid-template-columns:520px 1fr;gap:64px;align-items:end;margin:auto 0;}
  .section-div .meta{
    margin-top:64px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px;
    border-top:1px solid var(--rule-d);padding-top:28px;grid-column:1 / -1;
  }
  .section-div .meta div{font-size:23px;color:var(--bone-2);line-height:1.45;}
  .section-div .meta div b{
    display:block;color:var(--muted-d);font-weight:500;font-size:22px;
    letter-spacing:0.25em;text-transform:uppercase;margin-bottom:12px;
  }

  /* ===== Teoria + demo externa ===== */
  .teoria{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;margin-top:28px;}
  .teoria .label{display:block;margin-bottom:18px;}
  ol.ideas{margin:0;padding:0;list-style:none;counter-reset:idea;}
  ol.ideas li{
    counter-increment:idea;padding:0 0 20px 56px;position:relative;
    font-size:24px;line-height:1.42;color:var(--graphite-2);
  }
  section:not(.paper) ol.ideas li{color:var(--bone-2);}
  ol.ideas li::before{
    content:counter(idea,decimal-leading-zero);
    position:absolute;left:0;top:1px;font-family:var(--display);font-weight:700;
    font-size:34px;color:var(--brand);line-height:1;
  }
  section:not(.paper) ol.ideas li::before{color:var(--brand-br);}
  ol.ideas li b{display:block;font-family:var(--display);font-weight:600;font-size:30px;
    color:var(--graphite);margin-bottom:6px;line-height:1.1;}
  section:not(.paper) ol.ideas li b{color:var(--bone);}

  .demo{background:var(--brand-light);border-left:4px solid var(--brand);padding:26px 30px;}
  section:not(.paper) .demo{background:rgba(78,155,214,0.12);border-left-color:var(--brand-br);}
  .demo .label{color:var(--brand);margin-bottom:14px;}
  section:not(.paper) .demo .label{color:var(--brand-br);}
  .demo a.url{
    display:block;font-family:var(--mono);font-size:22px;color:var(--brand-dark);
    text-decoration:underline;text-underline-offset:5px;margin-bottom:22px;overflow-wrap:anywhere;
  }
  section:not(.paper) .demo a.url{color:var(--bone);}
  .demo ol.steps li{font-size:22px;padding-bottom:12px;}
  .demo .observa{
    margin:16px 0 0;padding-top:16px;border-top:1px solid var(--rule-l);
    font-size:22px;line-height:1.4;color:var(--graphite-2);
  }
  section:not(.paper) .demo .observa{color:var(--bone-2);border-top-color:var(--rule-d);}
  .demo .observa b{
    display:block;color:var(--brand);font-size:20px;text-transform:uppercase;
    letter-spacing:0.26em;margin-bottom:10px;font-weight:600;font-family:var(--sans);
  }
  section:not(.paper) .demo .observa b{color:var(--brand-br);}

  /* ===== Ejercicios ===== */
  .ex-header{display:grid;grid-template-columns:170px 1fr;gap:40px;margin:36px 0 28px;align-items:end;}
  .ex-num-label{font-size:22px;letter-spacing:0.3em;text-transform:uppercase;color:var(--muted-l);margin-bottom:10px;font-weight:500;}
  .ex-num{font-family:var(--display);font-size:150px;line-height:0.8;letter-spacing:-0.02em;color:var(--brand);font-weight:700;}
  section:not(.paper) .ex-num{color:var(--brand-br);}
  .ex-title{
    font-family:var(--display);font-size:58px;line-height:1.08;
    letter-spacing:0;font-weight:600;color:var(--graphite);margin:0;
  }
  section:not(.paper) .ex-title{color:var(--bone);}
  .ex-tool{margin-top:12px;font-size:23px;color:var(--muted-l);font-weight:400;}
  section:not(.paper) .ex-tool{color:var(--bone-2);}
  .ex-tool b{color:var(--brand);text-transform:uppercase;letter-spacing:0.18em;font-size:22px;margin-right:14px;font-weight:600;}
  section:not(.paper) .ex-tool b{color:var(--brand-br);}

  .ex-body{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
  .col{display:flex;flex-direction:column;gap:24px;}

  .concept-block .label{margin-bottom:16px;display:block;}
  .concept{font-family:var(--display);font-size:33px;line-height:1.16;color:var(--graphite);font-weight:600;}
  section:not(.paper) .concept{color:var(--bone);}
  .concept b{color:var(--brand);font-weight:600;}
  section:not(.paper) .concept b{color:var(--brand-br);}

  .steps-block .label{margin-bottom:18px;display:block;}
  ol.steps{margin:0;padding:0;list-style:none;counter-reset:step;}
  ol.steps li{
    counter-increment:step;padding:0 0 14px 52px;position:relative;
    font-size:23px;line-height:1.4;color:var(--graphite-2);
  }
  section:not(.paper) ol.steps li{color:var(--bone-2);}
  ol.steps li::before{
    content:counter(step,decimal-leading-zero);
    position:absolute;left:0;top:0;
    font-family:var(--mono);font-weight:500;font-size:22px;
    color:var(--brand);letter-spacing:0.06em;
  }
  section:not(.paper) ol.steps li::before{color:var(--brand-br);}
  ol.steps li:last-child{padding-bottom:0;}
  ol.steps li b{color:var(--graphite);font-weight:700;}
  section:not(.paper) ol.steps li b{color:var(--bone);}

  /* Tarjeta de prompt */
  .prompt-card{
    background:var(--ink);color:var(--bone);border-radius:0;
    padding:28px 32px;font-family:var(--mono);font-size:22px;line-height:1.45;
    position:relative;border-left:4px solid var(--brand-br);
  }
  /* Densidad segun cuanto texto lleva el prompt: el slide nunca debe desbordar. */
  .prompt-card.dense{font-size:20px;line-height:1.36;padding:24px 28px;}
  .prompt-card.dense .label{margin-bottom:18px;}
  .prompt-card.denser{font-size:18px;line-height:1.32;padding:20px 24px;}
  .prompt-card.denser .label{margin-bottom:14px;font-size:20px;}
  .prompt-card.dense p{margin-bottom:9px;}
  .prompt-card.denser p{margin-bottom:8px;}
  section:not(.paper) .prompt-card{background:var(--paper);color:var(--graphite);border-left:4px solid var(--brand);}
  .prompt-card .label{
    color:var(--brand-br);margin-bottom:22px;display:block;
    font-family:var(--sans);font-size:22px;letter-spacing:0.28em;
  }
  section:not(.paper) .prompt-card .label{color:var(--brand);}
  .prompt-card p{margin:0 0 10px;}
  .prompt-card p:last-child{margin-bottom:0;}
  .prompt-card .kw{color:var(--brand-br);font-weight:500;}
  section:not(.paper) .prompt-card .kw{color:var(--brand);}

  /* Resultado esperado */
  .result{padding:14px 0 0;border-top:1px solid var(--rule-l);font-size:22px;line-height:1.38;color:var(--graphite-2);}
  section:not(.paper) .result{color:var(--bone-2);border-top-color:var(--rule-d);}
  .result b{
    color:var(--brand);display:block;font-size:22px;text-transform:uppercase;
    letter-spacing:0.28em;margin-bottom:14px;font-weight:500;font-family:var(--sans);
  }
  section:not(.paper) .result b{color:var(--brand-br);}

  /* Aviso de limite — honestidad sobre lo que la IA no hace */
  .caveat{
    margin-top:10px;border-left:4px solid var(--red);padding:10px 16px;
    font-size:18.5px;line-height:1.36;color:var(--graphite-2);background:rgba(192,57,43,0.07);
  }
  section:not(.paper) .caveat{color:var(--bone-2);background:rgba(224,104,90,0.12);}
  /* solo el primer <b> es el rotulo; los demas son enfasis dentro del texto */
  .caveat > b:first-child{color:var(--red);text-transform:uppercase;letter-spacing:0.2em;font-size:17px;font-weight:600;display:block;margin-bottom:6px;}
  .caveat b{color:var(--graphite);font-weight:600;}
  section:not(.paper) .caveat > b:first-child{color:var(--red-br);}
  section:not(.paper) .caveat b{color:var(--bone);}

  /* ===== Tres pasos / tarjetas ===== */
  .howto-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;margin-top:64px;}
  .howto-card{border-top:1px solid var(--rule-l);padding-top:32px;}
  section:not(.paper) .howto-card{border-top-color:var(--rule-d);}
  .howto-card .n{font-family:var(--display);font-size:104px;color:var(--brand);line-height:0.88;font-weight:700;margin-bottom:32px;letter-spacing:-0.02em;}
  section:not(.paper) .howto-card .n{color:var(--brand-br);}
  .howto-card h3{font-family:var(--display);font-size:40px;font-weight:600;margin:0 0 18px;line-height:1.12;}
  .howto-card p{font-size:23px;line-height:1.45;color:var(--graphite-2);margin:0;}
  section:not(.paper) .howto-card p{color:var(--bone-2);}

  /* ===== Diagnostico / cifras ===== */
  .stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:48px;margin-top:64px;}
  .stat .label{display:block;margin-bottom:16px;}
  .stat b{
    font-family:var(--display);font-size:136px;line-height:0.95;color:var(--brand-br);
    font-weight:700;letter-spacing:-0.02em;margin-bottom:24px;
    display:flex;align-items:flex-end;min-height:130px;
  }
  /* Valores que son palabras y no cifras: caben en su columna sin invadir la vecina. */
  .stat b.word{font-size:72px;line-height:1.06;letter-spacing:-0.01em;}
  section.paper .stat b{color:var(--brand);}
  .stat p{font-size:22px;line-height:1.4;color:var(--bone-2);margin:0;}
  section.paper .stat p{color:var(--graphite-2);}

  /* ===== Dos columnas contrapuestas ===== */
  .contraste{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:26px;}
  .cc{padding-top:18px;border-top:3px solid var(--brand);}
  .cc.no{border-top-color:var(--red);}
  .cc .label{display:block;margin-bottom:12px;color:var(--brand);}
  .cc.no .label{color:var(--red);}
  section:not(.paper) .cc .label{color:var(--brand-br);}
  section:not(.paper) .cc.no .label{color:var(--red-br);}
  .cc h3{font-family:var(--display);font-size:44px;font-weight:600;line-height:1.06;margin:0 0 16px;color:var(--graphite);}
  section:not(.paper) .cc h3{color:var(--bone);}
  .cc ul{margin:0;padding:0;list-style:none;}
  .cc li{font-size:23px;line-height:1.42;color:var(--graphite-2);padding:9px 0 9px 26px;position:relative;}
  section:not(.paper) .cc li{color:var(--bone-2);}
  .cc li::before{content:'';position:absolute;left:0;top:19px;width:12px;height:2px;background:var(--brand);}
  .cc.no li::before{background:var(--red);}
  section:not(.paper) .cc li::before{background:var(--brand-br);}
  section:not(.paper) .cc.no li::before{background:var(--red-br);}
  .cc li b{color:var(--graphite);font-weight:600;}
  section:not(.paper) .cc li b{color:var(--bone);}
  .cc-cierre{
    margin:28px 0 0;padding-top:18px;border-top:1px solid var(--rule-l);
    font-size:25px;line-height:1.4;color:var(--graphite);max-width:1560px;
  }
  section:not(.paper) .cc-cierre{color:var(--bone);border-top-color:var(--rule-d);}
  .cc-cierre b{color:var(--brand);font-weight:600;}
  section:not(.paper) .cc-cierre b{color:var(--brand-br);}

  /* ===== Rejilla de tarjetas (anexos) ===== */
  .intro-cards{font-size:23px;line-height:1.45;color:var(--graphite-2);max-width:1560px;margin:16px 0 0;}
  section:not(.paper) .intro-cards{color:var(--bone-2);}
  .cards-grid{display:grid;gap:26px 40px;margin-top:26px;}
  .tc{border-top:2px solid var(--brand);padding-top:16px;}
  section:not(.paper) .tc{border-top-color:var(--brand-br);}
  .tc h3{font-family:var(--display);font-size:31px;font-weight:600;margin:0 0 8px;line-height:1.08;color:var(--graphite);}
  section:not(.paper) .tc h3{color:var(--bone);}
  .tc .cuando{font-size:20px;line-height:1.35;color:var(--graphite-2);margin:0 0 8px;}
  section:not(.paper) .tc .cuando{color:var(--bone-2);}
  .tc .ej{font-family:var(--mono);font-size:17.5px;line-height:1.35;color:var(--brand);margin:0;
    background:var(--brand-light);padding:8px 10px;}
  section:not(.paper) .tc .ej{color:var(--bone);background:rgba(78,155,214,0.14);}

  /* ===== Gobernanza ===== */
  .gov-grid{margin-top:56px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px;}
  .gov-item{border-top:2px solid var(--brand-br);padding-top:28px;}
  section.paper .gov-item{border-top-color:var(--brand);}
  .gov-item h3{font-family:var(--display);font-size:36px;font-weight:600;margin:0 0 18px;line-height:1.16;}
  .gov-item p{font-size:22px;color:var(--bone-2);line-height:1.5;margin:0;}
  section.paper .gov-item p{color:var(--graphite-2);}

  /* ===== Cierre ===== */
  .closing h1{
    font-family:var(--display);font-size:190px;line-height:0.98;letter-spacing:-0.01em;
    font-weight:700;margin:0;color:var(--bone);
  }
  .closing h1 .acc{color:var(--brand-br);}
  .closing .layout{margin:auto 0;}
  .closing .next{margin-top:48px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px;border-top:1px solid var(--rule-d);padding-top:36px;}
  .closing .next p{font-size:23px;line-height:1.5;color:var(--bone-2);margin:0;}
  .closing .next .lbl{color:var(--brand-br);font-size:22px;letter-spacing:0.25em;text-transform:uppercase;margin-bottom:14px;font-weight:500;display:block;}

  /* Los nombres de archivo son enlaces al material: se abre sin salir del deck. */
  a.mat{text-decoration:none;border-bottom:1px solid currentColor;color:inherit;}
  a.mat code{cursor:pointer;}
  a.mat:hover code,a.mat:focus-visible code{background:rgba(28,92,146,0.22);}
  section:not(.paper) a.mat:hover code,section:not(.paper) a.mat:focus-visible code{background:rgba(78,155,214,0.3);}
  a.mat:focus-visible{outline:2px solid var(--brand-br);outline-offset:2px;}
  a.mat::after{content:' \2197';font-family:var(--sans);font-size:0.78em;opacity:.75;}
  ul.files a.mat::after{content:none;}

  code{font-family:var(--mono);font-size:0.94em;background:rgba(28,92,146,0.12);padding:1px 8px;border-radius:2px;color:var(--brand);}
  section:not(.paper) code{background:rgba(78,155,214,0.18);color:var(--brand-br);}
"""
