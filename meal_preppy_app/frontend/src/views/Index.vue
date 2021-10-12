<template>
  <div>
    <h1 class="is-size-3 has-text-weight-bold">
      This Is Meal Preppy
    </h1>
    <div class="columns is-centered">
      <div class="column"></div>
      <div class="column">
        <h2 class="is-size-4">Meal Prep Automated</h2>
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
  animation: fadeIn linear 2.5s;
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
