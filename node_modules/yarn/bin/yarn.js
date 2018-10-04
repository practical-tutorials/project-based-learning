#!/usr/bin/env node

/* eslint-disable no-var */
/* eslint-disable flowtype/require-valid-file-annotation */
'use strict';

var ver = process.versions.node;
var majorVer = parseInt(ver.split('.')[0], 10);

if (majorVer < 4) {
  console.error('Node version ' + ver + ' is not supported, please use Node.js 4.0 or higher.');
  process.exit(1); // eslint-disable-line no-process-exit
} else {
  var dirPath = '../lib/';
  var v8CompileCachePath = dirPath + 'v8-compile-cache';
  var fs = require('fs');
  // We don't have/need this on legacy builds and dev builds
  if (fs.existsSync(v8CompileCachePath)) {
    require(v8CompileCachePath);
  }

  // Just requiring this package will trigger a yarn run since the
  // `require.main === module` check inside `cli/index.js` will always
  // be truthy when built with webpack :(
  var cli = require(dirPath + 'cli');
  if (!cli.autoRun) {
    cli.default().catch(function(error) {
      console.error(error.stack || error.message || error);
      process.exitCode = 1;
    });
  }
}
