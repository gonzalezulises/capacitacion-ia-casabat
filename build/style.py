# -*- coding: utf-8 -*-
"""Hoja de estilo del deck — molde de capacitacion-gemini-payjoy con los tokens
reales de Casa de las Baterias (mercadeocasabat/src/styles/global.css)."""

CSS = r"""
  :root{
    /* Tokens de Casa de las Baterias — tomados de mercadeocasabat/src/styles/global.css */
    --ink:#0A1322;        /* --color-bg (dark) */
    --ink-2:#0E1A30;      /* --color-bg2 (dark) */
    --bone:#EAEEF5;       /* --color-ink (dark) */
    --bone-2:#A6B2C7;     /* --color-ink-dim (dark) */
    --paper:#F4F7F5;      /* --color-surface (light) */
    --graphite:#141715;   /* --color-ink (light) */
    --graphite-2:#2A2E2B;
    --muted-d:#8494AC;    /* --color-ink-mute (dark) */
    --muted-l:#6D7570;    /* --color-ink-mute (light) */
    --rule-d:#1A2F50;     /* --color-surface2 (dark) */
    --rule-l:#D3DBD6;
    --green:#289448;      /* --color-green (light) — acento sobre papel */
    --green-br:#2FAE57;   /* --color-green (dark) — acento sobre tinta */
    --cyan:#1FACC0;       /* --color-cyan */
    --red:#C32421;        /* --color-red-acc */
    --gold:#A97F14;       /* --color-gold */

    --pad-x: 96px;
    --pad-top: 80px;

    --display: 'Antonio', 'Arial Narrow', 'Helvetica Neue', sans-serif;
    --sans: 'Roboto', system-ui, -apple-system, sans-serif;
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
  .footer .dot{width:5px;height:5px;background:var(--green-br);border-radius:50%;flex-shrink:0;}
  section.paper .footer .dot{background:var(--green);}
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
  .label.acc{color:var(--green);}
  section:not(.paper) .label.acc{color:var(--green-br);}

  /* ===== Portada ===== */
  .cover .frame{justify-content:space-between;}
  .cover h1{
    font-family:var(--display);
    font-size:250px;line-height:0.95;letter-spacing:-0.01em;
    font-weight:700;color:var(--bone);margin:0;
  }
  .cover h1 .acc{color:var(--green-br);}
  .cover .eyebrow{
    font-size:24px;letter-spacing:0.4em;text-transform:uppercase;
    color:var(--green-br);margin-bottom:64px;font-weight:500;
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
    font-family:var(--mono);font-size:22px;color:var(--green-br);
    letter-spacing:0.18em;text-transform:uppercase;font-weight:500;margin-bottom:14px;
  }
  section.paper .ag-block .bnum{color:var(--green);}
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
    color:var(--green);display:block;margin-bottom:3px;
    overflow-wrap:anywhere;
  }
  section:not(.paper) ul.files li code{color:var(--green-br);}
  ul.files li span{display:block;line-height:1.3;font-size:21px;}

  /* ===== Divider de bloque ===== */
  .section-div .frame{padding-top:96px;padding-bottom:96px;}
  .section-div .block-no{
    font-family:var(--display);font-size:560px;line-height:0.78;
    letter-spacing:-0.03em;color:var(--green-br);font-weight:700;margin:0;
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

  /* ===== Ejercicios ===== */
  .ex-header{display:grid;grid-template-columns:170px 1fr;gap:40px;margin:36px 0 28px;align-items:end;}
  .ex-num-label{font-size:22px;letter-spacing:0.3em;text-transform:uppercase;color:var(--muted-l);margin-bottom:10px;font-weight:500;}
  .ex-num{font-family:var(--display);font-size:150px;line-height:0.8;letter-spacing:-0.02em;color:var(--green);font-weight:700;}
  section:not(.paper) .ex-num{color:var(--green-br);}
  .ex-title{
    font-family:var(--display);font-size:58px;line-height:1.08;
    letter-spacing:0;font-weight:600;color:var(--graphite);margin:0;
  }
  section:not(.paper) .ex-title{color:var(--bone);}
  .ex-tool{margin-top:12px;font-size:23px;color:var(--muted-l);font-weight:400;}
  section:not(.paper) .ex-tool{color:var(--bone-2);}
  .ex-tool b{color:var(--green);text-transform:uppercase;letter-spacing:0.18em;font-size:22px;margin-right:14px;font-weight:600;}
  section:not(.paper) .ex-tool b{color:var(--green-br);}

  .ex-body{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
  .col{display:flex;flex-direction:column;gap:24px;}

  .concept-block .label{margin-bottom:16px;display:block;}
  .concept{font-family:var(--display);font-size:33px;line-height:1.16;color:var(--graphite);font-weight:600;}
  section:not(.paper) .concept{color:var(--bone);}
  .concept b{color:var(--green);font-weight:600;}
  section:not(.paper) .concept b{color:var(--green-br);}

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
    color:var(--green);letter-spacing:0.06em;
  }
  section:not(.paper) ol.steps li::before{color:var(--green-br);}
  ol.steps li:last-child{padding-bottom:0;}
  ol.steps li b{color:var(--graphite);font-weight:700;}
  section:not(.paper) ol.steps li b{color:var(--bone);}

  /* Tarjeta de prompt */
  .prompt-card{
    background:var(--ink);color:var(--bone);border-radius:0;
    padding:28px 32px;font-family:var(--mono);font-size:22px;line-height:1.45;
    position:relative;border-left:4px solid var(--green-br);
  }
  /* Densidad segun cuanto texto lleva el prompt: el slide nunca debe desbordar. */
  .prompt-card.dense{font-size:20px;line-height:1.36;padding:24px 28px;}
  .prompt-card.dense .label{margin-bottom:18px;}
  .prompt-card.denser{font-size:18px;line-height:1.32;padding:20px 24px;}
  .prompt-card.denser .label{margin-bottom:14px;font-size:20px;}
  .prompt-card.dense p{margin-bottom:9px;}
  .prompt-card.denser p{margin-bottom:8px;}
  section:not(.paper) .prompt-card{background:var(--paper);color:var(--graphite);border-left:4px solid var(--green);}
  .prompt-card .label{
    color:var(--green-br);margin-bottom:22px;display:block;
    font-family:var(--sans);font-size:22px;letter-spacing:0.28em;
  }
  section:not(.paper) .prompt-card .label{color:var(--green);}
  .prompt-card p{margin:0 0 10px;}
  .prompt-card p:last-child{margin-bottom:0;}
  .prompt-card .kw{color:var(--green-br);font-weight:500;}
  section:not(.paper) .prompt-card .kw{color:var(--green);}

  /* Resultado esperado */
  .result{padding:16px 0 0;border-top:1px solid var(--rule-l);font-size:22px;line-height:1.38;color:var(--graphite-2);}
  section:not(.paper) .result{color:var(--bone-2);border-top-color:var(--rule-d);}
  .result b{
    color:var(--green);display:block;font-size:22px;text-transform:uppercase;
    letter-spacing:0.28em;margin-bottom:14px;font-weight:500;font-family:var(--sans);
  }
  section:not(.paper) .result b{color:var(--green-br);}

  /* Aviso de limite — honestidad sobre lo que la IA no hace */
  .caveat{
    margin-top:14px;border-left:4px solid var(--gold);padding:12px 18px;
    font-size:19px;line-height:1.38;color:var(--graphite-2);background:rgba(169,127,20,0.07);
  }
  section:not(.paper) .caveat{color:var(--bone-2);background:rgba(232,184,66,0.10);}
  .caveat b{color:var(--gold);text-transform:uppercase;letter-spacing:0.2em;font-size:17px;font-weight:600;display:block;margin-bottom:6px;}
  section:not(.paper) .caveat b{color:#E8B842;}

  /* ===== Tres pasos / tarjetas ===== */
  .howto-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;margin-top:64px;}
  .howto-card{border-top:1px solid var(--rule-l);padding-top:32px;}
  section:not(.paper) .howto-card{border-top-color:var(--rule-d);}
  .howto-card .n{font-family:var(--display);font-size:104px;color:var(--green);line-height:0.88;font-weight:700;margin-bottom:32px;letter-spacing:-0.02em;}
  section:not(.paper) .howto-card .n{color:var(--green-br);}
  .howto-card h3{font-family:var(--display);font-size:40px;font-weight:600;margin:0 0 18px;line-height:1.12;}
  .howto-card p{font-size:23px;line-height:1.45;color:var(--graphite-2);margin:0;}
  section:not(.paper) .howto-card p{color:var(--bone-2);}

  /* ===== Diagnostico / cifras ===== */
  .stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:48px;margin-top:64px;}
  .stat .label{display:block;margin-bottom:16px;}
  .stat b{
    font-family:var(--display);font-size:136px;line-height:0.95;color:var(--green-br);
    font-weight:700;letter-spacing:-0.02em;margin-bottom:24px;
    display:flex;align-items:flex-end;min-height:130px;
  }
  /* Valores que son palabras y no cifras: caben en su columna sin invadir la vecina. */
  .stat b.word{font-size:72px;line-height:1.06;letter-spacing:-0.01em;}
  section.paper .stat b{color:var(--green);}
  .stat p{font-size:22px;line-height:1.4;color:var(--bone-2);margin:0;}
  section.paper .stat p{color:var(--graphite-2);}

  /* ===== Gobernanza ===== */
  .gov-grid{margin-top:56px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px;}
  .gov-item{border-top:2px solid var(--green-br);padding-top:28px;}
  section.paper .gov-item{border-top-color:var(--green);}
  .gov-item h3{font-family:var(--display);font-size:36px;font-weight:600;margin:0 0 18px;line-height:1.16;}
  .gov-item p{font-size:22px;color:var(--bone-2);line-height:1.5;margin:0;}
  section.paper .gov-item p{color:var(--graphite-2);}

  /* ===== Cierre ===== */
  .closing h1{
    font-family:var(--display);font-size:190px;line-height:0.98;letter-spacing:-0.01em;
    font-weight:700;margin:0;color:var(--bone);
  }
  .closing h1 .acc{color:var(--green-br);}
  .closing .layout{margin:auto 0;}
  .closing .next{margin-top:48px;display:grid;grid-template-columns:repeat(3,1fr);gap:48px;border-top:1px solid var(--rule-d);padding-top:36px;}
  .closing .next p{font-size:23px;line-height:1.5;color:var(--bone-2);margin:0;}
  .closing .next .lbl{color:var(--green-br);font-size:22px;letter-spacing:0.25em;text-transform:uppercase;margin-bottom:14px;font-weight:500;display:block;}

  code{font-family:var(--mono);font-size:0.94em;background:rgba(40,148,72,0.12);padding:1px 8px;border-radius:2px;color:var(--green);}
  section:not(.paper) code{background:rgba(47,174,87,0.16);color:var(--green-br);}
"""
