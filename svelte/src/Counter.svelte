<script>
  let count = $state(0);

  function increment() {
    count += 1;
  }

  function decrement() {
    count -= 1;
  }

  function reset() {
    count = 0;
  }
</script>

<div class="counter">
  <h2>Counter: {count}</h2>
  <button onclick={decrement} aria-label="decrement">-</button>
  <button onclick={reset} aria-label="reset">Reset</button>
  <button onclick={increment} aria-label="increment">+</button>
</div>

<style>
  .counter {
    text-align: center;
    padding: 1rem;
  }
  button {
    margin: 0 0.5rem;
    padding: 0.5rem 1rem;
    font-size: 1.2rem;
    cursor: pointer;
  }
</style>
