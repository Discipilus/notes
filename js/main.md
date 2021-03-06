
# Arror function
``` js
const sq = (x) => x * x;
let arr = ['1', '2', '3', '4'];
let res = arr
   .map((x) => parseInt(x))
   .filter((num) => num % 2)
   .reduce((max, value) => Math.max(max, value), 0);
```

# Rest parameter
```js
function max(a, b, ...other_params) {
    // console.log(other_params);
}
max(11, 22, 33, 44, 55);
```

# Spread operator
```js
const arr1 = [1, 2, 3, 4];
const arr2 = [5, 6, 7];
res = [...arr1, ...arr2];
//console.log(res);
res = [...arr1, 1000];
// console.log(res);

const persone = {
    name: {
        first_n: 'Peter',
        last_n: 'Smith',
    },
    age: 27,
}
const {name:{first_n, last_n}} = persone;
// console.log(first_n, last_n);
const {name:{first_n: firstName, last_n: lastName}} = persone;
// console.log(firstName, lastName);
```

# Array Destructuring
```js
arr = [1, 2, 3, 4];
const [a, b, , c] = arr;
// console.log(a, b, c);

const line = [[10, 17], [14, 7]];
const [[px1, px2], [py1, py2]] = line;
console.log(`The coordinates: ${px1}, ${px2}, ${py1}, ${py2}`);
```

```js
const dict = {
   duck: 'quake',
   dog: 'wuff',
   mouse: 'squeak',
   hamster: 'squeak',
};

res = Object.entries(dict)
    .filter(([, value]) => value === 'squeak')
    .map(([key]) => key);
console.log(res);


```

# Operator Spread
```js
const dict = {
   duck: 'quake',
   dog: 'wuff',
   mouse: 'squeak',
   hamster: 'squeak',
};

const dict2 = {
   horse: 'igogo',
   cow: 'muuu',
}

res = Object.assign({}, dict, dict2);
console.log(res);
res = { ...dict, ...dict2 };
console.log(res);
```

# Debugger
Just insert 'debugger' in source code and open DevTools in browser:
```js
onPersonSelected = (id) => {
    debugger;
    this.setState({
        selectedPersonId: id
    });
};
```
