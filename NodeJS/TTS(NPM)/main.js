const prompt = require('prompt');
const googleTTS = require('google-tts-api');
const open = require('open');

prompt.start();

prompt.get(['message'], function (err, result) {
  googleTTS(result.message , 'en', 1)   // speed normal = 1 (default), slow = 0.24
  .then(function (url) {
    console.log(url); // https://translate.google.com/translate_tts?...
    (async () => {
      await open(url, {app: 'chrome'});
  })();
  })
  .catch(function (err) {
    console.error(err.stack);
  });
});
 


