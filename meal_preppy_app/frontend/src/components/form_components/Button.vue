<template>
  <div class="container">
    <button
      class="button has-text-centered is-dark mt-2"
      :type="buttonType"
    >
      {{buttonTxt}}
    </button>
  </div>
</template>
<script>
export default {
  name: 'Button',
  props: ['buttonTxt', 'buttonType'],
};
</script>
