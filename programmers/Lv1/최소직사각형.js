function solution(sizes) {
  const r = sizes.map(([w, h]) => (w < h ? [h, w] : [w, h]));

  let mw = 0;
  let mh = 0;
  r.forEach(([w, h]) => {
    mw = Math.max(mw, w);
    mh = Math.max(mh, h);
  });
  return mw * mh;
}
