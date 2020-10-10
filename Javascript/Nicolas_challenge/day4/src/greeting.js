// <⚠️ DONT DELETE THIS ⚠️>
import './styles.css';
// <⚠️ /DONT DELETE THIS ⚠️>

const form = document.querySelector('.js-form'),
  input = form.querySelector('input'),
  greeting = document.querySelector('.js-greetings');

const userName = 'currentUser',
  SHOWING_CN = 'showing';

function saveName(text) {
  localStorage.setItem(userName, text);
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = input.value;
  paintGreeting(currentValue);
  saveName(currentValue);
}

function askForName() {
  form.classList.add(SHOWING_CN);
  form.addEventListener('submit', handleSubmit);
}

function paintGreeting(text) {
  form.classList.remove(SHOWING_CN);
  greeting.classList.add(SHOWING_CN);
  greeting.innerHTML = `Hello ${text}`;
}

function loadName() {
  const currentCountry = localStorage.getItem(countryCode);
  const currentUser = localStorage.getItem(userName) || null;
  if (currentUser === null) {
    askForName();
  } else {
    paintGreeting(currentUser);
  }
}

function init() {
  loadName();
}

init();
