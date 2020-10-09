// <⚠️ DONT DELETE THIS ⚠️>
import './styles.css';
// <⚠️ /DONT DELETE THIS ⚠️>

const body = document.querySelector('body');

function resizeHandler() {
  if (window.innerWidth > 150) {
    body.style.background = 'red';
  }
  if (window.innerWidth > 300) {
    body.style.background = 'orange';
  }
  if (window.innerWidth > 450) {
    body.style.background = 'yellow';
  }
  if (window.innerWidth > 600) {
    body.style.background = 'green';
  }
  if (window.innerWidth > 750) {
    body.style.background = 'blue';
  }
  if (window.innerWidth > 900) {
    body.style.background = 'indigo';
  }
  if (window.innerWidth > 1050) {
    body.style.background = 'violet';
  }
  return;
}
// plz resize the window to the right side than to the left side :)

function init() {
  window.addEventListener('resize', resizeHandler);
}

init();
