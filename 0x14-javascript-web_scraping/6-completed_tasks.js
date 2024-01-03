#!/usr/bin/node

const httpRequest = require('request');
const url = process.argv[2];

httpRequest(url, function (error, res, body) {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    const completedTasksByUser = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completedTasksByUser[task.userId] === undefined) {
          completedTasksByUser[task.userId] = 1;
        } else {
          completedTasksByUser[task.userId]++;
        }
      }
    }
    console.log(completedTasksByUser);
  } else {
    console.log('An error occurred. Status code: ' + res.statusCode);
  }
});
