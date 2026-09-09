// Verificador de layout — se pega en la consola del navegador con el deck abierto.
// El verificador de Node comprueba estructura; este comprueba lo único que Node no puede ver:
// si algún elemento se sale del slide de 1920x1080, por abajo o por la derecha.
// Atrapó 10 desbordes que solo se notaban al llegar a ese slide durante la sesión.
(() => {
  const W = 1920, H = 1080;
  const secs = [...document.querySelectorAll('deck-stage > section')];
  const malos = [];
  secs.forEach((s, i) => {
    const sr = s.getBoundingClientRect(), esc = sr.height / H;
    let abajo = 0, derecha = 0, culpable = '';
    s.querySelectorAll('.frame *').forEach(el => {
      const r = el.getBoundingClientRect();
      const b = (r.bottom - sr.top) / esc - H;
      const d = (r.right - sr.left) / esc - W;
      if (b > abajo) { abajo = b; culpable = el.className || el.tagName; }
      if (d > derecha) { derecha = d; culpable = el.className || el.tagName; }
    });
    if (abajo > 1 || derecha > 1) {
      malos.push({ slide: i + 1, label: s.dataset.label, desbordeAbajo: Math.round(abajo), desbordeDerecha: Math.round(derecha), culpable });
    }
  });
  console.log(malos.length
    ? `${malos.length} de ${secs.length} slides desbordan:`
    : `Sin desbordes: los ${secs.length} slides caben en 1920x1080.`);
  if (malos.length) console.table(malos);
  return { total: secs.length, desbordes: malos.length, malos };
})();
