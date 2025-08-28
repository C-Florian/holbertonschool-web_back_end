// 3-all.js
import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      // eslint-disable-next-line no-console
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
      return true;
    })
    .catch(() => {
      // eslint-disable-next-line no-console
      console.log('Signup system offline');
      return false;
    });
}
