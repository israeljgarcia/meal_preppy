<template>
  <div class="pantry">
    <IngredientList />
  </div>
</template>

<script>
import IngredientList from '../components/IngredientList.vue';

export default {
  name: 'Pantry',
  components: {
    IngredientList,
  },
};
</script>
