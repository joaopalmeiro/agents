# Notes

## Snippets

- `JavaScript/problem-1-multiples-of-3-and-5.js`

```js
function multiplesOf3and5(number) {
  let total = 0;

  for (let i = 0; i < number; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      total += i;
    }
  }

  return total;
}

console.log(multiplesOf3and5(1000)); // Output: 233168
```
