#!/usr/bin/node

// Using JSONPlaceholder, display no of completed tasks by user

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
