#!/usr/bin/node

import { createRequire } from 'module';
const require = createRequire(import.meta.url);

exports.add = function (a, b) {
  return (a + b);
};

