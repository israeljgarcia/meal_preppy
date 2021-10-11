<template>
  <div class="ingredientform">
      <IngredientForm />
  </div>
</template>

<script>
import IngredientForm from '../components/IngredientForm.vue';

export default {
  name: 'PantryIngredientForm',
  components: {
    IngredientForm,
  },
};
</script>
