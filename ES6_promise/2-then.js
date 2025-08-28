// 2-then.js
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => new Error())
    .finally(() => {
      // Always executed
      // eslint-disable-next-line no-console
      console.log('Got a response from the API');
    });
}
