<template>
  <div class="recipes">
      <RecipesList />
  </div>
</template>

<script>
import RecipesList from '../components/RecipesList.vue';

export default {
  name: 'Recipes',
  components: {
    RecipesList,
  },
};
</script>
