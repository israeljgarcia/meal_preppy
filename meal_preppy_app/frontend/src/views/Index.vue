<template>
  <div>
    <h1 class="is-size-3 has-text-weight-bold m-4">
      This Is Meal Preppy
    </h1>
    <div class="columns is-centered">
      <div class="column">
        <h2 class="is-size-4 has-text-centered">Meal Prep Automated</h2>
      </div>
    </div>
    <div class="images columns is-vcentered is-2 fadein">
      <div class="column card m-3">
        <figure class="image is-4by3">
          <img src="../assets/breakfast.jpeg" alt="">
        </figure>
        <h3 class="is-size-5 has-text-weight-medium m-2">All the meals you love</h3>
      </div>
      <div class="column card m-3">
        <figure class="image is-4by3">
          <img src="../assets/lunch.jpeg" alt="">
        </figure>
        <h3 class="is-size-5 has-text-weight-medium m-2">With the ingredietns you have</h3>
      </div>
      <div class="column card m-3">
        <figure class="image is-4by3">
          <img src="../assets/dessert.jpg" alt="">
        </figure>
        <h3 class="is-size-5 has-text-weight-medium m-2">Waiting at your fingertips</h3>
      </div>
    </div>
    <div class="columns is-centered mt-6">
      <div class="column">
        <a class="button is-dark mt-6" href="/signup">Get Started</a>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Index',
};
</script>
<style scoped>
h2 {
  animation: fadeIn linear 1s;
}

.fadein {
  animation: fadeIn linear 1.5s;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 100;
  }
}
</style>
