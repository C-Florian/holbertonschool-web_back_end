// full_server/server.js
import express from 'express';
import router from './routes/index.js';

const app = express();
app.use('/', router);

// IMPORTANT: écoute + log pour voir si ça démarre bien
app.listen(1245, () => {
  console.log('✅ Server listening on http://127.0.0.1:1245');
});

export default app; // IMPORTANT pour les tests