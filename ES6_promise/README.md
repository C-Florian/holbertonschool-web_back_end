# ES6 Promises

Holberton School project — practicing **JavaScript (ES6) Promises**: creation, composition, error handling, `then/catch/finally`, and helpers (`Promise.all`, `Promise.race`, `Promise.allSettled`, etc.).  
Code is tested with **Jest** and linted with **ESLint**.

---

## Learning Objectives

By the end of this project, you should be able to:
- Explain what a **Promise** is (how/why/what)
- Use `then`, `catch`, and `finally`
- Use Promise helpers: `Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.resolve`, `Promise.reject`
- Throw errors and handle them with `try/catch`
- Use the `await` operator and `async` functions

---

## Requirements

- Ubuntu 20.04 LTS
- **Node.js 20.x** and **npm 9/10**
- ES Modules (`"type": "module"`)
- All files end with a newline
- Tests: **Jest** → `npm run test`
- Lint: **ESLint** → `npm run lint`
- **All functions must be exported**

---

## Setup

> Run these from the `ES6_promise/` directory.

1) Install Node.js 20.x (if needed):
```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs
node -v
npm -v
