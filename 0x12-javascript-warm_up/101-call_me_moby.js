#!/usr/bin/node

exports.callMeMoby = function runXtime (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
