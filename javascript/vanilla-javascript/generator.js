function* boom(x, y) {
  const first = yield x;
  console.log(first);
  const second = yield y;
  console.log(second)
}

const gen = boom(5,3);

console.log("function boom type", typeof(gen));

var first = gen.next();
console.log(first); // console will log { value: 5, done: false }


var second = gen.next('hello');  
console.log(second); // console will first log 'hello' then { value: 3, done: false }.

var third = gen.next('World'); // log Wolrd
console.log(third); // log { value: undefined, done: true }
