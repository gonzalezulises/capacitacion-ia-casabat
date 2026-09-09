// Verificador de layout — se pega en la consola del navegador con el deck abierto.
// El verificador de Node comprueba estructura; este comprueba lo único que Node no puede ver:
// si algún elemento invade la banda del footer o se sale por la derecha.
// Medir contra el borde del slide no basta: el footer es absoluto y el contenido lo tapa antes.
(() => {
  const W = 1920, H = 1080;
  const secs = [...document.querySelectorAll('deck-stage > section')];
  const malos = [];
  secs.forEach((s, i) => {
    const sr = s.getBoundingClientRect(), esc = sr.height / H;
    const f = s.querySelector('.footer');
    const tope = f ? (f.getBoundingClientRect().top - sr.top) / esc - 8 : H;
    let abajo = 0, derecha = 0, culpable = '';
    s.querySelectorAll('.frame *').forEach(el => {
      if (el.closest('.footer')) return;
      const r = el.getBoundingClientRect();
      const b = (r.bottom - sr.top) / esc - tope;
      const d = (r.right - sr.left) / esc - W;
      if (b > abajo) { abajo = b; culpable = el.className || el.tagName; }
      if (d > derecha) { derecha = d; culpable = el.className || el.tagName; }
    });
    if (abajo > 1 || derecha > 1) {
      malos.push({ slide: i + 1, label: s.dataset.label, invadeFooter: Math.round(abajo), desbordeDerecha: Math.round(derecha), culpable });
    }
  });
  console.log(malos.length
    ? `${malos.length} de ${secs.length} slides desbordan:`
    : `Sin desbordes: los ${secs.length} slides caben sin invadir el footer.`);
  if (malos.length) console.table(malos);
  return { total: secs.length, desbordes: malos.length, malos };
})();
