/* Shared code-copy controls and native recorded-demo playback. No model code. */

// Static highlighting stays readable without JavaScript; these controls only copy text.
for (const pre of document.querySelectorAll('.rlql-prose .highlight pre')) {
  const container = pre.closest('.highlighter-rouge') || pre.closest('.highlight');
  if (!container || container.querySelector('.rlql-code-toolbar')) continue;
  const toolbar = document.createElement('div'); toolbar.className = 'rlql-code-toolbar';
  const label = document.createElement('span'); label.textContent = 'Code example';
  const button = document.createElement('button'); button.type = 'button'; button.textContent = 'Copy code';
  button.addEventListener('click', async () => {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(pre.textContent);
      else {
        const field = document.createElement('textarea'); field.value = pre.textContent; field.style.position = 'fixed'; field.style.opacity = '0'; document.body.append(field); field.select();
        const copied = document.execCommand('copy'); field.remove(); button.focus(); if (!copied) throw new Error('Copy unavailable');
      }
      button.textContent = 'Copied';
    } catch { button.textContent = 'Select text to copy'; }
  });
  toolbar.append(label, button); container.prepend(toolbar);
}

// Each figure owns its playback state. Scrolling never overrides a reader's pause.
for (const nativeDemo of document.querySelectorAll('[data-native-demo]')) {
  const image = nativeDemo.querySelector('[data-native-image]');
  const button = nativeDemo.querySelector('[data-native-play]');
  const controls = nativeDemo.querySelector('[data-native-controls]');
  if (!image || !button || !controls || !image.dataset.gifSrc) continue;
  const motionPreference = matchMedia('(prefers-reduced-motion: reduce)');
  let playing = false, userPaused = false, observer = null;
  image.dataset.posterSrc = image.getAttribute('src');
  function setPlaying(next) {
    playing = next;
    image.src = playing ? image.dataset.gifSrc : image.dataset.posterSrc;
    button.textContent = playing ? 'Pause real agent GIF' : 'Play real agent GIF';
    button.setAttribute('aria-pressed', String(playing));
  }
  function disarmAutoplay() {
    if (observer) { observer.disconnect(); observer = null; }
  }
  // Start once from the first frame in view. Reduced motion keeps the still poster.
  function armAutoplay() {
    if (playing || userPaused || motionPreference.matches || observer) return;
    if (!('IntersectionObserver' in window)) { setPlaying(true); return; }
    observer = new IntersectionObserver(entries => {
      if (!entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= 0.4)) return;
      disarmAutoplay();
      if (!userPaused && !motionPreference.matches) setPlaying(true);
    }, { threshold: 0.4 });
    observer.observe(image);
  }
  controls.hidden = false;
  button.addEventListener('click', () => {
    disarmAutoplay(); userPaused = playing; setPlaying(!playing);
  });
  motionPreference.addEventListener('change', () => {
    if (motionPreference.matches) { disarmAutoplay(); setPlaying(false); } else armAutoplay();
  });
  armAutoplay();
}
