import './styles.css';

// You're gonna need this
const NINE_HOURS_MILLISECONDS = 32400000;
const clock = document.querySelector('.js-clock');

const _second = 1000;
const _minute = _second * 60;
const _hour = _minute * 60;
const _day = _hour * 24;

function getTime() {
  // Don't delete this.
  const xmasDay = new Date('2020-12-24:00:00:00+0900');
  const currentTime = new Date();

  const distance = xmasDay - currentTime;
  if (distance < 0) {
    clearInterval();
    clock.innerHTML = 'Merry Christmas!!';
  }

  let days = Math.floor(distance / _day);
  let hours = Math.floor((distance % _day) / _hour);
  let minutes = Math.floor((distance % _hour) / _minute);
  let seconds = Math.floor((distance % _minute) / _second);
  clock.innerHTML = `${days < 10 ? '0' + days : days}d ${
    hours < 10 ? '0' + hours : hours
  }h ${minutes < 10 ? '0' + minutes : minutes}m ${
    seconds < 10 ? '0' + seconds : seconds
  }s`;
}

function init() {
  getTime();
  setInterval(getTime, 1000);
}
init();
